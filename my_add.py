# Decorators
def coverter(func):
	def inner(x, y):
		a=type(x)
		try:
			return func(x, a(y)) 
		except Exception:
			print "Zeomega Error 123:convertion is not possible"
        
	return inner

@coverter
def my_add(x,y):
	if type(x) is dict and type(y) is dict:
		x.update(y)        
	else:
		print x+y


 

