

def largest_con_sum(arr1):

    if len(arr1) == 0:
        print("empty list is passed into the function please pass valid list")
    current_sum =  max_sum = arr1[0]

    for num in arr1[1:]:
        #print num
        current_sum = max(current_sum+num,num)
        #print("current sum %s" %current_sum)

        max_sum = max(current_sum,max_sum)

        #print("max sum %s" % max_sum)

    return max_sum

if __name__ == "__main__":

    arr = [2,3,1,2,4,3]
    print(largest_con_sum(arr))