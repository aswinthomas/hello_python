from enum import Enum
from abc import ABC, abstractmethod


class Starter(Enum):
	SALAD = 1
	SOUP = 2
	BRUSCHETTA = 3
	VEGGIE_STICKS = 4
	CHICKEN_WINGS = 5


class Main(Enum):
	GRILLED_CHICKEN = 1
	PASTA = 2
	VEGGIE_STIR_FRY = 3
	FISH = 4
	PIZZA = 5


class Dessert(Enum):
	FRUIT_SALAD = 1
	ICE_CREAM = 2
	CHOCOLATE_CAKE = 3
	VEGAN_PUDDING = 4
	CHEESECAKE = 5


class Drink(Enum):
	WATER = 1
	VEGAN_SHAKE = 2
	SODA = 3
	FRUIT_JUICE = 4


class Meal:
	def __init__(self, starter=None, main=None, dessert=None, drink=None):
		self._starter = starter
		self._main = main
		self._dessert = dessert
		self._drink = drink

	@property
	def starter(self):
		return self._starter

	@property
	def main(self):
		return self._main

	@property
	def dessert(self):
		return self._dessert

	@property
	def drink(self):
		return self._drink

	@starter.setter
	def starter(self, starter):
		self._starter = starter

	@main.setter
	def main(self, main):
		self._main = main

	@dessert.setter
	def dessert(self, dessert):
		self._dessert = dessert

	@drink.setter
	def drink(self, drink):
		self._drink = drink


class Builder(ABC):
	@abstractmethod
	def add_starter(self, starter):
		pass

	@abstractmethod
	def add_main_course(self, main):
		pass

	@abstractmethod
	def add_dessert(self, dessert):
		pass

	@abstractmethod
	def add_drink(self, drink):
		pass


class MealBuilder(Builder):
	def __init__(self):
		self._starter = None
		self._main = None
		self._dessert = None
		self._drink = None

	def add_starter(self, starter):
		self._starter = starter

	def add_main_course(self, main):
		self._main = main

	def add_dessert(self, dessert):
		self._dessert = dessert

	def add_drink(self, drink):
		self._drink = drink

	def build(self):
		return Meal(self._starter, self._main, self._dessert, self._drink)


class Director:
	def construct_vegan_meal(self, builder):
		builder.add_starter(Starter.SALAD)
		builder.add_main_course(Main.VEGGIE_STIR_FRY)
		builder.add_dessert(Dessert.VEGAN_PUDDING)
		builder.add_drink(Drink.VEGAN_SHAKE)

	def construct_kids_meal(self, builder):
		builder.add_starter(Starter.VEGGIE_STICKS)
		builder.add_main_course(Main.PIZZA)
		builder.add_dessert(Dessert.ICE_CREAM)
		builder.add_drink(Drink.FRUIT_JUICE)

	def construct_low_carb_meal(self, builder):
		builder.add_starter(Starter.SALAD)
		builder.add_main_course(Main.GRILLED_CHICKEN)
		builder.add_dessert(Dessert.FRUIT_SALAD)
		builder.add_drink(Drink.WATER)


director = Director()
builder = MealBuilder()

director.construct_kids_meal(builder)
kids_meal = builder.build()
print("Meal constructed: ")
print("Starter:", kids_meal.starter)
print("Main:", kids_meal.main)
print("Dessert:", kids_meal.dessert)
print("Drink:", kids_meal.drink)

builder = MealBuilder()
director.construct_low_carb_meal(builder)
low_carb = builder.build()
print("Meal constructed: ")
print("Starter:", low_carb.starter)
print("Main:", low_carb.main)
print("Dessert:", low_carb.dessert)
print("Drink:", low_carb.drink)
