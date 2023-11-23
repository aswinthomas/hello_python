from methods import Item


def test_method():
	Item.instantiate_from_csv()
	assert any(item.name == 'Laptop' and item.quantity == 3 and item.price == 1000.0 for item in Item.all)
	# Although using an instance is not incorrect, there is no reason to do this
	digital_items = Item()
	digital_items.instantiate_from_csv()
	assert any(item.name == 'Laptop' and item.quantity == 3 and item.price == 1000.0 for item in digital_items.all)


def test_is_integer():
	assert Item.is_integer(243) is True
	assert Item.is_integer(34.0) is True
	assert Item.is_integer(10.3) is False
	# Although using an instance is not incorrect, there is no reason to do this
	digital_items = Item()
	assert digital_items.is_integer(243) is True
