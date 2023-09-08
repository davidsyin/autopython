import random
import sys

from variable import Variable
from constant import Constant
from statement import Statement


class PythonGenerator:

    DTYPES = ['integer', 'float', 'string', 'list']

    def __init__(self):
        self.dummy_statement = Statement()
        self.variables = []

    def get_variables_by_type(self, dtype):
        return [x for x in self.variables if x.dtype == dtype]

    def generate_value_assignment(self, value_type='integer', list_type='integer'):
        var, statement = Statement.generate_value_assignment(value_type, list_type)
        self.variables.append(var)
        return statement

    def generate_variable_assignment(self, value_type='integer', prob_existing_variable=0.5):
        if random.random() < prob_existing_variable:
            # Assign an existing variable
            for i in range(10):
                dtype = random.choice(self.DTYPES)
                vars = self.get_variables_by_type(dtype)
                if len(vars) >= 2:
                    chosen_vars = random.choices(vars, k=2)
                    chosen_vars[0].value = chosen_vars[1].value
                    return chosen_vars[0].name + ' = ' + chosen_vars[1].name
        #
        if len(self.variables) == 0:
            return self.generate_value_assignment(value_type)
        else:
            var_name = Variable.get_random_variable_name()
            var_existing = random.choice(self.variables)
            var = Variable(var_name, var_existing.dtype, var_existing.value)
            self.variables.append(var)
            return var.name + ' = ' + var_existing.name



# Testing code


def main() -> int:
    generator = PythonGenerator()
    print(generator.generate_value_assignment())
    print(generator.generate_value_assignment())
    print(generator.generate_value_assignment('float'))
    print(generator.generate_value_assignment('string'))
    print(generator.generate_value_assignment('list'))
    print(generator.generate_value_assignment('list', 'string'))
    print(generator.generate_variable_assignment())
    print(generator.generate_variable_assignment())
    print(generator.generate_variable_assignment())
    print(generator.generate_variable_assignment())
    return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit

