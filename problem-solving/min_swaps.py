# def minSwaps(arr, n):
#     numberOfOnes = 0
#
#
#     for i in range(0, n):
#
#         if (arr[i] == 1):
#             numberOfOnes = numberOfOnes + 1
#
#
#     x = numberOfOnes
#
#     count_ones = 0
#     maxOnes = 0
#
#
#     for i in range(0, x):
#
#         if (arr[i] == 1):
#             count_ones = count_ones + 1
#
#     maxOnes = count_ones
#
#
#     for i in range(1, (n - x + 1)):
#
#
#         if (arr[i - 1] == 1):
#             count_ones = count_ones - 1
#
#
#         if (arr[i + x - 1] == 1):
#             count_ones = count_ones + 1
#
#         if (maxOnes < count_ones):
#             maxOnes = count_ones
#
#
#     numberOfZeroes = x - maxOnes
#
#     return numberOfZeroes
#
#
# # Driver Code
# a = [0, 0, 1, 0, 1, 1, 0, 0, 1]
# n = 9
# print (minSwaps(a, n))


def minSwaps(arr, n):
    noOfOnes = 0

    # find total number of
    # all in the array
    for i in range(n):
        if (arr[i] == 1):
            noOfOnes = noOfOnes + 1

    # length of subarray to check for
    x = noOfOnes

    maxOnes = -2147483648

    # array to store number of 1's upto
    # ith index
    preCompute = {}

    # calculate number of 1's upto ith
    # index and store in the
    # array preCompute[]
    if (arr[0] == 1):
        preCompute[0] = 1
    for i in range(1, n):
        if (arr[i] == 1):
            preCompute[i] = preCompute[i - 1] + 1
        else:
            preCompute[i] = preCompute[i - 1]

    # using sliding window
    # technique to find
    # max number of ones in
    # subarray of length x
    for i in range(x - 1, n):
        if (i == (x - 1)):
            noOfOnes = preCompute[i]
        else:
            noOfOnes = preCompute[i] - preCompute[i - x]

        if (maxOnes < noOfOnes):
            maxOnes = noOfOnes

            # calculate number of zeros in subarray
    # of length x with maximum number of 1's
    noOfZeroes = x - maxOnes
    print preCompute
    l = 0
    for k,v in preCompute.items():
        l += v
    return l



a = [1 ,1, 1, 1, 0, 1, 0, 1]
n = len(a)

print(minSwaps(a, n))
