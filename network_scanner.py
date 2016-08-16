#! /usr/bin/env python
# vim: set fenc=utf8 ts=4 sw=4 et :
#
# Layer 2 network neighbourhood discovery tool
# written by Benedikt Waldvogel (mail at bwaldvogel.de)

from __future__ import absolute_import, division, print_function
import logging
from scapy.all import *
import scapy.config
import scapy.layers.l2
import scapy.route
import socket
import math
import errno
from NetworkComponent import *


class Scanner():
    """docstring for Scanner"""
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)-5s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        for network, netmask, _, interface, address in scapy.config.conf.route.routes:

            # skip loopback network and default gw
            if network == 0 or interface == 'lo' or address == '127.0.0.1' or address == '0.0.0.0':
                continue

            if netmask <= 0 or netmask == 0xFFFFFFFF:
                continue

            net = self.to_CIDR_notation(network, netmask)

            if interface != scapy.config.conf.iface:
                # see http://trac.secdev.org/scapy/ticket/537
                self.logger.warn("skipping %s because scapy currently doesn't support arping on non-primary network interfaces", net)
                continue

            if net:
                self.all_components = self.scan_and_print_neighbors(net, interface)
                for comp in self.all_components:
                    comp.print_data()


    def get_components(self):
        """
        returns all components
        """
        return self.all_components    


        

    def long2net(self,arg):
        if (arg <= 0 or arg >= 0xFFFFFFFF):
            raise ValueError("illegal netmask value", hex(arg))
        return 32 - int(round(math.log(0xFFFFFFFF - arg, 2)))


    def to_CIDR_notation(self,bytes_network, bytes_netmask):
        network = scapy.utils.ltoa(bytes_network)
        netmask = self.long2net(bytes_netmask)
        net = "%s/%s" % (network, netmask)
        if netmask < 16:
            self.logger.warn("%s is too big. skipping" % net)
            return None

        return net


    def scan_and_print_neighbors(self,net, interface, timeout=1):#performing the scan
        all_components = []
        self.logger.info("arping %s on %s" % (net, interface))
        try:
            ans, unans = scapy.layers.l2.arping(net, iface=interface, timeout=timeout, verbose=True)
            for s, r in ans.res:
                host = None
                line = r.sprintf("%Ether.src%  %ARP.psrc%")
                ip = r.psrc
                mac = r.hwsrc
                try:
                    hostname = socket.gethostbyaddr(r.psrc)
                    host = hostname[0]
                    line += " " + hostname[0]
                except socket.herror:
                    # failed to resolve
                    pass
                self.logger.info(line)
                net_comp = NetworkComponent(ip,mac,host)
                all_components.append(net_comp)
            return all_components

        except socket.error as e:
            if e.errno == errno.EPERM:     # Operation not permitted
                self.logger.error("%s. Did you run as root?", e.strerror)
            else:
                raise

   