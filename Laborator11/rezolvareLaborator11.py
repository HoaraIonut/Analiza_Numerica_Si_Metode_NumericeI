import numpy as np
import matplotlib.pyplot as plt

def CuadMetCoefNedet(f, a, b, n):
    X = np.linspace(a, b, n+1)
    A = []
    B = []
    for i in range(0, n+1):
        li = []
        for it in X:
            li.append(it ** i)
        A.append(li)
        B.append((b ** (i+1) - a ** (i+1))/(i+1))
    W = np.linalg.solve(A, B)
    S = 0
    for k in range(0, n+1):
        S += W[k]*f(X[k])
    return S

def CuadGauss(f, a, b):
    return (f((a+b)/2 - (b-a)/(2*3**(1/2))) + f((a+b)/2 + (b-a)/(2*3**(1/2))))*((b-a)/2)
    
def f(x):
    return np.exp((-1) * x ** 2)

def g(x):
    return 2*x+3

print(CuadMetCoefNedet(f, 0, 1, 1))
print(CuadGauss(f, 0, 1))
