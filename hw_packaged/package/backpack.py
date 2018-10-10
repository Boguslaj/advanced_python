from collections import namedtuple
from itertools import filterfalse
import os
import sys


def get_abs_real_path():
    """Returns real absolute path to the package"""
    try:
        real_path = __file__ if os.path.islink(__file__) else \
            os.path.realpath(__file__)

        return os.path.dirname(os.path.abspath(real_path))
    except Exception:
        print("Something went wrong ...")
        sys.exit()


def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        point = array[0].efficiency
        for el in array:
            if el.efficiency < point:
                less.append(el)
            elif el.efficiency > point:
                greater.append(el)
            else:
                equal.append(el)
        return sort(greater) + equal + sort(less)
    else:
        return array


class Knapsack(object):
    def __init__(self, capasity=400):
        self.max_capasity = capasity
        self.capasity_left = capasity
        self.stored = []
        self.total_value = 0

    def store(self, item):
        if item.weight <= self.capasity_left:
            self.capasity_left -= item.weight
            self.total_value += item.value
            return item
        return None


def start():

    print("Package:", __package__)
    print("File:", __file__)
    print("Name:", __name__)
    print("Starting application ...")

    path = get_abs_real_path()
    resource_file = os.path.join(path, 'resources', 'stuff.txt')
    with open(resource_file) as f:
        lines = f.readlines()

    Item = namedtuple("Item", 'name weight value efficiency')

    def itemise(line):
        par = line.split(',')
        item = Item(par[0], int(par[1]), int(par[2]),
                    int(par[2]) / int(par[1]))
        return item

    stuff = list(map(itemise, lines))

    stuff = sort(stuff)
    backpack = Knapsack()
    backpack.stored = list(filterfalse(lambda x: x is None,
                                       list(map(backpack.store, stuff))))

    print('Space left: ' + str(backpack.capasity_left))
    for i in backpack.stored:
        print(i.name)
    print('Total value: ' + str(backpack.total_value))

    print("Shutting down ...")
