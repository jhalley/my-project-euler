def pe43():
    d = {}
    x = [2,3,5,7,11,13,17]
    candidates = []
    answer = []
    pandigital_set = set('0123456789')
    
    def r_candidate_finder(xindex, a, candidate):
        if not candidate: candidate = a
        if xindex == len(x):
            if len(set(candidate)) == 9:
                candidates.append(candidate)
            return
        for b in d[x[xindex]]:
            if a[1:] == b[:-1]: r_candidate_finder(xindex+1, b, candidate + b[-1])
    
    for i in x:
        d[i] = []
        for j in xrange(10, 1000):
            if not j%i:
                d[i].append(str(j).rjust(3, '0'))
            
    for i in d[x[0]]:
        r_candidate_finder(1, i, '')
        
    for i in candidates:
        answer.append(int(pandigital_set.difference(set(i)).pop() + i))
        
    return sum(answer)
    
print pe43()