#threading

import time
import threading
import random

def exThread(i):
	print("thread %d" % i)
	time.sleep(random.randint(1,10))
	print("thread %d has finished sleeping" % i, flush=True)

def main():
	for i in range(10):
		t = threading.Thread(target=exThread, args=(i,))
		t.start()


if __name__ == "__main__":
	main()
