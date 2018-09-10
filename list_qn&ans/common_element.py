def common_element(list1,list2):

    list1_a = set(list1)
    list1_b = set(list2)

    if len(list1_a.intersection(list1_b))>0:
        return "common element are present "
    else:
        return "no common elements are present in both list"


if __name__ == "__main__":

    a1 = [1,2,3,4,5]
    b1 = [2,7,8,9]

    print(common_element(a1,b1))