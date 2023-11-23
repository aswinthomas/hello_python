import csv


class Item:
	# Class attribute. Pay rate after 20% discount
	pay_rate = 0.8
	all = []

	# Constructor. passing types is not necessary here due to default assignment
	def __init__(self, name="test", price=1., quantity=1):
		# Run validations for arguments
		assert price > 0, f"Price {price} is not greater than zero"
		assert quantity > 0, f"Quantity {quantity} is not greater than zero"

		# Assign to self object
		# add _ to name since name is read-only now. THis way you can access externally as _name
		# add __ to name, to make it private
		self.__name = name
		self.price = price
		self.quantity = quantity
		print(
			f"{self.__class__.__name__} constructor called with name={self.name} price={self.price} quantity={self.quantity}")

		# Execution
		Item.all.append(self)

	@property
	# Property decorator is a Read only Attribute
	def name(self):
		return self.__name

	@name.setter
	# Encapsulation of implementation details of __name from external user
	def name(self, val):
		if len(val) > 10:
			raise Exception("The name is too long")
		else:
			self.__name = val


