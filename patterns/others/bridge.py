class DrawingAPIOne(object):
	"""Implementation specific abstraction"""

	def draw_circle(self, x, y, radius):
		print(f"API01 drawing circle at ({x},{y}) with radius {radius}")


class DrawingAPITwo(object):
	"""Implementation specific abstraction"""

	def draw_circle(self, x, y, radius):
		print(f"API02 drawing circle at ({x},{y}) with radius {radius}")


class Circle(object):
	"""Implementation independent abstraction"""

	def __init__(self, x, y, radius, drawing_api):
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		"""Implementation specific abstraction"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		"""Implementation independent"""
		self._radius *= percent


circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()
circle2 = Circle(2, 3, 4, DrawingAPITwo())
circle2.draw()
