from test import *
from test.test1 import Cat
from test.test1 import Animal


c = Cat()
c.feed()
c.sleep()
c.reproduce()

if isinstance(c, Cat):
    print("yes")