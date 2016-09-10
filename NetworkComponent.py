class NetworkComponent():
	"""docstring for NetworkComponent"""

	def __init__(self, ip = None, mac = None, host = None, info_lst = None): 
		"""
		:params : ip,mac and host(if exists) or a list containing them
		saves the given data for the component, the default is pc.
		"""
		if info_lst:
			ip = str(info_lst[0])
			mac = str(info_lst[1])
			host = str(info_lst[2])
		self.ip = ip
		self.mac = mac
		self.host = host
		self.router = False

	def get_string(self):
		if self.host:
			comp_string = "IPv4: " + self.ip + '\n' + "MAC: " + self.mac + '\n' + "Host Name: " +  self.host
		else:
			comp_string = "IPv4: " + self.ip + '\n' + "MAC: " + self.mac
		return comp_string

	def set_router(self): #sets the component as router
		self.router = True

	def IsRouter(self):#as named
		return self.router
		
		