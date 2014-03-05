def multiply():
	sum=0
	for i in range(1,1000,1):
		if((i%3==0)or(i%5==0)):
			sum+=i
	print 'sum of all the multiples of 3 or 5 below 1000=',sum
			

if __name__=='__main__':
	multiply()
