import numpy as np
from math import *

linhas = 6
colunas = 7
soma = 0.0

h = 0.125
a = -5.0
b = 5.0
n = int(((b-a)/h)+1)

x = np.linspace(a, b, n)
x2 =  x**2
x3 =  x**3
x4 =  x**4
x5 =  x**5
x6 =  x**6
x7 =  x**7
x8 =  x**8
x9 =  x**9
x10 = x**10

somx = sum(x)
somx2 = sum(x2)
somx3 = sum(x3)
somx4 = sum(x4)
somx5 = sum(x5)
somx6 = sum(x6)
somx7 = sum(x7)
somx8 = sum(x8)
somx9 = sum(x9)
somx10 = sum(x10)

y = 2.71828182846**(-(x**2))

y2 = y**2
somy2 = sum(y2)
xy = x*y

x2y = x2*y
x3y = x3*y
x4y = x4*y
x5y = x5*y

somy = sum(y)
somxy = sum(xy)
somx2y = sum(x2y)
somx3y = sum(x3y)
somx4y = sum(x4y)
somx5y = sum(x5y)

matriz = [
[    n-1,         somx,           somx2,           somx3,      somx4,        somx5,    somy],
[   somx,        somx2,           somx3,           somx4,      somx5,        somx6,   somxy],
[  somx2,        somx3,           somx4,           somx5,      somx6,        somx7,  somx2y],
[  somx3,        somx4,           somx5, 	       somx6,      somx7,        somx8,  somx3y],
[  somx4,        somx5,           somx6,           somx7,      somx8,        somx9,  somx4y],
[  somx5,        somx6,           somx7,           somx8,      somx9,       somx10,  somx5y],
]

# Gauss
def zera(l, ll, x, y):
	m = l[x]/ll[y]
	for x in range(0, len(l)):
		l[x] = l[x] - (m*ll[x])

for j in range(0, colunas-2):
	for i in range(j, linhas):
		if i != j:			
			zera(matriz[i], matriz[j], j, j)

b = []
for i in range(linhas-1, -1, -1):
	b.append(matriz[i][colunas-1])

b[linhas-1] = matriz[linhas-1][colunas-1] / matriz[linhas-1][colunas-2]
soma = 0.0
for i in range(linhas-2, -1, -1):
	#print i
	for j in range(colunas-2, i, -1):
		#print j
		soma = soma + matriz[i][j]*b[j]

	soma = matriz[i][colunas-1] - soma
	b[i] = soma / matriz[i][i]
	soma = 0.0

for i in range(0, linhas):
	print b[i]

print ''
print 'y =',round(b[0],12), '+', round(b[1], 12),'x','+', round(b[2], 12),'x^2','+', round(b[3], 12),'x^3','+', round(b[4], 12),'x^4','+', round(b[5], 12),'x^5'

soma = 0.0
ybar = []
for i in range(0,len(x)):
    ybar.append((b[0] + (b[1] * x[i]) + (b[2] * (x[i] ** 2)) + (b[3] * (x[i] ** 3)) + (b[4] * (x[i] ** 4)) + (b[5] * (x[i] ** 5))))
    soma = soma + ((y[i] - (b[0] + b[1] * x[i] + (b[2] * (x[i] ** 2)) + (b[3] * (x[i] ** 3)) + (b[4] * (x[i] ** 4)) + (b[5] * (x[i] ** 5)))) ** 2)

baixo = somy2 - (somy2 / n)
r2 = 1 - (soma / baixo)

print ''
print 'r2 =',r2