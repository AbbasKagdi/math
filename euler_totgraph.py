import matplotlib.pyplot as plt
import numpy as np
import time

def phi(n): 
	result = n; 
	# Consider all prime factors of n and subtract their multiples from result 
	p = 2; 
	while(p * p <= n): 
		# Check if p is a prime factor. 
		if (n % p == 0): 
			# If yes, then update n and result 
			while (n % p == 0): 
				n = int(n / p); 
			result -= int(result / p); 
		p += 1; 

	# If n has a prime factor greater than sqrt(n) (There can be at-most one such prime factor) 
	if (n > 1): 
		result -= int(result / n); 
	return result; 

# start counter
start_time = time.time()

x = np.arange(1,101)
y = np.array([phi(i) for i in x])

for i, j in zip(x, y):
    print(i, "\t\t", j)

# record execution time
print (time.time() - start_time, "seconds")

def graph(formula, x_range):  
    x2 = np.array(x_range)  
    y2 = eval(formula)
    plt.plot(x2, y2, label=formula)

graph('x-1', x)

plt.scatter(x, y, label="φ(X)", marker= ".", color="#111", s=1)
plt.xlabel("X")
plt.ylabel("φ(X)")
plt.legend() 
plt.title("Euler's Totient")
plt.show() 