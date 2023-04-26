
def special_function(inp1):
    print('I am in special function : ', inp1)
    
def normal_function(inp1):
    print('I am in Normal function : ', inp1)

# normal_function(1)    

def hof_function(func_arg , func_arg_input):
    func_arg(func_arg_input)

hof_function(normal_function,2)    
hof_function(special_function,200)  