import sys
def wlc_count(file_name):
	file1 = open(file_name)        
	data = file1.read()
	
	
	print "Lines : ", len(data.split('\n'))-1
	print "Words : ", len(data.split())
	print "Characters : ", len(data)

if __name__ == '__main__':
       wlc_count(sys.argv[1])
 
