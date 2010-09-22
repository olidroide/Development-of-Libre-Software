import sys

if len(sys.argv) > 1:
	userParam = sys.argv[1]
	
	f = open('/etc/passwd','r')
	userDict = {}
	for i in f.readlines():
		lineSplit = i.split(":")
		user = lineSplit[0]
		path = lineSplit[len(lineSplit)-1]
		userDict[user]=path
	
	if userParam in userDict:
		print userDict[userParam]
	else:
		print "Error: The user not has shell"
else:
	print "Warning: need parameters, put a name of user"
