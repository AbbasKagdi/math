import matplotlib.pyplot as plt
#import math
import numpy as np

x = np.arange(1,101)
y = np.random.randint(low=0, high=100, size=(100,))

plt.plot(x, y) 

plt.xlabel("X") 

plt.ylabel("Rand(X)") 

plt.title("Euler's Totient") 

plt.show() 
