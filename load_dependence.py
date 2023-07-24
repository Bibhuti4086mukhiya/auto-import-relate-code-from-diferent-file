import ast
import inspect

with open("inpu.py", "r") as f:
    code = f.read() #
    
file_module={}
class WildcardImportChecker(ast.NodeVisitor):
    global file_module
    def visit_ImportFrom(self, node):
        for alias in node.names:
            file_module[f"{alias.name}"]=f'{node.module}'
        self.generic_visit(node)
    
tree = ast.parse(code)
visitor = WildcardImportChecker()
visitor.visit(tree)

file_def={}
i=0
class PrintToCallFunctionTransformer(ast.NodeTransformer):
    global file_def
    def visit_Call(self, node):
        global i
        if node.func.id!='print':
            file_def[f'{i}']=f'{node.func.id}'
            i+=1
        self.generic_visit(node)

transformer = PrintToCallFunctionTransformer()
new_tree = transformer.visit(tree)

func_name=list(file_def.values())

try:
    file=open('new_file.py','a')
except:
    pass

def find_assign_nodes(source_code):
    tree = ast.parse(source_code)
    assign_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.Assign)]
    return assign_nodes

def exclude_imports_functions(code_str):
    parsed_ast = ast.parse(code_str)
    def reconstruct_code(node):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return ""
        return ast.unparse(node)
    filtered_code = "\n".join(reconstruct_code(node) for node in parsed_ast.body)
    return filtered_code

def newFile(func_name):
    # sub_def=set()
    x_list=[]
    for i in func_name:
        module = __import__(str(file_module[i]))#file name 
        source_code = inspect.getsource(getattr(module,i))#def func name
        file.write(source_code)
        assign_nodes = find_assign_nodes(source_code)
        for assign_node in assign_nodes:
            targets = [target.id for target in assign_node.targets if isinstance(target, ast.Name)]
            value = ast.unparse(assign_node.value).strip()
            x=''
            if len(targets)==0:
                for j in value:
                    if j=='(':
                        x_list+=[x]
                        break
                    else:
                        x+=j

    print(x_list)
    if len(x_list)!=0:
        source = (open("new_file.py", "r").read())
        print(source)
        functions = [f.name for f in ast.parse(source).body
             if isinstance(f, ast.FunctionDef)]
        print(functions)
        
    file.write(source_code)

newFile(func_name) 



filtered_code = exclude_imports_functions(code)
file.write(filtered_code)
file.close()

