import inspect
from inspect import signature

class detectbloater:

    def get_all_classes(self, module_name):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isclass):
            class_list.append(a)
        return class_list

    def class_check(self, module_name, max_code_lines):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isclass):
            num_code_lines = len([line for line in inspect.getsourcelines(b)[0] if not line.strip().startswith('#')])
            if num_code_lines > max_code_lines:
                print(a + '() is a heavy class. Consider breaking it down')
                print(a + '() -' + str(num_code_lines) + ' lines of code')
#                print(a + "with comments-" + str(len(inspect.getsourcelines(b)[0])))

    def methods_check(self, module_name, max_code_lines):
        for a, b in inspect.getmembers(module_name.Math(), predicate=inspect.ismethod):
            num_code_lines = len([line for line in inspect.getsourcelines(b)[0] if not line.strip().startswith('#')])
            if num_code_lines > max_code_lines:
                print(a + '() is a heavy method. Consider breaking it down')
                print(a + '() - ' + str(num_code_lines) + ' lines of code')
#            print("with comments-" + str(len(inspect.getsourcelines(b)[0])))

    def function_check(self, module_name, max_code_lines):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isfunction):
            num_code_lines = len([line for line in inspect.getsourcelines(b)[0] if not line.strip().startswith('#')])
            if num_code_lines > max_code_lines:
                print(a + '() is a heavy function. Consider breaking it down')
                print("with comments-" + str(len(inspect.getsourcelines(b)[0])))

    def arguments_check(self, module_name, max_args):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isclass):
            method_list = [method for method in dir(a) if method.startswith('__') is False]
            print("$$$$")
            print(method_list)
            num_code_lines = len([line for line in inspect.getsourcelines(method_list[0])[0] if not line.strip().startswith('#')])
            sig = signature(method_list[0])
            parm_length = len(sig.parameters)
            if parm_length > max_args:
                print(a + '() has too many arguments. Consider reducing them')
                print(a + '()\'s arguments -' + str(parm_length))
