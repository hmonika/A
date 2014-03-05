''' A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 multiply 99.Find the largest palindrome made from the product of two 3 digit numbers. '''


import string
def ispalendrom(num):
	s = str(num)
	if s == s[::-1]:
		return True


def largest(bot,top):
	list1=[]
	print bot,top
	b = False
	for x in range(top,bot,-1):
		for y in range(top,bot,-1):
			#print 'x=',x," y = ",y
			b = ispalendrom(x*y)
			if b:
				list1.append(x*y)
			else:
				continue
		print 'x=',x,'y=',y
	print list1,'the largest palindrome made from the product of two 3-digit numbers.',max(list1)



