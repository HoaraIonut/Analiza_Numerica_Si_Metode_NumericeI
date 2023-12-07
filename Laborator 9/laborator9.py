#Rezolvare Exc1
import numpy as np
import matplotlib.pyplot as plt

def FDM(f, df, x, m):
    aprox = []
    err = []
    if m == 1:
        for k in range(1, 10):
            h = 10 ** (-k)
            fprim = (f(x+h) - f(x))/h
            err.append(abs(df(x) - fprim))
            aprox.append(h)
    elif m == 2:
        for k in range(1, 10):
            h = 10 ** (-k)
            fprim = (f(x) - f(x-h))/h
            err.append(abs(df(x) - fprim))
            aprox.append(h)
    else:
        for k in range(1, 10):
            h = 10 ** (-k)
            fprim = (f(x+h) - f(x-h))/ (2*h)
            err.append(abs(df(x) - fprim))
            aprox.append(h**2)        
    plt.loglog(aprox, err)
    
def f(x):
    return np.exp(2*x)

def df(x):
    return 2 * np.exp(2*x)

FDM(f, df, 0, 1)

#Rezolvare Exc2

x=0
n=3
h=0.1
 
def Richardson(f, x, h, n):
    def phi(f, x, h):
        return (f(x + h) - f(x)) / h
    D = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        D[i, 0] = phi(f, x, h / (2 ** i))
    for j in range(1, n + 1):
        for i in range(j, n + 1):
            D[i, j] = D[i, j - 1] + (D[i, j - 1] - D[i - 1, j - 1]) / (4 ** j - 1)
 
    return D[n, n]
rez=Richardson(f,x,h,n)
print(rez)
    
