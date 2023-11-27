from functools import wraps


def make_blink(function):
	"""Defines the decorator"""

	# This makes the decorator transparent in terms of its name
	@wraps(function)
	# Define the inner function
	def decorator():
		# Grab return value of function being decorated
		ret = function()

		# Add new functionality to the function being decorated
		return "<blink>" + ret + "</blink>"

	return decorator
