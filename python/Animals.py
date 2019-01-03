class Animal:

    name = None

    def __init__(self, name):
        self.name = name

    @staticmethod
    def growl():
        print("Grrrrr")


class Dog(Animal):

    def bark(self):
        print("Woof")


class Cat(Animal):

    def meow(self):
        print("Meow")


if __name__ == "__main__":
    d = Dog('doggie')
    d.bark()

    c = Cat('kittie')
    c.meow()

    a = Animal('ricky')
    print("%s" % a.name)

    print("%s %s %s" % (type(d), type(c), type(a)))

    Dog.growl()
