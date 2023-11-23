
class Communication:
	def __init__(self, id = 100):
		self.package_id = id

	# private method
	def __connect(self, smtp_server):
		pass

	def __create_body(self):
		return f"""
		Hello there,
		The package {self.package_id} is out for delivery
		Regards
		Your local delivery
		"""

	def __send(self):
		pass

	def send_email(self):
		self.__connect()
		self.__create_body()
		self.__send()
