import sys

def maxlongesteven(array):

    N = len(array)

    # initialing the two variables =0
    val = count = 0

    for i in range(0,N):

        # checking the elements are even or not
        if array[i]%2==0:
            count +=1
        else:
            val = max(val,count)
            count =0
            #Reinitiating the value to 0 if even numbers are not in sequence/continuouse
    val = max(val,count)
    return val

if __name__ == '__main__':

    arr = [2,3,1,2,4,3]

    print(maxlongesteven(arr))
