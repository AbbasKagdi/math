import matplotlib.pyplot as plt
import math
import numpy as np

def phi(n):
    result, start, inc = 1, 3, 2
    if n%2 == 1:
        start, inc = 2, 1
    for i in range(start, n, inc):
        if (math.gcd(i, n) == 1):
            result+=1
    return result 

x = np.arange(1,1001)
y = []
for i in x:
    y.append(phi(i))

for i, j in zip(x, y):
    print(i, "\t\t", j)

def graph(formula, x_range):  
    x2 = np.array(x_range)  
    y2 = eval(formula)
    plt.plot(x2, y2, label=formula)

graph('x-1', x)

#plt.plot(x, y, label="φ(X)", marker= ".", linewidth="0.005", color="#111")
plt.scatter(x, y, label="φ(X)", marker= ".", color="#111", s=1)
plt.xlabel("X")
plt.ylabel("φ(X)")
plt.legend() 
plt.title("Euler's Totient")
plt.show() 
