class Borg:
	_shared_data = {}  # Attribute dict

	def __init__(self):
		self.__dict__ = self._shared_data


class Singleton(Borg):
	"""The singleton class"""

	def __init__(self, **kwargs):
		super().__init__()
		self._shared_data.update(kwargs) # update attribute dict

	def __str__(self):
		return str(self._shared_data) # return for printing
