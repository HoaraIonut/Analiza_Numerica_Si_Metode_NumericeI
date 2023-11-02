#mai am de rezolvat exercitiul 2

import numpy as np
import matplotlib.pyplot as plt


def MetNaiva(f, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    Y = f(X)
    A = np.vander(X)
    C = np.linalg.solve(A, Y)
    C = np.flip(C)
    y = 0
    for i in range(n + 1):
        y = y + C[i] * x ** i
    return y


a = -1
b = 1
n = 4


def f(x):
    return np.e ** (2 * x)


x_vector = np.linspace(a, b)

y = [MetNaiva(f, a, b, n, x) for x in x_vector]

plt.plot(x_vector, y, c='b', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


def PlotInterpolare(f, a, b, n, metoda):
    X = np.linspace(a, b, n + 1)
    x_grafic = np.linspace(a, b, 50 * n + 1)
    Pn = []
    for x in x_grafic:
        Pn.append(metoda(f, a, b, n, x))
    plt.plot(x_grafic, Pn, c='r', linewidth=1, linestyle='dotted')
    plt.plot(x_grafic, f(x_grafic), c='black', linewidth=1)
    plt.scatter(X, f(X))
    return x

def ErrAbs(f, a, b, n, metoda):
    X = np.linspace(a, b, n + 1)
    x_grafic = np.linspace(a, b, 50 * n + 1)
    Pn = []
    err = []
    for x in x_grafic:
        err.append(f(x) - metoda(f, a, b, n, x))
    plt.plot(x_grafic, err, c='r', linewidth=1, linestyle='dotted')
    #plt.plot(x_grafic, f(x_grafic), c='black', linewidth=1)
    plt.scatter(X, f(X))
    return x

for i in range(1, 5):
    PlotInterpolare(f, a, b, i, MetNaiva)
    plt.title('n = ' + str(i))
    plt.show()

for i in range(1, 5):
    ErrAbs(f, a, b, i, MetNaiva)
    plt.title('n = ' + str(i))
    plt.show()
