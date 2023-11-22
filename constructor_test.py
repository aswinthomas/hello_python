import constructor


def test_item1():
    item = constructor.Item()
    item.name = "Phone"
    item.price = 100
    item.quantity = 5
    assert (item.calculate_total_price() == 500)
    item.apply_discount()
    assert (item.calculate_total_price() == 400)


def test_item2():
    item = constructor.Item(name="Laptop", price=1000, quantity=3)
    assert (item.calculate_total_price() == 3000)
    item.pay_rate = 0.7
    item.apply_discount()
    assert (item.calculate_total_price() == 2100)


def test_attribute():
    item = constructor.Item()
    # Class level attribute
    assert (constructor.Item.pay_rate == 0.8)
    # Instance level attribute
    assert (item.pay_rate == 0.8)


def test_show_all():
    item1 = constructor.Item("Phone", 100, 1)
    item2 = constructor.Item("Laptop", 1000, 3)
    item3 = constructor.Item("Cable", 10, 5)
    item4 = constructor.Item("Mouse", 50, 5)
    item5 = constructor.Item("Keyboard", 75, 5)

    assert(any(item.name == "Mouse" for item in constructor.Item.all))

