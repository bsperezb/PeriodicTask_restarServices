import time
import schedule
from src.periodic_task import  restartServices

# Schedule Time
schedule.every(5).seconds.do(restartServices)

def main():
	'''Periodic task to restart TCC services'''
	while True:
		schedule.run_pending()

if __name__ == "__main__":
	main()