from itertools import permutations as p

MEMOIZED = {} 
MEMOIZED[1] = 1
MEMOIZED[89] = 89
END_NUM = {1:0, 89:0}
UPPER_LIMIT = 10000000

def pe92():
    for i in xrange(2, UPPER_LIMIT): # we start at 2 because 0 is meaningless and we already know the value for 1
        figure_end(i)
    for i in xrange(1, UPPER_LIMIT):
        END_NUM[MEMOIZED[i]] += 1
    print END_NUM

def figure_end(x):
    global MEMOIZED
    global END_NUM

    if x in [1, 89]:
        return x
    elif x in MEMOIZED:
        return MEMOIZED[x]
    else:
        final_num = figure_end(sum([int(i)**2 for i in str(x)]))
        for k in set([int(''.join(j)) for j in p([i for i in str(x)])]):
            MEMOIZED[k] = final_num

        return final_num

pe92()
