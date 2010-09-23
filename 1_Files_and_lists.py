# 1.Files and lists
# Write a Python script that reads the contents of the passwd file (/etc/passwd) and
# prints the shell used by every username. The output should be something like this:
# root -> /bin/bash
# daemon -> /bin/sh
# bin -> /bin/sh


f = open('/etc/passwd','r')
for i in f.readlines():
	lineSplit = i.split(":")
	user = lineSplit[0]
	path = lineSplit[len(lineSplit)-1]
	print user + " -> " + path
	
