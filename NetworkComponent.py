class NetworkComponent():
	"""docstring for NetworkComponent"""

	def __init__(self, ip = None, mac = None, host = None, info_lst = None): 
		"""
		:params : ip,mac and host(if exists) or a list containing them
		saves the given data for the component
		"""
		if info_lst:
			ip = info_lst[0]
			mac = info_lst[1]
			host = info_lst[2]
		self.ip = ip
		self.mac = mac
		self.host = host

	def print_data(self):
		print self.ip
		print self.mac
		print self.host
		
		