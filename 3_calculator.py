# 3.Calculator
# Write a script to work like a calculator, implementing basic operations (+, -, *,
# /), for two operators. The script will receive the operators and the operation from the
# command line, see the examples below:
# ./calculator.py 30 + 25
# ./calculator.py 30 - 25
# ./calculator.py 30 \* 25
# ./calculator.py 30 / 25

import sys

firstArg = 0
secondArg = 0

if len(sys.argv) > 3:

# This Try from Antonio Navarro de Mingo exercice code. Thanks
	try:
		firstArg = float(sys.argv[1])
		secondArg = float(sys.argv[3])
	except ValueError:
		print "Error: No input numeric values"
		sys.exit(-1)
# 
	operator = sys.argv[2]
	result = None
	if operator == "+":
		result = firstArg + secondArg
	elif operator == "-":
		result = firstArg - secondArg
	elif operator == "*":
		result = firstArg * secondArg
	elif operator == "/":
		if secondArg == 0:
			print "Error: No divide by zero please, maybe in other universe..."
		else:
			result = firstArg / secondArg
	if result is None:
		print "No Result"
	else:
		print ("%s %s %s = %s")%(firstArg,operator,secondArg,result)
else:
	print "Warning: need parameters, for example 1 + 1"

