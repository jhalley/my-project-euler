def prime_number_generator(a,b):
    primes_list = [True for i in xrange(b)]
    
    for i in xrange(2, len(primes_list)):
        if primes_list[i]:
            for j in xrange(i*2, len(primes_list), i):
                primes_list[j] = False
    
    return [i for i in xrange(a, len(primes_list)) if primes_list[i]]
    
def pe49():
    primes = prime_number_generator(1000, 10000)
    primes_set = [set(str(i)) for i in primes]
    
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if (primes_set[i] == primes_set[j] == primes_set[k]) and (primes[j] - primes[i] == primes[k] - primes[j]):
                    temp_str = str('%i%i%i')%(primes[i], primes[j], primes[k])
                    if not temp_str == '148748178147':
                        print temp_str
                        return
                    
pe49()