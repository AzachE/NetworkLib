import Tkinter as tk
from PIL import Image, ImageTk
class GraphicMain():
	"""docstring for GraphicMain"""
	def __init__(self, root, components):
		self.components = components
		self.router_img = Image.open("resources\\router-icon.png")
		self.pc_img = ImageTk.PhotoImage(Image.open("resources\\pc-icon.png").resize((64,64)))
		self.root = root
		self.canvas = tk.Canvas(self.root, width = 1000, height = 400)
		self.canvas.pack()
		self.canvas.bind("<Button-1>",self.on_click)
		self.textbox = tk.Text(self.root, height = 8, width= 100)
		self.textbox.pack()
		x=0
		y=400
		for i in range(len(components)):#send the coordinates and identifying index		
			self.add_pc(components[i], x, y, i)
			x += 80

	def add_pc(self,pc, x, y, i):
		self.canvas.create_image(x, y, anchor = 'sw', image = self.pc_img, tags = str(i))# sends index in components' list as tag


	def get_component_by_id(self, i):
		return self.components[int(i)] 


	def on_click(self,event):
		if self.canvas.find_withtag("current"):
			self.textbox.delete(1.0,tk.END)
			component = self.get_component_by_id(self.canvas.gettags("current")[0])
			print component.get_string()
			self.textbox.insert(tk.END , component.get_string())


