#Exc1
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1

def f(x):
    return np.exp((-1) * x ** 2)

def Cuadraturi(f, a, b, n):
    if n == 1:
        return f((a+b)/2) * (b - a)
    elif n == 2:
        return (f(a) + f(b))/2 * (b - a)
    elif n == 3:
        return  (f(a) + 4*f(a/2+b/2) + f(b))/6
    elif n == 4:
        return (f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b)) / 8
    else:
        return 0

print("Dreptunghi = {}, Trapez = {}, Simpson = {}, Newton = {}".format(Cuadraturi(f, a, b, 1), Cuadraturi(f, a, b, 2), Cuadraturi(f, a, b, 3), Cuadraturi(f, a, b, 4)))

def CuadraturiSumate(f, a, b, n, m):
    X = np.linspace(a, b, m + 1)
    s = 0
    for i in range(1, len(X)):
        if n == 1:
            s += f((X[i-1]+X[i])/2) * (X[i] - X[i-1])
        elif n == 2:
            s += (f(X[i]) + f(X[i-1]))/2 * (X[i] - X[i-1])
        elif n == 3:
            s += (f(X[i-1]) + 4*f(X[i-1]/2+X[i]/2) + f(X[i]))/6
        elif n == 4:
            s += (f(X[i-1]) + 3*f((2*X[i-1]+X[i])/3) + 3*f((X[i-1]+2*X[i])/3) + f(X[i])) / 8
    return s

m = 5

print("Dreptunghi = {}, Trapez = {}, Simpson = {}, Newton = {}".format(CuadraturiSumate(f, a, b, 1, m), CuadraturiSumate(f, a, b, 2, m), CuadraturiSumate(f, a, b, 3, m), CuadraturiSumate(f, a, b, 4, m)))
