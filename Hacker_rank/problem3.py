import math

n=16
ram=1
sandy=0
t=10
def power_of_two(n,base=-1):
    result=2** base
    if result>n:
        base+=1
        power_of_two(n,base)
    else:
        if result==n:
              print base
        else:
            print base -1

def is_power(num):
    return num!=0 and ((num & (num-1))==0)

if is_power(n):
    n=n/2
else :
    power_of_two(n,t)
    
