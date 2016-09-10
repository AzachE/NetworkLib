import Tkinter as tk
from PIL import Image, ImageTk
import constants
class GraphicMain():
	"""docstring for GraphicMain"""
	def __init__(self, root, components, graphic_locationer):
		self.components = components
		self.graphic_locationer = graphic_locationer
		self.root = root
		self.canvas = tk.Canvas(self.root, width = constants.WINDOW_WIDTH, height = constants.WINDOW_HEIGHT)
		self.pc_img = ImageTk.PhotoImage(Image.open("resources\\pc-icon.png").resize((constants.IMG_HEIGHT, constants.IMG_WIDTH)))
		self.router_img = ImageTk.PhotoImage(Image.open("resources\\router-icon.png").resize((constants.IMG_HEIGHT + 32, constants.IMG_WIDTH + 32)))
		self.canvas.pack()
		self.canvas.bind("<Button-1>",self.on_click)
		self.textbox = tk.Text(self.root, height = 8, width= 100)
		self.textbox.pack()
		for i in range(len(components)):#send the coordinates and identifying index
			if components[i].IsRouter():
				self.add_router(components[i], i)	
			else:	
				self.add_pc(components[i], i)


	def add_pc(self,pc, i):
		locations = self.graphic_locationer.get_location(pc)
		self.canvas.create_image(locations[0], locations[1], anchor = 'nw', image = self.pc_img, tags = str(i))# sends index in components' list as tag


	def add_router(self, router ,i):
		locations = self.graphic_locationer.get_location(router)
		self.canvas.create_image(locations[0], locations[1], anchor = 'nw', image = self.router_img, tags = str(i))# sends index in components' list as tag


	def get_component_by_id(self, i):
		return self.components[int(i)] 


	def on_click(self,event):
		if self.canvas.find_withtag("current"):
			self.textbox.delete(1.0,tk.END)
			component = self.get_component_by_id(self.canvas.gettags("current")[0])
			print component.get_string()
			self.textbox.insert(tk.END , component.get_string())


