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
		self.name = name
		self.price = price
		self.quantity = quantity
		print(
			f"{self.__class__.__name__} constructor called with name={self.name} price={self.price} quantity={self.quantity}")

		# Execution
		Item.all.append(self)

	def calculate_total_price(self) -> float:
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate

	@classmethod
	# Use class method when you want a method to manipulate data structures e.g. instantiate objects
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)

		for item in items:
			Item(name=item.get('name'),
			     price=float(item.get('price')),
			     quantity=int(item.get('quantity')))

	@staticmethod
	# Use static method when it doesnt need to be unique per instance
	def is_integer(num):
		# Count the floats are in form .0 e.g. 5.0, 10.0
		if isinstance(num, float):
			return num.is_integer()
		elif isinstance(num, int):
			return True
		else:
			return False

	# Beautify return of instance
	def __repr__(self):
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


