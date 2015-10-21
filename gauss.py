linhas = 6
colunas = 7
soma = 0.0

matriz = [
    [24, 0.0, 81.25, 0.0, 474.296875, 0.0, 7.0897522776444672],
    [0.0, 81.25, 0.0, 474.296875, 0.0, 3289.0380859375, 0.0],
    [81.25, 0.0, 474.296875, 0.0, 3289.0380859375, 0.0, 3.5442178420851795],
    [0.0, 474.296875, 0.0, 3289.0380859375, 0.0, 24782.467956542969, 0.0],
    [474.296875, 0.0, 3289.0380859375, 0.0, 24782.467956542969, 0.0, 5.3097759958530517],
    [0.0, 3289.0380859375, 0.0, 24782.467956542969, 0.0, 196016.56103134155, 0.0],
]

"""
print "Matriz original: "
for i in matriz:
	print "   ",
	print i
"""


def zera(l, ll, x, y):
	m = l[x]/ll[y]
	for x in range(0, len(l)):
		l[x] = l[x] - (m*ll[x])


for j in range(0, colunas-2):
	for i in range(j, linhas):
		if i != j:			
			zera(matriz[i], matriz[j], j, j)


print "Matriz zerada: "
for i in matriz:
	print "   ",
	print i



b = []
for i in xrange(colunas-1):
	b.append(matriz[i][colunas-1])

#print b
"""
x6 = b[linhas-1]/(matriz[linhas-1][colunas-2])
x5 = b[linhas-2]/(matriz[linhas-2][colunas-3]+x6*matriz[linhas-2][colunas-2])
x4 = b[linhas-3]/(matriz[linhas-3][colunas-4]+x6*matriz[linhas-3][colunas-2]+x5*matriz[linhas-3][colunas-3])
x3 = b[linhas-4]/(matriz[linhas-4][colunas-5]+x6*matriz[linhas-4][colunas-2]+x5*matriz[linhas-4][colunas-3]+x4*matriz[linhas-4][colunas-4])
x2 = b[linhas-5]/(matriz[linhas-5][colunas-6]+x6*matriz[linhas-5][colunas-2]+x5*matriz[linhas-5][colunas-3]+x4*matriz[linhas-5][colunas-4]+x3*matriz[linhas-5][colunas-5])
x1 = b[linhas-6]/(matriz[linhas-6][colunas-7]+x6*matriz[linhas-6][colunas-2]+x5*matriz[linhas-6][colunas-3]+x4*matriz[linhas-6][colunas-4]+x3*matriz[linhas-6][colunas-5]+x2*matriz[linhas-6][colunas-6])

print 'x6 =', x6
print 'x5 =', x5
print 'x4 =', x4
print 'x3 =', x3
print 'x2 =', x2
print 'x1 =', x1

"""



x5 =  matriz[5][6] / matriz[5][5]
x4 = (matriz[4][6] - matriz[4][5]) / matriz[4][4]
x3 = (matriz[3][6] - (matriz[3][5] * x5)) / matriz[3][3]
x2 = (matriz[2][6] - (matriz[2][4] * x4)) / matriz[2][2]
x1 = (matriz[1][6] - (matriz[1][5] * x5) - (matriz[1][3] * x3)) / matriz[1][1]
x0 = (matriz[0][6] - (matriz[0][4] * x4) - (matriz[0][2] * x2)) / matriz[0][0]

print 'x5 =', x5
print 'x4 =', x4
print 'x3 =', x3
print 'x2 =', x2
print 'x1 =', x1
print 'x0 =', x0