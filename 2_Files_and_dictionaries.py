# 2.Files and dictionaries
# Modify the script of the previous exercise to only show the shell used by a given
# user. The shell used by every username should be stored in a dictionary, and the user-
# name of which you want to get the shell will be provided as a command line argument.
# You should handle possible errors like invalid user names or even if no user name is
# provided.


import sys

if len(sys.argv) > 1:
	userParam = sys.argv[1]
	
	f = open('/etc/passwd','r')
	userDict = {}
	for i in f.readlines():
		lineSplit = i.split(":")
		user = lineSplit[0]
		path = lineSplit[-1]
		userDict[user]=path
	
	try:
		print userParam +" -> "+ userDict[userParam]
	except KeyError:
		print "User "+userParam+" Doesnt Exist. Try another"
	f.close()
else:
	print "Warning: need parameters, put a name of user"
