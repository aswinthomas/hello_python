import pytest

from getter_setter import Item


def test_get_name():
	item = Item("my_item", 750)
	# name is a read only attribute
	assert item.name == "my_item"


def test_set_name():
	item = Item("my_item", 750)
	# name is also a setter
	item.name = "other_item"
	assert item.name == "other_item"


def test_set_name2():
	item = Item("my_item", 750)
	with pytest.raises(Exception) as e:
		item.name = "other_item_from_somewhere"
	assert str(e.value) == "The name is too long"


def test_increment():
	item = Item("my_item", 750)
	item.apply_increment(0.2)
	assert item.price == 900


def test_discount():
	item = Item("my_item", 750)
	item.apply_discount()
	assert item.price == 720