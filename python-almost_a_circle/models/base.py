#!/usr/bin/python3
class Base:\
''' this is a mf base class and this is the mf documentaion gimmie points
'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects