# #ex1
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# def f(x):
#     return x ** 3 - 4 * x ** 2 + 5 * x - 2
#
# def df(x):
#     return 3 * x ** 2 - 8 * x + 5
#
# def d2f(x):
#     return 6 * x - 8
#
# x = np.linspace(0, 1.75)
# y = f(x)
#
# plt.plot(x, y, c = 'b', linewidth=1)
# x = np.linspace(0, 1.75)
# y = df(x)
#
# plt.plot(x, y, c = 'b', linewidth=1)
#
# # plt.show()
#
#
# def NewtonRaphsonModificata1(m, f, df, x0, ITMAX, TOL):
#     for n in range(ITMAX):
#         x0 = x0 - m * (f(x0)/df(x0))
#         print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e}".format(n, x0, abs(f(x0))))
#         plt.scatter(x0, f(x0))
#         if(abs(f(x0)) < TOL):
#             break
#
# def NewtonRapshonModificiata2(f, df, x0, ITMAX, TOL):
#     for n in range(ITMAX):
#         x0 = x0 - (f(x0)/df(x0))/((df(x0) ** 2 - f(x0) * d2f(x0))/(df(x0) ** 2))
#         print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e}".format(n, x0, abs(f(x0))))
#         plt.scatter(x0, f(x0))
#         if(abs(f(x0)) < TOL):
#             break
#
# def NewRap(f, df, x0, ITMAX, TOL):
#     for n in range(ITMAX):
#         x0 = x0 - f(x0) / df(x0)
#         print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e}".format(n, x0, abs(f(x0))))
#         plt.scatter(x0, f(x0))
#         if (abs(f(x0)) < TOL):
#             break
#
#
# print("\n TABEL PENTRU METODA NR MODIFICATA 1")
# NewtonRaphsonModificata1(2, f, df, 0, 20, 10 ** (-10))
# plt.title("METODA NR MODIFICATA 1")
# plt.show()
#
# x = np.linspace(0, 1.75)
# y = f(x)
#
# plt.plot(x, y, c = 'b', linewidth=1)
# x = np.linspace(0, 1.75)
# y = df(x)
#
# plt.plot(x, y, c = 'b', linewidth=1)
#
# print("\n TABEL PENTRU METODA NR")
# NewRap(f, df, 0, 20, 10 ** (-10))
#
# plt.title("METODA NR")
# plt.show()
#
# x = np.linspace(0, 1.75)
# y = f(x)
#
# plt.plot(x, y, c = 'b', linewidth=1)
# x = np.linspace(0, 1.75)
# y = df(x)
#
# plt.plot(x, y, c = 'b', linewidth=1)
#
# x = np.linspace(0, 1.75)
# y = d2f(x)
#
# plt.plot(x, y, c = 'b', linewidth=1)
#
#
# print("\n TABEL PENTRU METODA NR MODIFICATA 2")
# NewtonRapshonModificiata2(f, df, 0, 20, 10 ** (-10))
# plt.title("METODA NR MODIFICATA 2")
# plt.show()
#
import numpy as np
import matplotlib as plt

def f(x):
    return x ** 3 - 4 * x ** 2 + 5 * x - 2

def df(x):
    return 3 * x ** 2 - 8 * x + 5

x = np.linspace(0, 1.75)
y = f(x)

plt.plot(x, y, c='r')

x = np.linspace(0, 1.75)
y = df(x)

plt.plot(x, y, c='r')
def phi(x):
    return x-(f(x)/df(x))

#EX2

def Aitken(f, phi, x0, ITMAX, TOL):
    aproximari = []
    x1 = phi(x0)
    x2 = phi(x1)
    for n in range(ITMAX):
        xc = (x2 * x0 - x1 ** 2) / (x2 - 2 * x1 + x0)
        aproximari.append(xc)
        x2, x1, x0 = phi(x2), x2, x1
        print("n={:d} | xn = {:.6f} | |f(xn)|={:.2e}".format(n, x0, abs(f(x0))))
        if abs(f(xc)) < TOL:
            break
    return aproximari, len(aproximari)

Aitken(f, phi, 0, 20, 10 ** (-10))
