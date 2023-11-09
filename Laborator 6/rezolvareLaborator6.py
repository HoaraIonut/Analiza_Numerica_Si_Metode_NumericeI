import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(2*x)

def MetNeville(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Q = np.zeros((n+1, n+1))
    for i in range(n+1):
        Q[i][0] = f(X[i])
    for i in range(1, n+1):
        for j in range(1, i+1):
            Q[i][j] = (Q[i][j-1]*(x - X[i-j]) - Q[i-1][j-1]*(x-X[i]))/(X[i]-X[i-j])
    #for i in range(n+1):
        #for j in range(n+1):
            #print(Q[i][j])
    return Q[n][n]

def PlotInterpolare(f, a, b, n, metoda):
    X = np.linspace(a, b, n + 1)
    x_grafic = np.linspace(a, b, 50 * n + 1)
    Pn = []
    for x in x_grafic:
        Pn.append(MetNeville(f, a, b, n, x))
    plt.plot(x_grafic, Pn, c='r', linestyle='dotted', linewidth=1)
    plt.plot(x_grafic, f(x_grafic), c='b', linewidth=1)
    plt.legend(['Functia aproximata', 'Functia f'])
    for el in X:
        plt.scatter(el, f(el), c='blue')
    plt.legend(['Functia aproximata', 'Functia f'])
    plt.show()

a = -1
b = 1

for n in range(5):
    plt.title('n = {val}'.format(val = n))
    PlotInterpolare(f, a, b, n, PlotInterpolare)

def ErrAbs(f, a, b, n, metoda):
    x_grafic = np.linspace(a, b, 50 * (n + 1))
    err = []
    for x in x_grafic:
        el = abs(f(x) - MetNeville(f, a, b, n, x))
        # print("ErrAbs = ", f(x) - el)
        err.append(el)
    plt.plot(x_grafic, err)
    plt.show()

for i in range(1, 5):
    plt.title("ErrAbs(x)=|f(x)-Pn(x)| pt n = {val}".format(val=i))
    ErrAbs(f, -1, 1, i, MetNeville)
