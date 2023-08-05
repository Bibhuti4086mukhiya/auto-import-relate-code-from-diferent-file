#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast
import inspect


# In[2]:


def path_of_file(lib_path=None):
    if lib_path is not None:
        import sys
        import os
        sys.path.insert(0,lib_path)
        with open(F"{lib_path}", "r") as f:
            code = f.read() #
        tree = ast.parse(code)
        return tree,code


# In[3]:


class WildcardImportChecker(ast.NodeVisitor):
    def visit_ImportFrom(self, node):
        for alias in node.names:
            self._file_module[f"{alias.name}"]=f'{node.module}'
        self.generic_visit(node)
    def set_file_module(self, module):
        self._file_module = module
        
def import_module(tree):
#     tree = path_of_file(file_path)
    file_module={}
    visitor = WildcardImportChecker()
    visitor.set_file_module(file_module)
    visitor.visit(tree)
    return file_module


# In[4]:


class PrintToCallFunctionTransformer(ast.NodeTransformer):
    def visit_Call(self, node):
        if node.func.id!='print':
            self._function+=[f'{node.func.id}']
        self.generic_visit(node)
    def set_function(self,id):
        self._function = id

def import_function_name(tree):
#     tree = path_of_file(file_path)
    function=[]
    transformer = PrintToCallFunctionTransformer()
    transformer.set_function(function)
    transformer.visit(tree)
    return function


# In[5]:


def find_assign_nodes(source_code):
    tree = ast.parse(source_code)
    assign_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.Assign)]
    return assign_nodes


# In[6]:


def exclude_imports_functions(code_str):
    parsed_ast = ast.parse(code_str)
    def reconstruct_code(node):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return ""
        return ast.unparse(node)
    filtered_code = "\n".join(reconstruct_code(node) for node in parsed_ast.body)
    return filtered_code


# In[7]:


def call_function(function):
    x_list=set()
    assign_nodes = find_assign_nodes(function)
    for assign_node in assign_nodes:
        targets = [target.id for target in assign_node.targets if isinstance(target, ast.Name)]
        value = ast.unparse(assign_node.value).strip()
        x=''
        if len(targets)==0:
            for j in value:
                if j=='(':
                    x_list.add(x)
                    break
                else:
                    x+=j
    return x_list

# call_function(function)


# In[8]:


def fileOpen(outputFile, content):
    with open(outputFile,'a') as f:
        f.write(content)
        f.close()


# In[9]:


def find_callFunction_inside_function():
    source = (open("output.py", "r").read())
    functions = [f.name for f in ast.parse(source).body
         if isinstance(f, ast.FunctionDef)]
    return functions


# In[10]:


def read_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
    return ast.parse(code, filename=filename)


# In[11]:


def find_function(node, target_function_name):
    for item in ast.walk(node):
        if isinstance(item, ast.FunctionDef) and item.name == target_function_name:
            return item
    return None


# In[18]:


def read_function_write(target_function_node,module):
    if target_function_node:
        # Get the source code of the target function
        with open(module+'.py', 'r') as file:
            lines = file.readlines()
            start_line = target_function_node.lineno - 1
            end_line = target_function_node.end_lineno
            target_function_source = ''.join(lines[start_line:end_line])
            fileOpen('output.py',target_function_source)
            return target_function_source
    else:
        print(f"The function '{target_function_name}' was not found in the file.")


# In[20]:


def newFile(file_name):
    path=path_of_file(file_name)
    tree=path[0]
    import_file=import_module(tree)
    function=import_function_name(tree)
    for i in function:
        module = import_file[i]#file name 
        parsed_tree = read_file(module+'.py')
        target_function_node = find_function(parsed_tree,i)
        target_function_source=read_function_write(target_function_node,module)
        inside_function=call_function(target_function_source)
        outputFile='output.py'
        if len(inside_function)!=0:
            remain_function_write=set(inside_function).difference(set(function))
            for j in remain_function_write:
                parsed_tree = read_file(module+'.py')
                target_function_node = find_function(parsed_tree,j)
                read_function_write(target_function_node,module)
    code=path[1]
    filtered_code = exclude_imports_functions(code)
    fileOpen(outputFile,filtered_code)
file_name='input.py'
newFile(file_name) 


# In[21]:


get_ipython().system('start')


# In[ ]:




