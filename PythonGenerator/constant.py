import random
import numpy
from datasets import load_dataset


class Constant(object):
    issues_dataset = None

    def __init__(self):
        Constant.initialize()

    @classmethod
    def initialize(cls):
        if cls.issues_dataset is None:
            print("Initializing Constant class...")
            cls.issues_dataset = load_dataset("lewtun/github-issues", split="train")
        else:
            return

    @classmethod
    def get_integer(cls, mean=5, always_positive=True):
        v = int(round(numpy.random.exponential(mean)))
        if always_positive:
            return v
        else:
            return random.choice([-1, 1]) * v

    @classmethod
    def get_float(cls, mean=5.0, always_positive=True):
        v = numpy.random.exponential(mean)
        if always_positive:
            return v
        else:
            return random.choice([-1, 1]) * v

    # If num_tokens==None, return a string of random length
    def get_string(self, num_tokens=None):
        idx = random.randint(0, len(self.issues_dataset) - 1)
        body = Constant.issues_dataset[idx]['body']
        if body is None:
            return ""
        tokens = body.split(' ')
        if num_tokens is None:
            if len(body) < 10:
                return body
            if len(tokens) < 20:
                pos1 = 0
                pos2 = random.randint(1, len(tokens))
            else:
                pos1 = random.randint(0, len(tokens) - 10)
                length = random.randint(3, 10)
                pos2 = pos1 + length
            return " ".join(tokens[pos1:pos2])
        else:
            if len(tokens) <= num_tokens:
                return body
            else:
                return " ".join(tokens[0:num_tokens])

    # If length==None, return a list of random length between 1 and max_length
    @classmethod
    def get_int_list(cls, length=None, max_length=10, mean=5, always_positive=True):
        output = []
        if length is None:
            length = random.randint(1, max_length)
        for i in range(length):
            output.append(cls.get_integer(mean, always_positive))
        return output

    # If length==None, return a list of random length between 1 and max_length
    @classmethod
    def get_float_list(cls, length=None, max_length=10, mean=5.0, always_positive=True):
        output = []
        if length is None:
            length = random.randint(1, max_length)
        for i in range(length):
            output.append(cls.get_float(mean, always_positive))
        return output

    # If length==None, return a list of random length between 1 and max_length
    def get_string_list(self, length=None, max_length=10):
        output = []
        if length is None:
            length = random.randint(1, max_length)
        for i in range(length):
            output.append(self.get_string())
        return output

    def get_list_by_type(self, list_type, length=None, max_length=10):
        if list_type == 'integer':
            return self.get_int_list(length, max_length)
        elif list_type == 'float':
            return self.get_float_list(length, max_length)
        elif list_type == 'string':
            return self.get_string_list(length, max_length)
        else:
            raise Exception("Unknown type" + list_type)
