import Tkinter as tk
from network_scanner import *
from graphic_illustration import *
from PIL import Image
from NetworkComponent import *


def get_components():#performes the scan and calls the components
	scan = Scanner()
	components = scan.get_components()
	return components


def create_main_app(components):
	"""
	:param components : get all found components
	:activats the tkinter window 
	"""
	root = tk.Tk()
	app = GraphicMain(root,components)
	root.mainloop()

components = []
#components = get_components() after first testing
components.append(NetworkComponent("192.168.1.1","70:54:d2:90:1a:fe","me"))
components.append(NetworkComponent("192.168.1.3","c5:52:da:b0:1a:fe","you"))
components.append(NetworkComponent("192.168.1.4","70:54:d2:90:1a:fe","it"))
components.append(NetworkComponent("192.168.1.6","c5:52:da:b0:1a:fe","this"))

create_main_app(components)