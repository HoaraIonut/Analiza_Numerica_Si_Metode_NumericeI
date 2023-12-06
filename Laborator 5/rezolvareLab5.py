import numpy as np
import matplotlib.pyplot as plt

def MetNaiva(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    A = np.vander(X)
    C = np.linalg.solve(A, Y)
    C = np.flip(C)
    y = 0
    for i in range(n+1):
        y += C[i] * x ** i
    return y

def f(x):
    return np.exp(2*x)
#
a = - 1
b = 1

def PlotInterpolare(f, a, b, n, metoda):
    plt.title('n = {val}'.format(val=n))
    X = np.linspace(a, b, n+1)
    x_grafic = np.linspace(a, b, 50*n+1)
    Pn = []
    for x in x_grafic:
        Pn.append(metoda(f, a, b, n, x))
    plt.plot(x_grafic, f(x_grafic), c='g', linewidth=1)
    plt.plot(x_grafic, Pn, c='r', linestyle='dotted', linewidth=1)
    for el in X:
        plt.scatter(el, f(el), c='b')
    plt.legend(['Functia f', 'Polinomul de interpolare Lagrange'])
    plt.show()

for i in range(1, 5):
    PlotInterpolare(f, a, b, i, MetNaiva)

def PlotInterpolareEroare(f, a, b, n, metoda):
    plt.title('Eroare absoluta pt n = {val}'.format(val=n))
    X = np.linspace(a, b, n+1)
    x_grafic = np.linspace(a, b, 50*n+1)
    Pn = []
    for x in x_grafic:
        Pn.append(metoda(f, a, b, n, x))
    plt.plot(x_grafic, abs(f(x_grafic) - Pn), c='r')
    plt.show()

for i in range(1, 5):
    PlotInterpolareEroare(f, a, b, i, MetNaiva)

#Rezolvare Ex2

def MetLagrange(f, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    Y = f(X)
    y = 0
    for k in range(n+1):
        L = 1
        for i in range(n + 1):
            if i != k:
                L = L * (x-X[i])/(X[k] - X[i])
        y = y + L * Y[k]
    return y

for i in range(1, 5):
    PlotInterpolare(f, a, b, i, MetLagrange)

for i in range(1, 5):
    PlotInterpolareEroare(f, a, b, i, MetLagrange)

