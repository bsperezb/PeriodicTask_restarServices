from time import time
import schedule

def job():
	print('hellow World')

def main():
	'''Periodic task to restart TCC services'''
	while True:
		schedule.every(2).seconds.do(job)


if __name__ == "__main__":
	print("run")
	main()