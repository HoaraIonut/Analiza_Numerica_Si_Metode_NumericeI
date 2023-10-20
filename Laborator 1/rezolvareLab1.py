#rezolvare lab1

# 1 a

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**(6)-x-1

x = np.linspace(-2, 2)
y = f(x)

plt.plot(x, y, c='r', linewidth=1)
plt.plot(x, np.zeros(len(x)), c='b', linewidth=1)

#1 b
TOL = 10**(-5)

def metodaBisectie(a, b):
    x = (a + b) / 2
    while abs(f(x)) >= TOL:
        if f(a)*f(x) <= 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
    return x

plt.scatter(metodaBisectie(-1, 0), f(metodaBisectie(-1, 0)), 50, c = 'r')
plt.scatter(metodaBisectie(1, 2), f(metodaBisectie(1, 2)), 50, c = 'r')
plt.show()

# 2 a

import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.exp(-x/2)*(x**(2)+2*x-8)

x = np.linspace(-3, 3)
y = g(x)

plt.plot(x, y, c='g', linewidth=1)
plt.plot(x, np.zeros(len(x)), c='b', linewidth=1)


#b si c CRED CA ASA SE REZOLVA

TOL = 10**(-5)
xstar = 2

a = -3
b = 3

for i in range(10):
    x = (a + b) / 2
    if g(a) * g(x) <= 0:
        b = x
    else:
        a = x
    erra = abs(xstar - x)
    errr = erra / abs(xstar)
    plt.scatter(erra, g(erra), 25, c = 'r')
    plt.scatter(errr, g(errr), 25, c = 'y')
    if i == 9:
        print('x10 este egal cu: ', x)

plt.show()
#3

import numpy as np
import matplotlib.pyplot as plt
import copy


def h(x):
    return x * x - 3


def metodaBisectiei(f, a, b, ITMAX, TOL, OPT):
    n = 1
    x = (a + b) / 2
    ok = True
    while ok == True:
        if f(a) * f(x) <= 0:
            b = x
        else:
            a = x
        xant = copy.deepcopy(x)
        x = (a + b) / 2
        n = n + 1
        if n == ITMAX:
            ok = False
        if OPT == 1:
            if abs(b - a) <= TOL:
                ok = False
        if OPT == 2:
            if abs(x - xant) / abs(xant) <= TOL:
                ok = False
        if OPT == 3:
            if abs(f(x)) >= TOL:
                ok = False
    return x


AB = np.linspace(1, 2)

plt.plot(AB, h(AB), c='r', linewidth=1)
plt.plot(AB, np.zeros(len(AB)), c='b', linewidth=1)


val1 = metodaBisectiei(h, 1, 2, 10 ** (4), 10 ** (-8), 1)
plt.scatter(val1, h(val1), 50, c='r')
val2 = metodaBisectiei(h, 1, 2, 10 ** (4), 10 ** (-8), 2)
plt.scatter(val2, h(val2), 50, c='g')
val3 = metodaBisectiei(h, 1, 2, 10 ** (4), 10 ** (-8), 3)
plt.scatter(val3, h(val3), 50, c='y')

plt.show()

