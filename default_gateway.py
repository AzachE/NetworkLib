from scapy.all import *
p = sr1(IP(dst="www.slashdot.org", ttl = 0)/ICMP()/"XXXXXXXXXXX")
print p.src