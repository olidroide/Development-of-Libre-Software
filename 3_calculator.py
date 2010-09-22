# 3.Calculator
# Write a script to work like a calculator, implementing basic operations (+, -, *,
# /), for two operators. The script will receive the operators and the operation from the
# command line, see the examples below:
# ./calculator.py 30 + 25
# ./calculator.py 30 - 25
# ./calculator.py 30 \* 25
# ./calculator.py 30 / 25
# Note that ’*’ must be escaped, since it’s a special character for the shell. Every
# possible error should be handled showing appropriate error messages.

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
		print ("%s %s %s = %s")%(firstArg,operator,secondArg,resultado)
else:
	print "Warning: need parameters, for example 1 + 1"

