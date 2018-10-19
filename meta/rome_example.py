from darck_meta import Metaticus


class Properitus(metaclass=Metaticus):
    def __init__(self):
        print('When in Rome, do as romans do.')
        print(self)

    def get_centurion(self):
        print('Welcome to the legion.')
        return self._centurion

    def set_centurion(self, value):
        self._centurion = value

    def del_centurion(self):
        del self._centurion

    def get_legion(self):
        return 'LEGION'

    def set_legion(self, value='LEGION'):
        self._legion = 'LEGION'
        print('We Are Legion!')

    def del_legion(self):
        print('You Can Not Defeat The Legion!')


p = Properitus()
print(Properitus.__dict__)
print(p.__dict__)
p.centurion = 1
p.legion = 1
print(p.centurion)
print(p.legion)
print(Metaticus.__dict__)
print(p.__dict__)
