from math import *

run = True
xn = 1.3

while (run):
	
	fxn = ((exp(xn)) - (tan(xn)))

	dfxn = (exp(xn)) - (1/cos(xn**2))

	xn_1 = xn - (fxn/dfxn)
	modulo = xn_1 - xn

	if modulo > 0 and modulo < 0.001:
		run = False

	print fxn
	print dfxn
	print xn_1
	print modulo
	print "----"

	xn = round(xn_1, 10)

	
