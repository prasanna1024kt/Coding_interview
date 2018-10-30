# Enter your code here. Read input from STDIN. Print output to STDOUT


number = int(raw_input().strip())

arr = map(int, raw_input().strip().split(' '))

freg = map(int, raw_input().strip().split(' '))

s = []
for i in range(number):
    s += [arr[i]] * freg[i]


# print s

def median(data):
    new_list = sorted(data)
    if len(new_list) % 2 > 0:
        return new_list[len(new_list) / 2]
    elif len(new_list) % 2 == 0:
        return (new_list[(len(new_list) / 2)] + new_list[(len(new_list) / 2) - 1]) / 2.0


f_sum = sum(freg)

s = sorted(s)

if number % 2 != 0:
    q1 = median(s[:f_sum / 2])
    q3 = median(s[f_sum / 2 + 1:])
else:
    q1 = median(s[:f_sum / 2])
    q3 = median(s[f_sum / 2:])

print round((q3 - q1), 1)
