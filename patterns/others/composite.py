class Component(object):
	"""Abstract class"""

	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass


class Child(Component):
	"""Concrete class"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Store name of child
		self.name = args[0]

	def component_function(self):
		print(f"{self.name}")
		return self.name


class Composite(Component):
	"""Concrete class that maintains tree"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# store name of composite object
		self.name = args[0]
		# child items
		self.children = []

	def append_child(self, child):
		self.children.append(child)

	def remove_child(self, child):
		self.children.remove(child)

	def component_function(self):
		res = []
		print(f"{self.name}")
		res.append(self.name)
		for child in self.children:
			child_name = child.component_function()
			res.append(child_name)
		return res
