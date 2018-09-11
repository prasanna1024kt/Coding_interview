def wrapper(f):
    def fun(l):
        f(["+91"+" " +ptr1[-10:-5]+ " " +ptr1[-5:] for ptr1 in l])
    return fun
@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    print l
    sort_phone(l)