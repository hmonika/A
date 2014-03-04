import string
def ispalendrom(num):
    return str(num)==str(num)[::-1]


def largest(bot,top):
    for x in range(top,bot,-1):
        for y in range(top,bot,-1):
            if ispalendrom(x*y):
                return x*y
