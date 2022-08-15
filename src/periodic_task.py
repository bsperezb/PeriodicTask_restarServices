from subprocess import call

def restartServices():
	with open('bash_scirpt.sh', 'rb') as file:
		script = file.read()	
	rc = call(script, shell=True)