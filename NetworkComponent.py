class NetworkComponent():
	"""docstring for NetworkComponent"""

	def __init__(self, ip = None, mac = None, host = None, info_lst = None): 
		"""
		:params : ip,mac and host(if exists) or a list containing them
		saves the given data for the component
		"""
		if info_lst:
			ip = str(info_lst[0])
			mac = str(info_lst[1])
			host = str(info_lst[2])
		self.ip = ip
		self.mac = mac
		self.host = host

	def get_string(self):
		comp_string = self.ip + '\n' + self.mac + '\n' + self.host
		return comp_string
		
		