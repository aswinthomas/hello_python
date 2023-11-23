import pytest

from getter_setter import Item


def test_getter():
	item = Item("my_item", 750)
	# name is a read only attribute
	assert item.name == "my_item"


def test_setter():
	item = Item("my_item", 750)
	# name is also a setter
	item.name = "other_item"
	assert item.name == "other_item"


def test_setter2():
	item = Item("my_item", 750)
	with pytest.raises(Exception) as e:
		item.name = "other_item_from_somewhere"
	assert str(e.value) == "The name is too long"
