# import ast

# def exclude_imports_functions(code_str):
#     parsed_ast = ast.parse(code_str)
    
#     # Helper function to check if a node is an import statement
#     def is_import(node):
#         return isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom)
    
#     # Helper function to check if a node is a function definition
#     def is_function_def(node):
#         return isinstance(node, ast.FunctionDef)
    
#     # Helper function to reconstruct the code from the AST while excluding imports and functions
#     def reconstruct_code(node):
#         if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
#             return ""
#         return ast.unparse(node)
    
#     # Traverse the AST and reconstruct the filtered code
#     filtered_code = "".join(reconstruct_code(node) for node in parsed_ast.body)
    
#     return filtered_code

# # Example usage:

# with open("inpu.py", "r") as f:
#     code_string = f.read() #

# filtered_code = exclude_imports_functions(code_string)
# print(filtered_code)

# import ast

# with open(r'inpu.py') as file:
#     node = ast.parse(file.read())

# def show_info(functionNode):
#     function_rep = ''
#     function_rep = functionNode.name + '('

#     for arg in functionNode.args.args:
#         function_rep += arg.arg + ','

#     function_rep = function_rep.rstrip(function_rep[-1])
#     function_rep += ')'
#     return function_rep

# result = []
# functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
# classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

# for function in functions:
#     result.append(show_info(function))

# for class_ in classes:
#     methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
#     for method in methods:
#         result.append((class_.name + '.' + show_info(method)))

# print(', '.join(result))
# import ast 

# with open("new_file.py", "r") as f:
#     code = f.read() #


# from pathlib import Path

# parsed_ast = ast.parse(Path("new_file.py").read_text())

# functions = [
#     node
#     for node in ast.walk(parsed_ast)
#     if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
# ]

# for function in functions:
#     print(f"Function name: {function.body}")
#     print(f"Args: {', '.join([arg.arg for arg in function.args.args])}")


# import ast

# def find_function_calls(source_code, function_name):
#     # Convert the source code to its AST representation
#     tree = ast.parse(source_code)

#     # Helper function to traverse the AST and find function calls inside the def function
#     class FunctionCallVisitor(ast.NodeVisitor):
#         def __init__(self, function_name):
#             self.function_name = function_name
#             self.calls = []

#         def visit_Call(self, node):
#             if isinstance(node.func, ast.Name) and node.func.id == self.function_name:
#                 self.calls.append(node)
#             self.generic_visit(node)

#     # Find the def function in the AST
#     for node in ast.walk(tree):
#         if isinstance(node, ast.FunctionDef) and node.name == function_name:
#             function_node = node
#             break
#     else:
#         raise ValueError(f"Function '{function_name}' not found in the code.")

#     # Visit the AST and find function calls inside the def function
#     visitor = FunctionCallVisitor(function_name)
#     visitor.visit(function_node)

#     return visitor.calls

# # Example source code with a 'def' function containing function calls
# source_code = """
# def outer_function():
#     def inner_function():
#         print("Inside inner_function")
    
#     inner_function()
#     inner_function()
# """

# # Find function calls inside the 'inner_function'
# function_calls = find_function_calls(source_code, "inner_function")

# # Print the function calls found
# for call_node in function_calls:
#     print(ast.unparse(call_node))

# import ast

# file_def={}
# i=0
# class PrintToCallFunctionTransformer(ast.NodeTransformer):
#     global file_def
#     def visit_Call(self, node):
#         global i
#         print(node.func)
#         if node.func.value.id=='':
#             file_def[f'{i}']=f'{node.func.id}'
#             i+=1
#         print()
#         self.generic_visit(node)

# with open("abcd.py", "r") as f:
#     code = f.read() #

# tree = ast.parse(code)
# transformer = PrintToCallFunctionTransformer()
# new_tree = transformer.visit(tree)

# print(file_def)

# func_name=list(file_def.values())

# print(func_name)

# import ast

# with open("abcd.py", "r") as f:
#     code = f.read() #

# tree = ast.parse(code)

# result = {
#     node.targets[0].id: node.value.id
#     for node in ast.walk(tree)
#     if isinstance(node, ast.Assign)
# }

# print(result)

# def has_call(tree):
#    return isinstance(tree, ast.Call) or any(has_call(j) for k in getattr(tree, '_fields', []) for j in 
#         (getattr(tree, k) if isinstance(getattr(tree, k), list) else [getattr(tree, k)]))

# r = {ast.unparse(i.targets[0]):ast.unparse(i.value) for i in ast.walk(ast.parse(code)) 
#       if isinstance(i, ast.Assign) and not has_call(i)}

# print(r)

# import ast

# with open("inpu.py", "r") as f:
#     code = f.read() #

# def find_assign_nodes(source_code):
#     tree = ast.parse(source_code)
#     assign_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.Assign)]
#     return assign_nodes

# assign_nodes = find_assign_nodes(code)

# for assign_node in assign_nodes:
#     targets = [target.id for target in assign_node.targets if isinstance(target, ast.Name)]
#     value = ast.unparse(assign_node.value).strip()
#     print(f"{value}")




# import ast

# source = open("new_file.py", "r").read()
# functions = [f.name for f in ast.parse(source).body
#              if isinstance(f, ast.FunctionDef)]

# print(functions)


import os

# # Specify the path to the outer folder
# outer_folder_path = "C:/Users/Dell/Desktop/storage/timeline/2023/july/"
# # Specify the path to the folder inside the outer folder

# inner_folder_path = os.path.join(outer_folder_path, "auto access relate code")

# # Access files inside the inner folder
# for file_name in os.listdir(inner_folder_path):
#     file_path = os.path.join(inner_folder_path, file_name)
#     if os.path.isfile(file_path):
#         # Do something with the file, e.g., read its contents
#         with open(file_path, "r") as file:
#             file_contents = file.read()
#             print(file_contents)

import os

# Specify the path to the folder you want to read
folder_path = "C:/Users/Dell/Desktop/storage/timeline/2023/july/auto access relate code"

# List all the files and subdirectories in the folder
contents = os.listdir(folder_path)

# Print the contents of the folder
print(contents)
