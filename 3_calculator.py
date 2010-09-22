import sys

if len(sys.argv) > 3:
	firstArg = sys.argv[1]
	operator = sys.argv[2]
	secondArg = sys.argv[3]
	resultado = None
	if operator == "+":
		resultado = float(firstArg) + float(secondArg)
	if operator == "-":
		resultado = float(firstArg) - float(secondArg)
	if operator == "*":
		resultado = float(firstArg) * float(secondArg)
	if operator == "/":
		if float(secondArg) == 0:
			print "Error: No divide by zero please, maybe in other universe..."
		else:
			resultado = float(firstArg) / float(secondArg)
	if resultado is None:
		print ""
	else:
		print ("El resultado de %s %s %s es %s")%(firstArg,operator,secondArg,resultado)
else:
	print "Warning: need parameters, for example 1 + 1"

