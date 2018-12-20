import os

#finding the missing element of the list

#if missing element is one
def missing(list1):
    n=len(list1)
    tot = (n+1)*(n+2)/2
    sum_a=sum(list1)
    return tot - sum_a


# above function used to get the missing element of one variable but it'll fail if missing element is more than one .
#  Below function will returns the if missing element is more than omne
def missing_elements(list1):
    #sorted(list1)

    list2 = set(range(list1[0],list1[-1]+1))
    return list2-set(list1)

if __name__ =="__main__":

    list1 = [1,4,2,6,3,5,7,8,9,10,11,13,15,14]

    list_two = [1, 4, 2, 6, 7, 8,9, 9, 11, 13, 15, 14]

    print(missing(list1))

    print("missing 2 element %s" %missing_elements(list_two))