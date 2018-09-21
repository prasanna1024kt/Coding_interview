# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 
import math

number= int(raw_input().strip())

arr = map(int,raw_input().strip().split(' '))
mean= sum(arr)/len(arr)

std = math.sqrt(sum(((x-mean)**2 for x in arr))/len(arr))

print std


