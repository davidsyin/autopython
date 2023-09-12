import random
import sys
from datasets import load_dataset

from variable import Variable
from constant import Constant
from statement import Statement


class PythonGenerator:
    DTYPES = ['integer', 'float', 'string', 'list']

    def __init__(self):
        self.dummy_statement = Statement()
        self.variables = []
        self.issues_dataset = load_dataset("lewtun/github-issues", split="train")

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
                    chosen_vars = random.sample(vars, 2)
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

    def generate_variable_modification(self):
        for i in range(10):
            dtype = random.choice(self.DTYPES)
            vars = self.get_variables_by_type(dtype)
            if len(vars) >= 1:
                chosen_var = random.choice(vars)
                if dtype == "list":
                    if type(chosen_var.value) is int:
                        x = abs(Constant.get_integer() + 1)
                        chosen_var.value.append(x)
                        return chosen_var.name + ".append(" + str(x) + ")"
                    if type(chosen_var.value) is float:
                        x = abs(Constant.get_float() + 1)
                        chosen_var.value.append(x)
                        return chosen_var.name + ".append(" + str(x) + ")"
                    if type(chosen_var.value) is str:
                        idx = random.randint(0, len(self.issues_dataset) - 1)
                        body = Constant.issues_dataset[idx]['body']
                        if body is None:
                            return
                        tokens = body.split(' ')
                        if len(body) < 10:
                            chosen_var.value.append(body)
                            return chosen_var.name + ".append(" + body + ")"
                        if len(tokens) < 20:
                            pos1 = 0
                            pos2 = random.randint(1, len(tokens))
                        else:
                            pos1 = random.randint(0, len(tokens) - 10)
                            length = random.randint(3, 10)
                            pos2 = pos1 + length
                        chosen_var.value.append(" ".join(tokens[pos1:pos2]))
                        return chosen_var.name + ".append(" + " ".join(tokens[pos1:pos2]) + ")"
                else:
                    if dtype == "integer":
                        x = abs(Constant.get_integer() + 1)
                        operation = random.randint(1, 5)
                        if operation == 1:
                            chosen_var.value += x
                            return chosen_var.name + " += " + str(x)
                        if operation == 2:
                            chosen_var.value -= x
                            return chosen_var.name + " -= " + str(x)
                        if operation == 3:
                            chosen_var.value *= x
                            return chosen_var.name + " *= " + str(x)
                        if operation == 4:
                            chosen_var.value /= x
                            return chosen_var.name + " /= " + str(x)
                        if operation == 5:
                            chosen_var.value %= x
                            return chosen_var.name + " %= " + str(x)
                    if dtype == "float":
                        x = abs(Constant.get_float() + 1)
                        operation = random.randint(1, 5)
                        if operation == 1:
                            chosen_var.value += x
                            return chosen_var.name + " += " + str(x)
                        if operation == 2:
                            chosen_var.value -= x
                            return chosen_var.name + " -= " + str(x)
                        if operation == 3:
                            chosen_var.value *= x
                            return chosen_var.name + " *= " + str(x)
                        if operation == 4:
                            chosen_var.value /= x
                            return chosen_var.name + " /= " + str(x)
                    if dtype == "string":
                        idx = random.randint(0, len(self.issues_dataset) - 1)
                        body = Constant.issues_dataset[idx]['body']
                        if body is None:
                            return
                        tokens = body.split(' ')
                        if len(body) < 10:
                            chosen_var.value.append(body)
                            return chosen_var.name + " += " + body
                        if len(tokens) < 20:
                            pos1 = 0
                            pos2 = random.randint(1, len(tokens))
                        else:
                            pos1 = random.randint(0, len(tokens) - 10)
                            length = random.randint(3, 10)
                            pos2 = pos1 + length
                        chosen_var.value += " ".join(tokens[pos1:pos2])
                        return chosen_var.name + ''' += "''' + " ".join(tokens[pos1:pos2]) + '"'


# Testing code

def main() -> int:
    generator = PythonGenerator()

    # print(generator.generate_value_assignment())
    #
    # for i in range(random.randint(5,15)):
    print(generator.generate_value_assignment())
    for i in range(random.randint(5, 15)):
        operation = random.randint(1, 5)
        if operation == 1:
            print(generator.generate_value_assignment())
        elif operation < 4:
            print(generator.generate_variable_assignment())
        else:
            print(generator.generate_variable_modification())
    # print(generator.generate_value_assignment())
    # print(generator.generate_value_assignment('float'))
    # print(generator.generate_value_assignment('string'))
    # print(generator.generate_value_assignment('list'))
    # print(generator.generate_value_assignment('list', 'string'))
    # print(generator.generate_variable_assignment())
    # print(generator.generate_variable_assignment())
    # print(generator.generate_variable_assignment())
    # print(generator.generate_variable_assignment())
    # print(generator.generate_variable_modification())
    return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit

