# -*- coding:utf-8 -*-

import numpy as np
from math import *

h = 0.05
a = 1.0
b = 3.0
n = int(((b-a)/h)+1)

x = list(np.linspace(a, b, n))
y = x[:]
yx = x[:]

for i in range(1, n):
	y[i] = y[i-1]+( h*((y[i-1]/x[i-1]) - (((y[i-1]/x[i-1])**2))))

for i in xrange(n):
	yx[i] = x[i]/(1+log(x[i]))

print 'xi\t', "\ty'i", '\ty(xi)', '\tErro'
for i in xrange(n):
	print x[i], '\t', y[i], '\t', yx[i], '\t', y[i]-yx[i]