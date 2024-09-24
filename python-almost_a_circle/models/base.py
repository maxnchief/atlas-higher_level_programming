#!/usr/bin/python3

''' 
do these quotes give me points?
'''

class Base:\
    ''' this is a mf base class and this is the mf documentaion gimmie point
        @id: The id for a specific instance
    '''
__nb_objects = 0

def __init__(self, id=None):
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects