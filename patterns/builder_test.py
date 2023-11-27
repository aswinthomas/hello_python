from builder import SkylarkBuilder, Director


def test_builder():
	builder = SkylarkBuilder()
	director = Director(builder)
	director.construct_car()
	car = director.get_car()

	assert str(car) == "Skylark | Regular tires | Turbo Engine"
