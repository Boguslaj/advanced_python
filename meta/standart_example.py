from darck_meta import Metaticus


class Example(metaclass=Metaticus):
   def __init__(self):
       self._x = None

   def get_x(self):
       return self._x

   def set_x(self, value):
       self._x = value

   def get_y(self):
       return 'y'


ex = Example()
ex.x = 255
print(ex.x)
print(ex.y)

