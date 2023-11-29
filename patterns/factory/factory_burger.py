from abc import abstractmethod, ABC
from time import sleep
from enum import Enum


class BurgerMenu(Enum):
    CHEESE = "CHEESE"
    DELUXE_CHEESE = "DELUXE_CHEESE"
    VEGAN = "VEGAN"
    DELUXE_VEGAN = "DELUXE_VEGAN"


class Burger(ABC):
    def __init__(self):
        self.name = ""
        self.bread = ""
        self.sauce = ""
        self.toppings = ""

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass

    def get_name(self):
        return self.name


class CheeseBurger(Burger):

    def __init__(self):
        super().__init__()
        self.name = "Cheese Burger"
        self.bread = "sourdough"
        self.sauce = "ketchup"
        self.toppings = "Onions"

    def prepare(self):
        print(f"Preparing ingredients for {self.name}")
        sleep(1)

    def cook(self):
        print(f"Cooking {self.name}")
        sleep(1)

    def serve(self):
        print(f"Serving {self.name}")
        sleep(1)


# class DeluxeCheeseBurger(Burger):
# class VeganBurger(Burger):
# class DeluxeVeganBurger(Burger):


class BurgerStore(ABC):
    @abstractmethod
    def create_burger(self, item: BurgerMenu) -> Burger:
        pass

    def order_burger(self, item: BurgerMenu) -> Burger:
        order = self.create_burger(item)
        print(f"Making a {order.get_name()}")
        order.prepare()
        order.cook()
        order.serve()
        return order


class CheeseBurgerStore(BurgerStore):
    _burger_dict = {BurgerMenu.CHEESE: CheeseBurger()}

    # , BurgerMenu.DELUXE_CHEESE: DeluxeCheeseBurger(),
    # BurgerMenu.VEGAN: VeganBurger(), BurgerMenu.DELUXE_VEGAN: DeluxeVeganBurger()

    def create_burger(self, item: BurgerMenu) -> Burger:
        if item in self._burger_dict:
            return self._burger_dict[item]


# class VeganBurgerStore(BurgerStore):
# class DeluxeVeganBurgerStore(BurgerStore):
# class DeluxeCheeseBurgerStore(BurgerStore):


store = CheeseBurgerStore()
burger = store.order_burger(BurgerMenu.CHEESE)
print(f"Completed order for a {burger.get_name()}")
