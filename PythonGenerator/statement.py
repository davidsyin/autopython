import random
import sys

from variable import Variable
from constant import Constant


class Statement(object):
    # Note: These are all binary operators. OPERATOR= is a unary operator.
    BINARY_OPERATORS = ['+', '-', '*', '/', '//', '%', '**']

    MODIFY_OPERATORS = ['+=', '-=', '*=', '/=', '//=', '%=', '**=']

    LIST_BINARY_OPERATORS = ['+']

    variable_generator = None
    constant_generator = None

    def __init__(self):
        Statement.initialize()

    @classmethod
    def initialize(cls):
        if cls.variable_generator is None:
            print("Initializing Statement class...")
            cls.variable_generator = Variable()
            cls.constant_generator = Constant()

    # type should be from 'integer', 'float', 'string', 'list'
    # if type is None, then randomly pick one type
    # returns (variable name, statement)
    @classmethod
    def generate_value_assignment(cls, value_type='integer', list_type='integer'):
        if value_type is None:
            value_type = random.choice(['integer', 'float', 'string', 'list'])
        if list_type is None:
            list_type = random.choice(['integer', 'float', 'string', 'list'])
        if value_type == 'integer':
            var_name = cls.variable_generator.get_numberic_variable_name()
            variable = Variable(var_name, value_type, cls.constant_generator.get_integer())
        elif value_type == 'float':
            var_name = cls.variable_generator.get_numberic_variable_name()
            variable = Variable(var_name, value_type, cls.constant_generator.get_float())
        elif value_type == 'string':
            var_name = cls.variable_generator.get_string_variable_name()
            variable = Variable(var_name, value_type, cls.constant_generator.get_string())
        elif value_type == 'list':
            var_name = cls.variable_generator.get_collection_variable_name()
            variable = Variable(var_name, value_type, cls.constant_generator.get_list_by_type(list_type))
        else:
            raise Exception("Unknown value_type" + value_type)
        statement = variable.name + ' = ' + variable.get_value()
        return (variable, statement)



# Testing code


def main() -> int:
    statement = Statement()
    print(Statement.generate_value_assignment())
    print(Statement.generate_value_assignment())
    print(Statement.generate_value_assignment('float'))
    print(Statement.generate_value_assignment('string'))
    print(Statement.generate_value_assignment('list'))
    print(Statement.generate_value_assignment('list', 'string'))
    return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
