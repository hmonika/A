''' 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
   '''


def smallestNum():
	i=2520
	found=False
	while(found==False):
		i+=2520
		division=True
		for j in range(11,21,1):
			if(i%j!=0):
				division=False
				break
			else:
				continue
		if(division):
			found=True
	print 'the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?=',i


if __name__=='__main__':
	smallestNum()
