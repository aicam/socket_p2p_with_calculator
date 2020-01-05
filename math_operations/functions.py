import numpy as np
def Add(params):
    return np.add(np.array(params[0]),np.array(params[1]))
def Substract(params):
    return np.subtract(np.array(params[0]), np.array(params[1]))
def Divide(params):
    return np.divide(np.array(params[0]), np.array(params[1]))
def Multiply(params):
    return np.multiply(np.array(params[0]), np.array(params[1]))
def Sin(params):
    return np.sin(params[0])
def Cos(params):
    return np.cos(params[0])
def Tan(params):
    return np.tan(params[0])
def Cot(params):
    return 1/np.tan(params[0])