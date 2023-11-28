from factory_pet import DogFactory, PetStore, get_pet


def test_dog():
	d = get_pet(pet="dog")
	assert d.speak() == "Woof!"


def test_cat():
	c = get_pet(pet="cat")
	assert c.speak() == "Meow!"


def test_factory():
	# create concrete factory
	factory = DogFactory()
	# create pet store housing our abstract factory
	shop = PetStore(factory)
	# invoke details of the pet
	pet, pet_food = shop.show_pet()
	assert str(pet) == "Dog"
	assert pet.speak() == "Woof!"
	assert pet_food == "Dog food"

