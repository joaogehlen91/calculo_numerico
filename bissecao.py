import os
os.system("clear")

an = 2
bn = 3
count = 0
fxn = 0.01	
run = True

while (run):
	xn = (an + bn) / 2.00

	fxn = xn**3 - 10
	

	fa = an**3 - 10

	if (fxn * fa) < 0 :
		print "%f  -> troca o b" %(fxn)
		bn = xn
	else :
		print "%f  -> troca o a" %(fxn) 
		an = xn

	if fxn > 0 and fxn < 0.01:
		run = False

print "Fim"
print "A raiz e "+ str(xn)