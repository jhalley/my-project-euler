import sys
from math import log

# p = numerator
# q = denominator
# n = current iteration number
# maxn = max iteration number
# using the property that the next convergent in the series after p/q of sqrt(2) is (p+2q)/(p+q)
def pe57(n, maxn, p, q):
    nextp = p + 2*q
    nextq = p + q

    # two different ways of calculating digit length. both take about the same time.
    #is_num_greater = 1 if len(str(nextp)) > len(str(nextq)) else 0
    is_num_greater = int(log(nextp, 10)) - int(log(nextq, 10))
    if n == maxn:
        return is_num_greater
    else:
        return is_num_greater + pe57(n+1, maxn, nextp, nextq)

sys.setrecursionlimit(2000) # python has a recursion limit of 1000 by default. changing it to be much higher for the purposes of this program. could have just made the function a loop as well...
print pe57(1, 1000, 3, 2)
