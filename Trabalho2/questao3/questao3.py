import numpy as np
from math import *

def fxy(x, y):
	return (y/x) - ((y/x)**2)

h = 0.25
a = 1.0
b = 3.0
n = int(((b-a)/h)+1)

x = list(np.linspace(a, b, n))
y = list(x[:])
yx = list(x[:])
k1 = x[:]
k2 = x[:]
k3 = x[:]
k4 = x[:]

for i in range(0, n-1):
	k1 = h*fxy(x[i],y[i])
	k2 = h*fxy((x[i]+h/2), y[i]+k1/2)
	k3 = h*fxy((x[i]+h/2), y[i]+k2/2)
	k4 = h*fxy(x[i]+h,y[i]+k3)

	y[i+1] = y[i]+((1.0/6.0)*(k1+ 2*k2 + 2*k3 + k4))

for i in xrange(n):
	yx[i] = x[i]/(1+log(x[i]))	

for i in xrange(n):
	print y[i]