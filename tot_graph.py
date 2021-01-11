import matplotlib.pyplot as plt
import math
import numpy as np

def phi(n):
    if n%2 == 1:
        return phi1(n)
    else:
        return phi2(n)

def phi1(n):
    # odd
    result = 1
    for i in range(2, n):
        if (math.gcd(i, n) == 1):
            result+=1
    return result 

def phi2(n):
    # even
    result = 1
    # search on odd numbers only
    for i in range(3, n, 2):
        if (math.gcd(i, n) == 1):
            result+=1
    return result 

x = np.arange(1,101)
y = []
for i in x:
    y.append(phi(i))

#for i, j in zip(x, y):
    #print(i, "\t\t", j)

def graph(formula, x_range):  
    x2 = np.array(x_range)  
    y2 = eval(formula)
    plt.plot(x2, y2, label=formula)

graph('x-1', x)

plt.plot(x, y, label="φ(X)", marker= ".", linewidth="0.005", color="#111")
plt.xlabel("X")
plt.ylabel("φ(X)")
plt.legend() 
plt.title("Euler's Totient")
plt.show() 
