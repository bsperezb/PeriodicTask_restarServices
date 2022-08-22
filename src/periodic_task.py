from subprocess import call

def restartServices():
	with open('src/bash_scirpt.sh', 'rb') as file:
		script = file.read()	
	rc = call(script, shell=True)