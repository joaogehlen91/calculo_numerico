# -*- coding:utf-8 -*-

import numpy as np
from math import *

h = 0.125
a = -3.0
b = 3.0
n = int(((b-a)/h)+1)

x = np.linspace(-3.0, 3.0, n)

y = 2.71828182846**-(x**2)

for i in range(1, n-1):
	y[i] = 2*y[i]

AT = (h/2)*sum(y)
AT = AT*(2/sqrt(pi))
print AT