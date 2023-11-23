from constructor import Item


def test_item1():
	item = Item()
	item.name = "Phone"
	item.price = 100
	item.quantity = 5
	assert (item.calculate_total_price() == 500)
	item.apply_discount()
	assert (item.calculate_total_price() == 400)


def test_item2():
	item = Item(name="Laptop", price=1000, quantity=3)
	assert (item.calculate_total_price() == 3000)
	item.pay_rate = 0.7
	item.apply_discount()
	assert (item.calculate_total_price() == 2100)


def test_attribute():
	item = Item()
	# Class level attribute
	assert (Item.pay_rate == 0.8)
	# Instance level attribute
	assert (item.pay_rate == 0.8)


def test_show_all():
	item1 = Item("Phone", 100, 1)
	item2 = Item("Laptop", 1000, 3)
	item3 = Item("Cable", 10, 5)
	item4 = Item("Mouse", 50, 5)
	item5 = Item("Keyboard", 75, 5)

	assert (any(item.name == "Mouse" and item.quantity == 5 and item.price == 50 for item in Item.all))
