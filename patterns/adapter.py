class Korean:
	"""Korean speaker"""

	def __init__(self):
		self.name = "Korean"

	# different name in each class
	def speak_korean(self):
		return "An-neyong?"


class British:
	"""British speaker"""

	def __init__(self):
		self.name = "British"

	# different name in each class
	def speak_english(self):
		return "Hello!"


class Adapter:
	"""Changes generic method to individualized"""

	def __init__(self, object, **adapted_method):
		self._object = object

		# add new dict that establishes mapping
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		"""return attributes"""
		return getattr(self._object, attr)
