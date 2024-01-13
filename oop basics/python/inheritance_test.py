from inheritance import Phone


def test_phone1():
	phone = Phone(name="samsungNote10", price=500, quantity=5, broken_phones=1)
	assert (phone.calculate_total_price() == 2500)
	phone.apply_discount()
	assert (phone.calculate_total_price() == 1750)


def test_show_all():
	phone1 = Phone("Phone1", 100, 1, 1)
	phone2 = Phone("Phone2", 1000, 3, 2)
	phone3 = Phone("Phone3", 10, 5, 3)
	phone4 = Phone("Phone4", 50, 5, 4)
	phone5 = Phone("Phone5", 75, 5, 5)
	# Even though we don't append broken_phones to all within Phone.__init__, Item.__init__ appends the Phone object
	assert (any(
		phone.name == "Phone2" and phone.quantity == 3 and phone.price == 1000 and phone.broken_phones == 2 for phone in
		Phone.all))
