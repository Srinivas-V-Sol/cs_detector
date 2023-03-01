import ast
import sys

sys.path.insert(1, 'D:\share\Desktop\Ammu\Software Arch & Design\Course Project\good_smell\good_smell\TestCode')

#import mymath

class Visitor(ast.NodeVisitor):

    def visit_Assign(self, node:ast.Assign):
        print("=======Inside Assign Class========")
        d=[]
        d=node.targets[0]
        v=node.value
        print("target print", d.id)
        print("target print", v.func.id)

def main():
    with open('D:\share\Desktop\Ammu\Software Arch & Design\Course Project\good_smell\\tests\examples\Experiment.py') as f:
        code = f.read()
        node = ast.parse(code)
        Visitor().visit(node)


if __name__ == '__main__':
    main()