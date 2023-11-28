class House(object):
    """Class being vivited"""

    def accept(self, visitor):
        """Interface to accept visitor"""
        visitor.visit(self)

    def work_on_ac(self, ac_specialist):
        print(f"{self} worked on by {ac_specialist}")

    def work_on_electricity(self, electrician):
        print(f"{self} worked on by {electrician}")

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""

    def __str__(self):
        return self.__class__.__name__


class ACSpecialist(Visitor):
    def visit(self, house):
        house.work_on_ac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)

ac_sp = ACSpecialist()
elec_sp = Electrician()

house = House()
house.accept(ac_sp)
house.accept(elec_sp)