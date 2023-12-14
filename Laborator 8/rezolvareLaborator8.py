#Rezolvare Lab8

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(2 * x)
def df(x):
    return 2*f(x)

a = -1
b = 1

#Exc1

def SplineLiniar(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)

    h = np.diff(X)
    A = Y
    B = np.diff(Y) / h

    j = 0
    for i in range(n+1):
        if x > X[i]:
            j = i

    return A[j] + B[j] * (x - X[j])

def SplinePatratic(f, df, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    Y = f(X)

    h = np.diff(X)
    A = Y
    B = []
    B.append(df(x))
    for i in range(1, n):
        B.append(2 / h[i-1] * (Y[i] - Y[i-1]) - B[i-1])
    C = []
    for i in range(n):
        C.append(1 / (h[i] ** 2) * (Y[i + 1] - Y[i])-B[i]/h[i])

    j = 0
    for i in range(n + 1):
        if x > X[i]:
            j = i

    return A[j] + B[j] * (x - X[j]) + C[j]*(x-X[j])**2


def PlotInterpolare(f, a, b, n, metoda):
    plt.title('n = {}'.format(n))

    X = np.linspace(a, b, n+1)
    x_grafic = np.linspace(a, b, 50*n+1)
    Pn = []
    for x in x_grafic:
        Pn.append(metoda(f, a, b, n, x))
    plt.plot(x_grafic, f(x_grafic), c='g', linewidth=1)
    plt.plot(x_grafic, Pn, c='r', linestyle='dotted', linewidth=1)
    for el in X:
        plt.scatter(el, f(el), c='b')
    plt.legend(['Functia f', 'Aproximare f'])
    plt.show()

def PlotInterpolarePatratic(f, a, b, n, metoda):
    plt.title('n = {}'.format(n))

    X = np.linspace(a, b, n+1)
    x_grafic = np.linspace(a, b, 50*n+1)
    Pn = []
    for x in x_grafic:
        Pn.append(metoda(f, df, a, b, n, x))
    plt.plot(x_grafic, f(x_grafic), c='g', linewidth=1)
    plt.plot(x_grafic, Pn, c='r', linestyle='dotted', linewidth=1)
    for el in X:
        plt.scatter(el, f(el), c='b')
    plt.legend(['Functia f', 'Aproximare f'])
    plt.show()

PlotInterpolarePatratic(f, a, b, 5, SplinePatratic)

