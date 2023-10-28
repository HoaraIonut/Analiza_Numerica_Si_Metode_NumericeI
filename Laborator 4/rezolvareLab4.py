#ex1

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 3 - 4 * x ** 2 + 5 * x - 2

def df(x):
    return 3 * x ** 2 - 8 * x + 5

def d2f(x):
    return 6 * x - 8

x = np.linspace(0, 1.75)
y = f(x)

plt.plot(x, y, c = 'b', linewidth=1)

x = np.linspace(0, 1.75)
y = df(x)

plt.plot(x, y, c = 'r', linewidth=1)

plt.title('Functia f si prima derivata a sa')
plt.legend(['functia f', 'prima derivata a functiei f'])
plt.show()

################################

def NewtonRaphsonModificata1(m, f, df, x0, ITMAX, TOL):
    for n in range(ITMAX):
        x1 = x0
        x0 = x0 - m * (f(x0)/df(x0))
        print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e} | errabs = {:.2e}".format(n, x0, abs(f(x0)), abs(x1 - x0)))
        plt.scatter(x0, f(x0))
        if(abs(f(x0)) < TOL):
            break



print("\n TABEL PENTRU METODA NR MODIFICATA 1")

x = np.linspace(0, 1.75)
y = f(x)

plt.plot(x, y, c = 'r', linewidth=1)

x = np.linspace(0, 1.75)
y = df(x)

plt.plot(x, y, c = 'b', linewidth=1)

NewtonRaphsonModificata1(2, f, df, 0, 20, 10 ** (-10))
plt.legend(['functia f', 'prima derivata a functiei f'])
plt.title("METODA NR MODIFICATA 1")
plt.show()

############################

def NewtonRapshonModificiata2(f, df, x0, ITMAX, TOL):
    for n in range(ITMAX):
        x1 = x0
        x0 = x0 - (f(x0)/df(x0))/((df(x0) ** 2 - f(x0) * d2f(x0))/(df(x0) ** 2))
        print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e} | errabs = {:.2e}".format(n, x0, abs(f(x0)), abs(x1 - x0)))
        plt.scatter(x0, f(x0))
        if(abs(f(x0)) < TOL):
            break


x = np.linspace(0, 1.75)
y = f(x)

plt.plot(x, y, c = 'b', linewidth=1)

x = np.linspace(0, 1.75)
y = df(x)

plt.plot(x, y, c = 'r', linewidth=1)

x = np.linspace(0, 1.75)
y = d2f(x)

plt.plot(x, y, c = 'g', linewidth=1)


print("\n TABEL PENTRU METODA NR MODIFICATA 2")
NewtonRapshonModificiata2(f, df, 0, 20, 10 ** (-10))
plt.title("METODA NR MODIFICATA 2")
plt.legend(['functia f', 'prima derivata a functiei f', 'a doua derivata a functiei f'])
plt.show()

###############################


def NewRap(f, df, x0, ITMAX, TOL):
    for n in range(ITMAX):
        x1 = x0
        x0 = x0 - f(x0) / df(x0)
        print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e} | errabs = {:.2e}".format(n, x0, abs(f(x0)), abs(x1-x0)))
        plt.scatter(x0, f(x0))
        if (abs(f(x0)) < TOL):
            break

x = np.linspace(0, 1.75)
y = f(x)

plt.plot(x, y, c = 'b', linewidth=1)

x = np.linspace(0, 1.75)
y = df(x)

plt.plot(x, y, c = 'r', linewidth=1)

print("\n TABEL PENTRU METODA NR")
NewRap(f, df, 0, 20, 10 ** (-10))

plt.title("METODA NR")
plt.legend(['functia f', 'prima derivata a functiei f'])
plt.show()


#EX3


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 3 - 4 * x ** 2 + 5 * x - 2

def df(x):
    return 3 * x ** 2 - 8 * x + 5

x = np.linspace(0, 1.75)
y = f(x)

plt.plot(x, y, c='r')

x = np.linspace(0, 1.75)
y = df(x)

plt.plot(x, y, c='b')


def phi(x):
    return x-(f(x)/df(x))

def Aitken(f, phi, x0, ITMAX, TOL):
    aproximari = []
    x1 = phi(x0)
    x2 = phi(x1)
    for n in range(ITMAX):
        xc = (x2 * x0 - x1 ** 2) / (x2 - 2 * x1 + x0)
        aproximari.append(xc)
        x2, x1, x0 = phi(x2), x2, x1
        plt.scatter(x0, f(x0))
        print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e} | errabs = {:.2e}".format(n, x0, abs(f(x0)), abs(x1 - x0)))
        if abs(f(xc)) < TOL:
            break
    return aproximari, len(aproximari)

print('\n')

Aitken(f, phi, 0, 20, 10 ** (-10))

plt.title("METODA LUI AITKEN")
plt.legend(['functia f', 'prima derivata a lui f'])
plt.show()
#
# ###############################################
#
#
#
def Steffensen(f, phi, x0, ITMAX, TOL):
    aproximari = []
    x1 = phi(x0)
    x2 = phi(x1)
    for n in range(ITMAX):
        x0 = (x2*x0 - x1 ** 2)/(x2 - 2 * x1 + x0)
        aproximari.append(x0)
        plt.scatter(x0, f(x0))
        print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e} | errabs = {:.2e}".format(n, x0, abs(f(x0)), abs(x1 - x0)))
        x1 = phi(x0)
        x2 = phi(x1)
        if abs(f(x0) < TOL):
            break
        return aproximari, len(aproximari)

x = np.linspace(0, 1.75)
y = f(x)

plt.plot(x, y, c='r')

x = np.linspace(0, 1.75)
y = df(x)

plt.plot(x, y, c='b')
print('\n')
Steffensen(f, phi, 0, 20, 10 ** (-10))


plt.title("METODA LUI STEFFENSEN")
plt.legend(['functia f', 'prima derivata a lui f'])
plt.show()
