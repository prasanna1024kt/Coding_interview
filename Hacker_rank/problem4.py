import math

start=25
end=30
start = int(input("Enter lower range: "))
end = int(input("Enter upper range: "))
power=5
power1=5
a=[]
a=range(power)
a1=[]
a1=range(power1)

arr1=[0]
for i in range(power+1):
    data=[pow(i,x) for x in range(i-1)]
    #print data
#print data

for i in range(power1+1):
    data1=[pow(i,x) for x in range(i-1)]

for line in data:
    if line not in arr1:
        arr1.append(line)
#print arr1
    


arr2=[0]
for i in range(power+1):
    arr2.append(pow(i,i))
#print arr2
power_of_arr=[]
for i in arr1 :
    for j in arr2 :
        power_of_arr.append(i+j)
#print power_of_arr
output=[]
for i in range(start,end+1):
    for k in power_of_arr:
        if i==k:
            if i not in output:
                output.append(i)
for line in output:
    print line
        
        
    
