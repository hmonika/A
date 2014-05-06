def GCD(a,b):
	a = abs(a)
	b = abs(b)
	while b != 0:
		(a,b) = (b, a % b)
	return a

def LCM(a,b):
       return a * b / GCD(a , b)

def my_gcd(*args):
   return reduce(GCD, args)


def my_lcm(*args):
   return reduce(LCM, args)
       
       


