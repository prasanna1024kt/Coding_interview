import timeit

def binary_check(num):

    conv_bin=bin(num)[2:]
    return conv_bin == conv_bin[-1::-1]

def decimal_check(num):
    temp = num
    rev = 0
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10

    if num == rev:
        return True
    else:
        return False

if __name__ == '__main__':

    sum1=0

    start = timeit.default_timer()

    for num in xrange(0,1000000):
        if binary_check(num) and decimal_check(num):
            #lst.append(num)
            sum1 +=num
    print sum1
    stop = timeit.default_timer()

    print('Time: ', stop - start)

