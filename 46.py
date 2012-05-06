#!/usr/bin/python
    
prime_list = [1 for i in range(1000001)]    # array of all primes below 1000000

def goldbach(x):
    for i in xrange(1,x):
        twice_square = 2*i**2
        if twice_square >= x: break
        if prime_list[x-twice_square]: 
            #print '%s = %s + 2 x %s ^ 2'%(x, x-twice_square, i) 
            return True
    return False

def pe46(x):
    # generate prime number list
    for i in range(2, len(prime_list)):
        if prime_list[i]:
            for j in range(i+i, len(prime_list), i): prime_list[j]=0

    for i in xrange(3, x, 2):
        if prime_list[i]: continue
        if not goldbach(i): 
            print i
            break

if __name__ == '__main__':
    pe46(1000000)
