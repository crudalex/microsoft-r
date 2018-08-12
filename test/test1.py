class Animal(object):
    def __init__(self):
        pass
    def feed(self):
        pass
    def reproduce(self):
        pass
    def sleep(self):
        pass


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        pass
    def feed(self):
        print("fish")
    def reproduce(self):
        print("kitten")
    def sleep(self):
        print("meow")




