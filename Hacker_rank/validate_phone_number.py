import re

N = int(raw_input())

for i in range(0,N):
    number = raw_input()

    check_number = re.compile("[7-9]\d{9}")

    if len(number)==10 and check_number.match(number):
        print("Yes %s"%number)
    else:
        print("No %s " %number)
