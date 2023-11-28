class Korean:
	"""Incompatible interface: Korean speaker"""

	def __init__(self):
		self.name = "Korean"

	# different name in each class
	def speak_korean(self):
		return "An-neyong?"


class British:
	"""Incompatible interface: British speaker"""

	def __init__(self):
		self.name = "British"

	# different name in each class
	def speak_english(self):
		return "Hello!"


class SpeakerInterface:
	"""Target Interface"""

	def speak(self):
		pass


class Adapter(SpeakerInterface):
	"""Changes generic method to individualized"""

	def __init__(self, object):
		self._object = object

	def speak(self):
		"""Translates the generic method to individualized"""
		if hasattr(self._object, 'speak_korean'):
			return self._object.speak_korean()
		elif hasattr(self._object, 'speak_english'):
			return self._object.speak_english()
