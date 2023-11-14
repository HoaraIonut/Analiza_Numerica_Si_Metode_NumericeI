import numpy as np
import matplotlib.pyplot as plt

#EX 1 - 2
def f(x):
    return x**3 - 2 * x**2 - 5
def df(x):
    return 3 * x**2 - 4 * x

def NR(f, df, a, b, x0, ITMAX, TOL, SOL = 0, IT = 0):
    X = np.linspace(a, b)
    Y = f(X)
    plt.plot(X, Y, linewidth = 1)

    SOL = x0
    IT = 1

    print('La iteratia {:04} aproximarea numerica a solutiei este {:.10f}, eroarea absoluta este {:.4e}, eroarea reziduala este {:.4e}.'.format(IT, SOL, abs(SOL - 0), abs(f(SOL))))

    for i in range(2, ITMAX + 1):
        if abs(f(SOL)) < TOL:
            break

        SolAnterior = SOL
        SOL = SOL - f(SOL)/df(SOL)
        IT = IT + 1

        plt.scatter(SOL, f(SOL))

        print('La iteratia {:04} aproximarea numerica a solutiei este {:.10f}, eroarea absoluta este {:.4e}, eroarea reziduala este {:.4e}.'.format(IT, SOL, abs(SOL - SolAnterior), abs(f(SOL))))

    plt.show()
    return SOL

a = 1
b = 4
x0 = 4
ITMAX = 10
TOL = 10**(-10)

NR(f, df, a, b, x0, ITMAX, TOL)
