# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy as np

from scipy import stats
n =int(raw_input().strip())

arr = map(int,raw_input().strip().split(' '))
ptr=stats.mode(arr)[0]

print np.mean(arr)
print np.median(arr)
print str(ptr)[1:-1]