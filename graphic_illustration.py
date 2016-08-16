import Tkinter as tk
from PIL import Image, ImageTk
class GraphicMain():
	"""docstring for GraphicMain"""
	def __init__(self, root, components):
		self.router_img = Image.open("resources\\router-icon.png")
		self.pc_img = ImageTk.PhotoImage(Image.open("resources\\pc-icon.png"))
		self.root = root
		self.main_canvas = tk.Canvas(self.root, width = 1000, height = 1000)
		self.main_canvas.pack()
		x=0
		y=1000
		for component in components:			
			self.add_pc(component, x, y )
			x += 128
	def add_pc(self,pc, x, y):
		self.main_canvas.create_image(x, y, anchor = 'sw', image = self.pc_img)
		print y




