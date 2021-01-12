import sympy
import matplotlib.pyplot as plt
import numpy as np
import time
#import math		 

def pi(n):
    result = 0
    for i in range(n):
        if sympy.isprime(i) == True:
            result += 1
    return result

# start counter
start_time = time.time()

x = np.arange(2,1001)
y = np.array([pi(i) for i in x])

for i, j in zip(x, y):
    print(i, "\t\t", j)

# record execution time
print (time.time() - start_time, "seconds")

def graph(formula, x_range):  
    x2 = np.array(x_range)  
    y2 = eval(formula)
    plt.plot(x2, y2, label="x/ln(x)")

graph('x/np.log(x)', x)

plt.scatter(x, y, label="π(X)", marker= ".", color="#a55", s=1)
plt.xlabel("X")
plt.ylabel("π(X)")
plt.legend() 
plt.title("Prime Counting Function")
plt.show() 