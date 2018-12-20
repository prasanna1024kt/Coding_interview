def sec_large_smallest(list1):
    larg = list1[0]
    sec_large = list1[0]
    small = list1[0]
    secon_small = list1[0]
    third_lar=list1[0]
    for item in list1:
        if item > larg:
            larg=item
        elif sec_large != larg and sec_large < item:
            sec_large =item
        elif third_lar != sec_large and third_lar != larg and third_lar < item:
            third_lar=item
        elif item < small :
            small =item
        elif secon_small != small and secon_small > item:
            secon_small=item

    print("largest element is %s " %larg)
    print("Second largest element is %s " % sec_large)
    print("Third largest element is %s " % third_lar)
    print("smallest element is %s " % small)
    print("second smallest  element is %s " % secon_small)


if __name__ == "__main__":

    print ("finding the second largest and smallest number from the list")
    arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
    sec_large_smallest(arr)


