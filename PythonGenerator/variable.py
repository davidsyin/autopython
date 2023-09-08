import random
import string
import numpy as np

class Variable(object):
    # ITERATORS = ['i', 'j', 'k', 'i1', 'i2', 'j1', 'j2']
    #
    # NUM_VARIABLES = ['x', 'y', 'z', 'w', 'm', 'n', 'x1', 'x2', 'y1', 'y2']
    #
    # STR_VARIABLES = ['s', 't', 'u', 'v']
    #
    # COLLECTION_VARIABLES = ['a', 'b', 'c', 'd']

    def __init__(self, name=None, dtype=None, value=None):
        self.name = name
        self.dtype = dtype
        self.value = value

    def __str__(self):
        return "{" + self.name + '|' + self.dtype + '|' + self.get_value() + "}"

    def get_value(self):
        if self.dtype in ['integer', 'float', 'list']:
            return str(self.value)
        elif self.dtype in ['string']:
            return '"' + self.value + '"'
        else:
            return None

    @classmethod
    def get_random_variable_name(cls, length=None):
        if length == None:
            length = max(1, min(10, int(np.random.exponential(3.0))))
        output = random.choice(string.ascii_lowercase + '_')
        while len(output) < length:
            output += random.choice(string.ascii_lowercase + string.digits + '_')
        return output

    @classmethod
    def get_iterator_variable_name(cls):
        #return random.choice(cls.ITERATORS)
        return cls.get_random_variable_name()

    @classmethod
    def get_numberic_variable_name(cls):
        #return random.choice(cls.NUM_VARIABLES)
        return cls.get_random_variable_name()

    @classmethod
    def get_string_variable_name(cls):
        #return random.choice(cls.STR_VARIABLES)
        return cls.get_random_variable_name()

    @classmethod
    def get_collection_variable_name(cls):
        #return random.choice(cls.COLLECTION_VARIABLES)
        return cls.get_random_variable_name()



