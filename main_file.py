import Tkinter as tk
from network_scanner import *
from graphic_illustration import *
from PIL import Image
from NetworkComponent import *
from graphic_locations import *
from scapy.all import *


def get_components():#performes the scan and calls the components
	scan = Scanner()
	components = scan.get_components()
	return components


def create_main_app(components, graphic_locationer):
	"""
	:param components : get all found components
	:activats the tkinter window 
	"""
	root = tk.Tk()
	app = GraphicMain(root,components, graphic_locationer)
	root.mainloop()

components = []
components = get_components() #after first testing
"""
components.append(NetworkComponent("192.168.1.1","70:54:d2:90:1a:fe","me"))
components.append(NetworkComponent("192.168.1.3","c5:52:da:b0:1a:fe","you"))
components.append(NetworkComponent("192.168.1.4","70:54:d2:90:1a:fe","it"))
components.append(NetworkComponent("192.168.1.6","c5:52:da:b0:1a:fe","this"))
components.append(NetworkComponent("192.168.1.6","c5:52:da:b0:1a:fe","router"))
"""
p = sr1(IP(dst="www.slashdot.org", ttl = 0)/ICMP()/"XXXXXXXXXXX") #get default gateway ip
def_gateway_ip = p.src
for component in components:
	if component.ip == def_gateway_ip:
		component.set_router()
graphic_locationer = GraphicLocationer()
graphic_locationer.set_quantities(len(components))
create_main_app(components, graphic_locationer)