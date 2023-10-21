#ex1

import numpy as np
import matplotlib.pyplot as plt

legenda = []

#a
def f(x):
    return x + np.exp(-1 * (x ** 2)) * np.cos(x)

x = np.linspace(-1, 1)
y = f(x)

plt.plot(x, y, c='r', linewidth='1')
legenda.append('Functia f')

plt.legend(legenda)
plt.show()

#b
def secantaf(f, x0, x1, N):
    #plt.title("Erorile relative pentru metoda secantei")
    err = []
    err.append(abs((x0-x1)/x0))
    for n in range(2, N - 1):
        x1, x0 = x1 - f(x1) * ((x1 - x0)/(f(x1) - f(x0))), x1
        err.append(abs((x0 - x1) / x0))
        print('La iteratia {}, x = {:.10f}, err = {:.2e}'.format(n, x0, err[-1]))
    plt.plot(list(range(1, N - 1)), err, c='b')
    return err

def falsi(f, x0, x1, N):
    #plt.title("Erorile relative pentru metoda falsi")
    err = []
    err.append(abs((x0 - x1)/ x0))
    x2 = x1 - f(x1) * ((x1 - x0)/(f(x1)-f(x0)))
    err.append(abs((x1 - x2) / x1))
    for n in range(3, N-1):
        if f(x1) * f(x0) <= 0:
            x2, x1, x0 = x2 - f(x2) * ((x2 - x1)/(f(x2) - f(x1))), x2, x1
        else:
            x2, x1, x0 = x2 - f(x2) * ((x2 - x0)/(f(x2) - f(x0))), x2, x0
        err.append(abs((x1-x2)/x1))
        print('La iteratia {}, x = {:.10f}, err = {:.2e}'.format(n, x0, err[-1]))

    plt.plot(list(range(1, N-1)), err, c='g')
    return err

secantaf(f, -1, 1, 10)
falsi(f, -1, 1, 10)

plt.legend(['Erorile relative pt met. Secantei', 'Erorile relative pt met. Falsi'])
plt.show()

secantaf(f, 1, -1, 10)
falsi(f, 1, -1, 10)

plt.legend(['Erorile relative pt met. Secantei', 'Erorile relative pt met. Falsi'])
plt.show()

#ex2
import numpy as np
import matplotlib.pyplot as plt

#a

legenda = []

def secantaf(f , x0, x1, TOL):
    n = 1
    while abs(f(x1)) > TOL:
        x1, x0 = x1 - f(x1) * ((x1 - x0)/(f(x1)-f(x0))), x1
        plt.scatter(x1, f(x1))
        legenda.append('aproximare {}'.format(n))
        print("La iteratia {} radacina xn are valoarea {:.10f}".format(n, x1))
        n = n + 1
    print('\n')
    return x1

def falsi(f, x0, x1, TOL):

    n = 1
    x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
    while abs(f(x2) > TOL):
        if f(x1) * f(x0) <= 0:
           x2, x1, x0 = x2 - f(x2) * ((x2 - x1)/(f(x2) - f(x1))), x2, x1
        else:
           x2, x1, x0 = x2 - f(x2) * ((x2 - x0)/(f(x2) - f(x0))), x2, x0
        plt.scatter(x2, f(x2))
        legenda.append('aproximare {}'.format(n))
        print("La iteratia {} radacina xn are valoarea {:.10f}".format(n, x2))
        n = n + 1
    print('\n')
    return x2
#b
def f(x):
    return np.cos(x) - x

x = np.linspace(0, np.pi / 2)
y = f(x)
plt.plot(x, y, c='r', linewidth="1")
legenda.append('Functia f')
plt.plot(x, np.zeros(len(x)), c='b', linewidth='1')
legenda.append('Axa OX')

secantaf(f, 0, np.pi / 2, 10 ** (-8))
plt.legend(legenda)
plt.title('Aproximarile solutiei folosind metoda secantei cand x0 = 0 x1 = pi/2')
plt.show()

legenda = []


x = np.linspace(0, np.pi / 2)
y = f(x)
plt.plot(x, y, c='r', linewidth="1")
legenda.append('Functia f')
plt.plot(x, np.zeros(len(x)), c='b', linewidth='1')
legenda.append('Axa OX')

falsi(f, 0, np.pi / 2, 10 ** (-8))
plt.legend(legenda)

plt.title('Aproximarile solutiei folosind metoda falsi cand x0 = 0 x1 = pi/2')
plt.show()

legenda=[]

x = np.linspace(0, np.pi / 2)
y = f(x)
plt.plot(x, y, c='r', linewidth="1")
legenda.append('Functia f')
plt.plot(x, np.zeros(len(x)), c='b', linewidth='1')
legenda.append('Axa OX')

secantaf(f, np.pi / 2, 0, 10 ** (-8))
plt.legend(legenda)
plt.title('Aproximarile solutiei folosind metoda secantei cand x0 = pi/2 x1 = 0')
plt.show()

legenda = []


x = np.linspace(0, np.pi / 2)
y = f(x)
plt.plot(x, y, c='r', linewidth="1")
legenda.append('Functia f')
plt.plot(x, np.zeros(len(x)), c='b', linewidth='1')
legenda.append('Axa OX')

falsi(f, np.pi / 2, 0, 10 ** (-8))
plt.legend(legenda)

plt.title('Aproximarile solutiei folosind metoda falsi cand x0 = pi/2 x1 = 0')
plt.show()
