import Tkinter
import constants

class GraphicLocationer():
	"""Creates a map of all the pixels available for images, gets and image and will return coordinates with exact location"""
	def __init__(self):	 # [rows down][columns right], 0 = free, 1 =occupied 
		width = constants.WINDOW_WIDTH
		height = constants.WINDOW_HEIGHT
		self.pc_locations = []
		self.routers_locations = []
		self.pcs_num = 0
		self.routers_num = 0
		self.total_space = width*height
		self.screen_map = self.create_map(width,height)
		print self.screen_map[height - 1][width - 1]


	def create_map(self, width, height):
		map1 = [[0 for x in range(width)] for y in range(height)]
		for i in range(height):
			for j in range(width):
				map1[i][j] = 0 
		return map1


	def set_quantities(self, components):#sets the number of pcs and routers for further locationing
		self.pcs_num = components - 1				#self.pcs_num = components - routers
		self.routers_num = 1
		self.generate_locations()


	def generate_locations(self):
		x = 0
		y = 0
		while ((y + constants.IMG_WIDTH < len(self.screen_map[0])) or (len(self.pc_locations) == self.pcs_num)): #when no space or enough spaces
			while (x + constants.IMG_HEIGHT < len(self.screen_map)) or (len(self.pc_locations) == self.pcs_num):
				location = (y,x)
				self.pc_locations.append(location)
				x += constants.IMG_HEIGHT + 8
			y += constants.IMG_WIDTH + 8
			x = 0
		self.routers_locations.append((len(self.screen_map[0]) - constants.IMG_WIDTH - 32, 0))


	def get_location(self, comp):#recieves a component and returns it's location tuple
		if comp.IsRouter():
			location = self.routers_locations[0]
			self.routers_locations.remove(location)
			return location
		location = self.pc_locations[0]
		self.pc_locations.remove(location)
		return location
 	#TODO: mark taken locations for further developments




GraphicLocationer()