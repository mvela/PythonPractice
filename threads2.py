import threading
import time
import random

class Requests(threading.Thread):
	def __init__(self, name, moneyRequest):
		threading.Thread.__init__(self)

		self.name = name
		self.moneyRequest = moneyRequest

		Requests.money(self)
		time.sleep(random.randint(1,3))

	def money(self):
		print("%s requested %d money" % (self.name, self.moneyRequest))
		

sarah = Requests("Sarah", 24)
paul = Requests("Paul", 55)

sarah.start()
paul.start()

sarah.join()
paul.join()

print("Execution Complete")

