import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(2 * x)

a = -1
b = 1

def MetNeville(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Q = np.zeros((n+1, n+1))
    for i in range(n+1):
        Q[i, 0] = f(X[i])
    for i in range(1, n+1):
        for j in range(1, n+1):
            Q[i, j] = (Q[i, j-1] * (x-X[i-j]) - Q[i-1, j-1]*(x-X[i])) / (X[i] - X[i-j])
    return Q[n, n]

def PlotInterpolareMetNeville(f, a, b, n, metoda):
    X = np.linspace(a, b, n+1)
    X_grafic = np.linspace(a, b, 50*n+1)
    Pn = []

    for x in X_grafic:
        Pn.append(metoda(f, a, b, n, x))

    plt.subplot(1, 2, 1)
    plt.title("(Met Neville) n = {}".format(n))
    plt.plot(X_grafic, Pn, c='r')
    plt.plot(X_grafic, f(X_grafic), c='b')
    plt.scatter(X, f(X), c='y')

    plt.subplot(1, 2, 2)
    plt.title("(Met Neville) Eroare absoluta pt n = {}".format(n))
    plt.plot(X_grafic, abs(f(X_grafic) - Pn))
    plt.show()

# for i in range(1, 5):
#     PlotInterpolareMetNeville(f, a, b, i, MetNeville)


#Rezolvare Exc2

def MetNewton(f, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    c = f(X[0])

    def C(k):
        p = 1

        for i in range(k):
            p *= (X[k] - X[i])

        return (f(X[k]) - P(k - 1, X[k])) / p

    def P(k, x):
        if k == 0:
            return c
        else:
            p = 1
            for i in range(k):
                p *= (x - X[i])
            return P(k - 1, x) + C(k) * p

    return P(n, x)

def PlotInterpolareMetNewton(f, a, b, n, metoda):
    X = np.linspace(a, b, n+1)
    X_grafic = np.linspace(a, b, 50 * (n+1))
    Pn = []

    for x in X_grafic:
        Pn.append(metoda(f, a, b, n, x))

    plt.subplot(1, 2, 1)
    plt.title("(Met Newton) pt n = {}".format(n))
    plt.plot(X_grafic, Pn, c='r')
    plt.plot(X_grafic, f(X_grafic), c='b')
    plt.scatter(X, f(X), c='y')

    plt.subplot(1, 2 ,2)
    plt.title("(Met Newton) Eroarea absoluta pt n={}".format(n))
    plt.plot(X_grafic, abs(f(X_grafic) - Pn))
    plt.show()


# for i in range(1, 5):
#     PlotInterpolareMetNewton(f, a, b, i, MetNewton)

def MetNewtonDD(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    q = f(X[0])

    def c(inc, fin):
        if(inc == fin):
            return f(X[inc])
        else:
            return (c(inc+1, fin) - c(inc, fin-1))/(X[fin] - X[inc])

    def P(k, x):
        if k == 0:
            return q
        else:
            p = 1
            for i in range(k):
                p *= (x - X[i])
            return P(k - 1, x) + (c(0, k) * p)

    return P(n, x)

def PlotInterpolareMetNewtonDD(f, a, b, n, metoda):
    X = np.linspace(a, b, n+1)
    X_grafic = np.linspace(a, b, 50*(n+1))
    Pn = []

    for x in X_grafic:
        Pn.append(metoda(f, a, b, n, x))

    plt.subplot(1, 2, 1)
    plt.title("(Met Newton DD) n = {}".format(n))
    plt.plot(X_grafic, f(X_grafic), c='r')
    plt.plot(X_grafic, Pn, c='b')
    plt.scatter(X, f(X), c='y')

    plt.subplot(1, 2, 2)
    plt.title("(Met Newton DD) Eroare abs pt n = {}".format(n))
    plt.plot(X_grafic, abs(f(X_grafic) - Pn))
    plt.show()

for i in range(1, 5):
    PlotInterpolareMetNewtonDD(f, a, b, i, MetNewtonDD)
