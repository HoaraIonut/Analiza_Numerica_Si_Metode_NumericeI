#Rezolvare Exc1

import numpy as np
import matplotlib.pyplot as plt

def MetNeville(f, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    Q = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        Q[i][0] = f(X[i])
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            Q[i][j] = (Q[i][j-1] * (x - X[i - j]) - Q[i - 1][j - 1] * (x - X[i])) / (X[i] - X[i-j])
    y = Q[n][n]
    return y

def f(x):
    return np.exp(2*x)
#
a = - 1
b = 1

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
    plt.legend(['Functia f', 'Polinomul de interpolare Lagrange'])
    plt.show()

for i in range(1, 5):
    PlotInterpolare(f, a, b, i, MetNeville)

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
    PlotInterpolareEroare(f, a, b, i, MetNeville)

#Rezolvare Exc2

def MetNewton(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    def Pk(k, x):
       if k == 0:
           return Y[0]
       else:
           p1 = np.prod([X[k] - X[i] for i in range(k)])
           p2 = np.prod([x - X[i] for i in range(k)])
           ck = (Y[k] - Pk(k - 1, X[k])) / p1
           return Pk(k-1, x) + ck * p2
    return Pk(n, x)

for i in range(1, 5):
    PlotInterpolare(f, a, b, i, MetNewton)

for i in range(1, 5):
    PlotInterpolareEroare(f, a, b, i, MetNewton)

#Rezolvare Exc3

def MetNewtonDD(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    def DD(arr):
        if len(arr) == 1:
            return f(arr[0])
        else:
            return (DD(arr[1:]) - DD(arr[0:-1])) / (arr[-1] - arr[0])
    def Pk(k, x):
        if k == 0:
            return Y[0]
        else:
            produs = np.prod([x - X[i] for i in range(k)])
            return Pk(k-1, x) + DD(X[:k+1]) * produs
    return Pk(n, x)

for i in range(1, 5):
    PlotInterpolare(f, a, b, i, MetNewtonDD)

for i in range(1, 5):
    PlotInterpolareEroare(f, a, b, i, MetNewtonDD)
