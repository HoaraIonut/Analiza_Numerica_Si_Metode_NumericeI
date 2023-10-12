#ex1

# import numpy as np
# import matplotlib.pyplot as plt

# def phi1(x):
#     return (-1) * (x **(3)) + (-4) * x * x + x + 10

# def phi1der(x):
#     return (-3) * x * x + (-8) * x + 1 

# def f(x):
#     return x**(3) +4 * x**(2) - 10

# def phi4(x):
#     return (10 / (x + 4)) ** (.5)

# def metPctFix(func, x0, N):
#     x = x0
#     for i in range (N):
#         x = func(x)
#         #plt.scatter(x, f(x), c='b')
#         print(x, f(x))
#     return x
    

# x1 = np.linspace(1, 2)
# y1 = f(x1)

# plt.plot(x1, y1, c='r', linewidth=1)

# plt.show()

# x2 = np.linspace(1, 2)
# y2 = phi1(x2)

# plt.plot(x2, y2, c='b', linewidth=1)
# plt.show()

# x3 = np.linspace(1, 2)
# y3 = phi1der(x3)

# plt.plot(x3, y3, c='y', linewidth=1)
# plt.show()

# x4 = np.linspace(1, 2)
# y4 = phi4(x4)

# plt.plot(x4, y4, c='r', linewidth=1)
# metPctFix(phi4, 1, 20)
#plt.show()

#ex2
# import numpy as np
# import matplotlib.pyplot as plt 

# def f(x):
#     return x + np.exp(-1 * (x ** 2)) * np.cos(x)

# def fprim(x):
#     return 1 - np.exp(-1 * (x **2))*(2*x*np.cos(x)+np.sin(x))

# def NewRap(func, funcprim, x0, N):
#     x = x0
#     for i in range(N):
#         x = x - func(x) / funcprim(x)
#         print(x)
#     return x
    
    
# x = np.linspace(-1, 1)
# y = f(x)

# plt.plot(x, y, c='r', linewidth=1)
# plt.plot(x, np.zeros(len(x)), c='b', linewidth=1)

# x = NewRap(f, fprim, 0, 10)
# plt.scatter(x, f(x), c = 'g')

#ex3

# import numpy as np
# import matplotlib.pyplot as plt 

# def f(x):
#     return np.cos(x) - x

# def fprim(x):
#     return (-1) * np.sin(x) - 1


# x = np.linspace(0, np.pi / 2)
# y = f(x)

# plt.plot(x, y, c='r', linewidth=1)
# plt.plot(x, np.zeros(len(x)), c='b', linewidth=1)

# def NewRap(func, funcprim, x0, TOL):
#     x = x0
#     while abs(func(x)) >= TOL:
#         x = x - func(x) / funcprim(x)
#         plt.scatter(x, f(x), c='y')
#     return x

# x = NewRap(f, fprim, np.pi / 4, 10 ** (-5))


