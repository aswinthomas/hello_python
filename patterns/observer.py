class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        # if observer not in list, add to list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # notify all, except the one that is updating
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):
    """Concrete subject"""

    def __init__(self, name=""):
        super().__init__()
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp
        # notify
        self.notify()


class Observer:
    def update(self, subject):
        print(f"{self} Temperature updated to {subject.temp}")


c1 = Core("Core 1")
c2 = Core("Core 2")

o1 = Observer()
o2 = Observer()

# attach observers
c1.attach(o1)
c1.attach(o2)

# change temperature
c1.temp = 80
c1.temp = 90