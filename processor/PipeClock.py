import time

def PipeClock():
	st=time.time()
	while True:
		if ((time.time()-st)*1000>100):
			break
	print("Next?")
	#if((int)(raw_input())==0):
		#exit(0)



	
