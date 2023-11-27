from abc import ABC, abstractmethod


class Pet(ABC):
	"""Abstract product"""

	@abstractmethod
	def speak(self):
		pass


class Dog(Pet):
	"""Concrete Product"""

	def __init__(self, name):
		self.name = name

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"


class PetFactory(ABC):
	"""Abstract factory"""

	@abstractmethod
	def get_pet(self):
		pass

	@abstractmethod
	def get_food(self):
		pass


class DogFactory(PetFactory):
	"""Concrete factory"""

	def get_pet(self):
		"""Returns Dog object"""
		return Dog(name="Marley")

	def get_food(self):
		"""Returns Dog food"""
		return "Dog food"


class PetStore:
	"""Client using the Factory"""

	def __init__(self, pet_factory=None):
		"""pet_factory is our Abstract Factory"""
		self._pet_factory = pet_factory

	def show_pet(self):
		"""Utility method to display details of object"""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()
		return pet, pet_food


class Cat:
	"""One of the objects to be returned"""

	def __init__(self, name):
		self.name = name

	def speak(self):
		return "Meow!"


# You dont have to know which family of pets it belongs, until runtime
# This is created without inheritance since py is dynamically typed language and does not require abstract classes
def get_pet(pet="dog"):
	"""The Factory Method"""
	pets = dict(dog=Dog("Marley"), cat=Cat("Peace"))
	return pets[pet]
