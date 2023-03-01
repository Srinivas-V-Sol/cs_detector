
import ast

import os
import sys

from importlib.machinery import SourceFileLoader
from smells.detect_bloater import detectbloater
from smells.detect_dispensables import detectdispensables


max_lines_class_method = 25
max_params_method = 4
min_comment_words = 25
# caution: path[0] is reserved for script path (or '' in REPL)
dir= 'D:\share\Desktop\Ammu\Software Arch & Design\Course Project\good_smell\good_smell\TestCode'


sys.path.insert(1, dir)
print(os.listdir(dir))
i = 0
my_module = []

bloatcheck = detectbloater()
dispensablecheck = detectdispensables()

for files in os.listdir(dir):
    if files.endswith(".py"):
        import_path = os.path.join(dir, files)
        print("\n================================")
        print("Running on File: " + str(os.path.basename(import_path).split('/')[-1]))
        my_module.append(SourceFileLoader(os.path.split(import_path)[1].rstrip(".py"),import_path).load_module())
        print(my_module[i])
        bloatcheck.class_check(my_module[i], max_lines_class_method)
        bloatcheck.methods_check(my_module[i], max_lines_class_method)
        bloatcheck.arguments_check(my_module[i], max_params_method)
        dispensablecheck.lazyclass_check(my_module[i])
        dispensablecheck.dataclass_check(my_module[i])
        dispensablecheck.comment_check(my_module[i], min_comment_words)
        i = i+1
# import_path = os.path.join(dir, 'mymath.py')
# my_module = (SourceFileLoader(os.path.split(import_path)[1].rstrip(".py"),import_path).load_module())
#
# bloatcheck = detectbloater()
# dispensablecheck = detectdispensables()
# bloatcheck.class_check(my_module, max_lines_class_method)
# bloatcheck.methods_check(my_module, max_lines_class_method)
# bloatcheck.arguments_check(my_module, max_params_method)
# dispensablecheck.lazyclass_check(my_module)
# dispensablecheck.dataclass_check(my_module)
# dispensablecheck.comment_check(my_module, min_comment_words)

