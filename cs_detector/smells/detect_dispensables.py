import inspect
from inspect import signature
import gc


class detectdispensables:

    def get_all_classes(self, module_name):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isclass):
            class_list.append(a)
        return class_list

    def lazyclass_check(self, module_name):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isclass):
            obj_count = sum(1 for o in gc.get_referrers(b) if o.__class__ is b)
            if obj_count < 1:
                print(a + '() is a Lazy class. Consider using it or removing it')

    def dataclass_check(self, module_name):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isclass):
            try:
                attr_b = b.hasattr()
            except:
                print("No methods defined in the class : " + a)
            dc_check = inspect.getmembers(b, predicate=inspect.ismethod)
            print(a)
            print(b)
            print(len(dc_check))
            if (len(dc_check)) < 1:
                print("No methods defined in the class : " + a)

    def comment_check(self, module_name, min_words):
        for x, y in inspect.getmembers(module_name, predicate=inspect.isclass):
            method_list = [method for method in dir(y) if method.startswith('__') is False]
            print(method_list)
            print(x)
            b=0
            for a, b in inspect.getmembers(b, predicate=inspect.ismethod):
                cmt = [line for line in inspect.getsourcelines(b)[0] if line.strip().startswith('#')]
                for i in cmt:
                    if(len(i.split()))<min_words:
                        print("Use meaningful comments. Short comments found in the method: " + a)