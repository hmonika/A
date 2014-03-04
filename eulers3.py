def prime(number):
   # number=13195
    div=2
    ls=[]
    while(number!=0):
        if(number%div!=0):
            #print "div is", div
            div=div+1
        else:
            ls=[]
            number=number/div
            #print "number after division",number
            ls.append(div)
            #print ls
            #print "largest prime factor of the number=",div
            if(number==1):
                break
    print "largest prime factor of the number=",ls
