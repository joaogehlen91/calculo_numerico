import numpy as np

e = 2.71828182846
h = 0.01
a = 0.0
b = 1.0
n = int(((b-a)/h))
x = np.linspace(a, b, n+1)
linhas = n-1
colunas = n

matriz = np.zeros(shape=(n-1,n))

h2 = h**2
for i in range(0, n-1):
	ih = i*h
	beta = (2.0 *(i*(h**3))) - 4.0
	alfa = 2.0 - h
	lamp = 2.0 + h
	res = (-2.0 * h2 * e**ih)*((ih**2)+1.0)

	matriz[i-1][n-1] = res
	matriz[n-2][n-1] = res
	matriz[n-2][n-1] = matriz[n-2][n-1] - alfa*e
	for j in range(0, n-1):
		if i==j:
			matriz[i][j] = beta
		if (i+1)==j:
			matriz[i][j] = alfa
		if (i-1)==j:
			matriz[i][j] = lamp

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


print 'X', '\t', '    Y'
print x[0], '\t', 0.0
for i in range(1, n-1):
	print x[i], '\t', b[i]
print x[n], '\t', e