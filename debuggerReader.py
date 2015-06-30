import os
import time, datetime

print (" ") * 1000

fileName = "debug.err"

os.environ['LINES'] = "80"
os.environ['COLUMNS'] = "50"

debugFileExists = False
for files in os.listdir(os.getcwd()):
	if files == fileName:
		debugFileExists = True

if not debugFileExists:
	print ("No debug file, quitting.")
	quit()

lastModified = os.path.getmtime(fileName)


while True:
	if not lastModified == os.path.getmtime(fileName):
		print (" ") * 1000
		with open(fileName, 'r') as log:
			print (log.read())
		lastModified = os.path.getmtime(fileName)
		print (datetime.datetime.now().time())
	time.sleep(1)
