from .functions import *
def recv_data(params):
    return_array = {
        'sin': Sin,
        'cos': Cos,
        'tan': Tan,
        'cot': Cot,
        'add': Add,
        'subtract': Substract,
        'divide': Divide,
        'multiply': Multiply,
    }
    print(params)
    return return_array.get(params[0],lambda i:False)(params)