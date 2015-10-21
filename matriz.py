import random

def cria_matriz(lin,col):
	A=[]
 	for i in range(lin):
  		linha=[]
  		for j in range(col):
   			linha = linha + [random.randint(1,10)]
  	A= A + [linha]
	return A

def mostra_matriz(matriz):
 	print 'Matriz'
 		for i in range(len(matriz)):
  			for j in range(len(matriz[0])):
   			print matriz[i][j],'\t',
  		print
 	print '_' * 10