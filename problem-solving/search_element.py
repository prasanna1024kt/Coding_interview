list1 = [2,4,5,7,9,12,14,16,17,19,22,25,27,28,33,37]
target=28

def linear_search(data,target):

    for i in range(len(data)):

        if data[i]==target:
            return True
    return False



