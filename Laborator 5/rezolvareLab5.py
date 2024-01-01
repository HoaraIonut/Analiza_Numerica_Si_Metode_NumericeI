#Rezolvare Lab5

import numpy as np
import  matplotlib.pyplot as plt

#Rezolvare exc 1

def f(x):
    return np.exp(2 * x)

a = -1
b = 1

def MetNaiva(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)

    A = np.vander(X)
    C = np.flip(np.linalg.solve(A, Y))

    y = 0
    for i in range(n + 1):
        y += C[i] * x ** i
    return y

def PlotInterpolareMetNaiva(f, a, b, n, metoda):
    X = np.linspace(a, b, n + 1)
    X_grafic = np.linspace(a, b, 50 * n + 1)
    Pn = []

    for x in X_grafic:
        Pn.append(metoda(f, a, b, n, x))

    plt.subplot(1, 2, 1)
    plt.title(" (Met Naiva) n = {}".format(n))
    plt.plot(X_grafic, f(X_grafic), c='r', linewidth=1)
    plt.plot(X_grafic, Pn, c='b', linewidth=1)

    plt.scatter(X, f(X), c='y')

    plt.subplot(1, 2, 2)
    plt.title("(Met Naiva) Eroarea absoluta pt n = {}".format(n))
    plt.plot(X_grafic, abs(f(X_grafic) - Pn))

    plt.show()

#Rezolvare exc 2

def MetLagrange(f, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    def L(n, k):
        P1 = 1
        P2 = 1
        for i in range(n+1):
            if i != k:
                P1 *= (x - X[i])
                P2 *= (X[k] - X[i])
        return P1/P2

    y = 0
    for k in range(0, n+1):
        y += (L(n, k) * f(X[k]))

    return y

def PlotInterpolareLagrange(f, a, b, n, metoda):
    X = np.linspace(a, b, n+1)
    X_grafic = np.linspace(a, b, 50*n+1)
    Pn = []

    for x in X_grafic:
        Pn.append(metoda(f, a, b, n, x))

    plt.subplot(1, 2, 1)
    plt.title("(Metoda Lagrange) n = {}".format(n))
    plt.plot(X_grafic, Pn, c='r')
    plt.plot(X_grafic, f(X_grafic), c='b')
    plt.scatter(X, f(X), c='y')

    plt.subplot(1, 2, 2)
    plt.title("(Metoda Lagrange) Eroarea absoluta pt n = {}".format(n))
    plt.plot(X_grafic, abs(f(X_grafic)-Pn))
    plt.show()

for i in range(1, 5):
    PlotInterpolareLagrange(f, a, b, i, MetLagrange)
