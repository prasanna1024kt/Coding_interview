# # # To find minimum sum of unique elements
# # def minSum(arr, n):
# #     sum = arr[0];
# #     prev = arr[0]
# #
# #     for i in range(1, n):
# #
# #         # If violation happens, make current
# #         # value as 1 plus previous value and
# #         # add to sum.
# #         if arr[i] <= prev:
# #             prev = prev + 1
# #             sum = sum + prev
# #
# #             # No violation.
# #         else:
# #             sum = sum + arr[i]
# #             prev = arr[i]
# #
# #     return sum
# #
# #
# # # Drivers code
# # arr = [3,1,2,2]
# # n = len(arr)
# # print(minSum(arr, n))
# #
# #
#
# import collections
#
#
# # function to find minimum increment required
# def minIncrementForUnique(A):
#     # collect frequency of each element
#     count = collections.Counter(A)
#
#     # array of unique values taken
#     taken = []
#
#     ans = 0
#
#     for x in range(100000):
#         if count[x] >= 2:
#             taken.extend([x] * (count[x] - 1))
#         elif taken and count[x] == 0:
#             ans += x - taken.pop()
#
#             # return answer
#     return ans
#
#
# # Driver code
# A = [3, 2, 1, 2]
# print(minIncrementForUnique(A))


# Python3 program to make sorted array elements
# distinct by incrementing elements and keeping
# sum to minimum.

# To find minimum sum of unique elements.
def minSum(arr, n):
    sm = arr[0]

    for i in range(1, n):

        if arr[i] == arr[i - 1]:


            j = i
            while j < n and arr[j] <= arr[j - 1]:
                arr[j] = arr[j] + 1
                j += 1
                flag = 1
        #if flag == 0:
        sm = sm + arr[i]

    return sm


# Driver code
arr = [2,2,4,5]
n = len(arr)
print(minSum(arr, n))

# sum1 = arr[0]
#     n=len(arr)
#
#     for i in range(1,n):
#         if arr[i] == arr[i-1]:
#             j=i
#             while j<n and arr[j] <= arr[j-1]:
#                 arr[j]=arr[j] + 1
#                 j +=1
#         sum1 = sum1 + arr[i]
#     return sum1