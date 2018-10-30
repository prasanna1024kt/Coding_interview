import sys


number = int(raw_input().strip())
arr1 = map(int,raw_input().strip().split(' '))
arr2 = map(int,raw_input().strip().split(' '))
summa=float(sum(arr1[i] * arr2[i] for i in range(number) ))
summa2= float(sum(arr2))
weighted_mean = summa / summa2

print ("{0:.1f}".format(weighted_mean))