from prototype import Prototype, Car


def test_prototype():
	c = Car()
	prototype = Prototype()
	prototype.register_object('skylark', c)
	c1 = prototype.clone(name='skylark')
	assert c1 != c
	assert str(c1) == "Skylark | Red | Ex"
