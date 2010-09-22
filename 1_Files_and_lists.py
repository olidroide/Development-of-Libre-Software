f = open('/etc/passwd','r')
for i in f.readlines():
	lineSplit = i.split(":")
	user = lineSplit[0]
	path = lineSplit[len(lineSplit)-1]
	print user + " -> " + path
	
