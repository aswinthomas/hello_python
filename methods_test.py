import methods


def test_method():
	methods.Item.instantiate_from_csv()
	assert any(item.name == 'Laptop' and item.quantity == 3 and item.price == 1000.0 for item in methods.Item.all)
	# Although using an instance is not incorrect, there is no reason to do this
	digital_items = methods.Item()
	digital_items.instantiate_from_csv()
	assert any(item.name == 'Laptop' and item.quantity == 3 and item.price == 1000.0 for item in digital_items.all)


def test_is_integer():
	assert methods.Item.is_integer(243) is True
	assert methods.Item.is_integer(34.0) is True
	assert methods.Item.is_integer(10.3) is False
	# Although using an instance is not incorrect, there is no reason to do this
	digital_items = methods.Item()
	assert digital_items.is_integer(243) is True
