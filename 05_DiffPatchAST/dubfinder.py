import sys
import importlib
import inspect
import ast
import textwrap
import difflib
import re

def inspector(module):
    module_memb = {}

    for name, val in inspect.getmembers(module):
        if inspect.isclass(val) and not re.search(".__", name):
            # found class and inspect it's structure
            module_memb.update(inspector(val))
        elif inspect.isfunction(val):
            seq = (''.join(str(val).split()[1:-2])).split('.')
            if len(seq) == 2:
                name = seq[0] + "." + name
            module_memb[name] = val

    return module_memb

all_functions = {}

for mod in sys.argv[1:]:
    module = importlib.import_module(mod)
    module_memb = inspector(module)

    for name in module_memb:
        func = module_memb[name]
        func_code = inspect.getsource(func)
        func_tree = ast.parse(textwrap.dedent(func_code))
        
        for node in ast.walk(func_tree):
            if 'id' in node._fields:
                node.id = '_'
            if 'name' in node._fields:
                node.name = '_'
            if 'arg' in node._fields:
                node.arg = '_'
            if 'attr' in node._fields:
                node.attr = '_'

        all_functions[f"{module.__name__}.{name}"] = ast.unparse(func_tree)

all_functions = dict(sorted(all_functions.items(), key = lambda elem: elem[0]))

for i, fun1 in enumerate(all_functions):
    for j, fun2 in enumerate(all_functions):
        if i > j and difflib.SequenceMatcher(None, all_functions[fun1], all_functions[fun2]).ratio() > 0.95:
            print(f"{fun1} : {fun2}")
