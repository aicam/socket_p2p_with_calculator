import numpy as np
def Add(params):
    return np.add(int(params[0]),int(params[1]))
def Substract(params):
    return np.subtract(params[0], params[1])
def Divide(params):
    return np.divide(int(params[0]), int(params[1]))
def Multiply(params):
    return np.multiply(int(params[0]), int(params[1]))
def Sin(params):
    return np.sin(int(params[0]))
def Cos(params):
    return np.cos(int(params[0]))
def Tan(params):
    return np.tan(int(params[0]))
def Cot(params):
    return 1/np.tan(int(params[0]))