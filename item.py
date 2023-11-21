
class Item:
	def __init__(self, name="test", price=1, quantity=1):
		self.name = name
		self.price = price
		self.quantity = quantity
		print("Constructor called with name="+self.name" price="+self.price" quantity="self.quantity)

	def calculate_total_price(self) -> float:
		return self.price * self.quantity



item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
item1.calculate_total_price()

item2 = Item(name="Laptop", price=1000, quantity=3)
item2.calculate_total_price()