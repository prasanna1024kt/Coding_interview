from fractions import Fraction
from math import ceil
import timeit

def egypt(f):
    e = int(f)
    f -= e
    parts = [e]
    while(f.numerator>1):
        e = Fraction(1, int(ceil(1/f)))
        parts.append(e)
        f -= e
    parts.append(f)
    return parts

start = timeit.default_timer()

a = Fraction(5,121)

print(egypt(a))
stop = timeit.default_timer()
print('Time: ', stop - start)