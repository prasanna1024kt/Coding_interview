import sys

def small_second_element(array):

    # initiating 2 variable to 0
    first = second = sys.maxint

    for i in range(0,len(array)):

        if array[i]<first:
            second=first
            first=array[i]
        if (array[i]< second and array[i]!=first):
            second=array[i]
    print("first smallest valus is %s and second smallest is %s"%(first,second))

if __name__ == "__main__":
    arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
    print(small_second_element(arr))

