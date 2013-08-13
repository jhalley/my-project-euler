# PE58
# Assuming that a square spiral of length 1 is n=1
# 
# b|x|a
# -|-|-
# x|x|x
# -|-|-
# c|x|d
#
# The formula for calculating the value of the number at the corners of a square spiral for n is:
# d = (2n - 1)**2
# c = d - (2n-2)
# b = d - 2(2n-2)
# a = d - 3(2n-2)

MAXN=20000

# Sieve method
#prime_list = [1 if i%2 else 0 for i in range((MAXN*2 - 1)**2)] # Assuming that the solution is somewhere below n=MAXN
#prime_list[2] = 1
def gen_prime_list():
    i = 3 
    while i < len(prime_list):
        if not prime_list[i]: 
            i += 1
            continue

        j = i + i;
        while j < len(prime_list):
            prime_list[j] = 0
            j += i

        i += 1

import math
# It takes way too long to allocate the memory needed for prime_list to be efficient, so we're doing it by this method instead
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def pe58(max_n=MAXN):
    num_primes = 0

    for n in range(2, max_n+1):
        num_corner_numbers = (n-1)*4 + 1
        x = (2*n -2)

        d = (2*n -1)**2
        c = d - x
        b = d - 2*x
        a = d - 3*x

        #if prime_list[c]: num_primes += 1
        #if prime_list[b]: num_primes += 1
        #if prime_list[a]: num_primes += 1
        if is_prime(c): num_primes += 1
        if is_prime(b): num_primes += 1
        if is_prime(a): num_primes += 1

        print '%s / %s = %s'%(num_primes, num_corner_numbers, 1.0*num_primes/num_corner_numbers)

        if 1.0*num_primes/num_corner_numbers < 0.1:
            return (2*n - 1)

    return 'Answer is beyond n=%s!'%MAXN


    
#gen_prime_list()
print 'Answer is: %s'%pe58()
