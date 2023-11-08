#EX1 a)
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
        y += C[i] * x **i
    return y

#EX1 b)

def f(x):
    return np.exp(2 * x)

a = -1
b = 1


def PlotInterpolare(f, a, b, n, metoda):
    X = np.linspace(a, b, n + 1)
    x_grafic = np.linspace(a, b, 50 * n + 1)
    Pn = []
    for x in x_grafic:
        Pn.append(MetNaiva(f, a, b, n, x))
    plt.plot(x_grafic, Pn, c='r', linestyle='dotted', linewidth=1)
    plt.plot(x_grafic, f(x_grafic), c='b', linewidth=1)
    plt.legend(['Functia aproximata', 'Functia f'])
    for el in X:
        plt.scatter(el, f(el), c='blue')
    plt.legend(['Functia aproximata', 'Functia f'])
    plt.show()

# for i in range(1, 5):
#     plt.title("Polinomul de interpolare Lagrange Pn(x) unde n = {sval}".format(sval=i))
#     PlotInterpolare(f, a, b, i, MetNaiva)


#EX1 c)
def ErrAbs(f, a, b, n, metoda):
    x_grafic = np.linspace(a, b, 50 * (n + 1))
    err = []
    for x in x_grafic:
        el = abs(f(x) - MetNaiva(f, a, b, n, x))
        # print("ErrAbs = ", f(x) - el)
        err.append(el)
    plt.plot(x_grafic, err)
    plt.show()

for i in range(1, 5):
    plt.title("ErrAbs(x)=|f(x)-Pn(x)| pt n = {val}".format(val=i))
    ErrAbs(f, -1, 1, i, MetNaiva)

#EX2 a)

