# Using the sieve method
def get_primes_up_to_n(n):
    p_temp = {i:1 for i in xrange(1, int(n) + 1)}

    for i in xrange(2, int(n) + 1):
        if p_temp[i]:
            for j in xrange(i + i, int(n) + 1, i):
                p_temp[j] = 0

    return {i:1 for i in p_temp.keys() if p_temp[i]}

def prime_factorize(primes, n):
    tmp = n
    factors = []
    while tmp != 1:
        if tmp in primes:
            factors.append(tmp)
            tmp = 1

        for i in primes:
            if not tmp%i:
                tmp = tmp/i
                factors.append(i)
                break

    return factors

def main(n):
    # Get the list of prime numbers up to sqrt(n)
    primes = get_primes_up_to_n(n)
    sorted_primes = sorted(primes.keys())[1:]   # We remove 1
    print 'finished calculating primes'

    phi = {i:1 for i in xrange(2, n + 1)}
    print 'finished preloading phi'
    for i in phi:
        if not i%1000:
            print i
        # If the number is prime, all numbers below it are automatically relatively prime to it
        if i in primes:
            phi[i] = i - 1
        else:   # We need to prime factorize i, and test all numbers up to i-1 against the prime factors i
            prime_factors = set(prime_factorize(sorted_primes, i))
            for j in xrange(2, i):
                if j in primes:
                    if j not in prime_factors:
                        phi[i] += 1
                else:
                    if sum([1 if not j%p else 0 for p in prime_factors]) == 0:
                        phi[i] += 1

    # Get max n/phi[n]
    max_val = 0
    max_n = 0
    for n in phi.keys():
        temp = n/phi[n]
        if n/phi[n] > max_val:
            max_val = temp
            max_n = n

    print max_n

def main2(n):
    # Get the unique prime factors of all numbers to n
    f = {i:set() for i in xrange(2, n+1)}
    for i in xrange(2, n+1):
        if not i%1000:
            print 'Getting prime factors: %s'%i
        # Determine if number is prime
        if not f[i]:
            f[i].add(i) 
            for j in xrange(i+i, n+1, i):
                f[j].add(i)

    # Check if there are any common factors
    phi_n = {i:i-1 for i in xrange(2, n+1)}
    for i in xrange(3, n+1):
        if not i%1000:
            print 'Checking relative primeness: %s'%i
        for j in xrange(2, i):
            if f[j].intersection(f[i]): # Not relatively prime to each other
                phi_n[i] -= 1

    # get max
    max_n = 2
    max_val = 2.0
    for i in xrange(3, n+1):
        tmp = i*1.0/phi_n[i]
        if tmp > max_val:
            max_val = tmp
            max_n= i

    #print f
    #print phi_n
    print max_val
    print max_n

def main3(n):
    # Get the unique prime factors of all numbers to n
    f = {i:set() for i in xrange(2, n+1)}
    for i in xrange(2, n+1):
        if not i%1000:
            print 'Getting prime factors: %s'%i
        # Determine if number is prime
        if not f[i]:
            f[i].add(i) 
            for j in xrange(i+i, n+1, i):
                f[j].add(i)

    # Check if there are any common factors
    phi_n = {i:[i-1, 0] for i in xrange(2, n+1)}
    for i in xrange(2, n+1):
        if not i%1000:
            print 'Checking relative primeness: %s'%i
        for factor in f[i]:
            for j in xrange(i+factor, n+1, factor):
                if phi_n[j][1] != i:
                    phi_n[j][0] -= 1
                    phi_n[j][1] = i
    #print phi_n

    # get max
    max_n = 2
    max_val = 2.0
    for i in xrange(3, n+1):
        tmp = i*1.0/phi_n[i][0]
        if tmp > max_val:
            max_val = tmp
            max_n= i

    #print f
    #print phi_n
    print max_val
    print max_n

#main(1000000)
#main(10)
#main2(1000000)
#main3(1000000)

# Ah, idiot. No need to bruteforce. Just use the euler totient formula!
