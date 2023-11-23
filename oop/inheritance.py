import csv
from methods import Item


class Phone(Item):
	def __init__(self, name="test", price=1., quantity=1, broken_phones=0):
		# Call super function to have access to all attributes and methods
		super().__init__(
			name, price, quantity
		)

		# Run validations for arguments
		assert broken_phones >= 0, f"Broken phones {quantity} is not greater than or equal to zero"

		# Assign to self object
		self.broken_phones = broken_phones
		print(f"{self.__class__.__name__} constructor called with broken_phones={self.broken_phones}")
