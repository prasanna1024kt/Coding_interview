class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def nse(arr):
    st = Stack()
    element = 0
    next = 0

    st.push(arr[0])

    for i in range(1, len(arr), 1):

        next = arr[i]
        if st.isEmpty() == False:
            element = st.pop()
            while element < next:
                print ("element %s ---- %s " % (element, next))
                print(st.items)
                if st.isEmpty == True:
                    break
                element = st.pop()
            if element > next:
                st.push(element)
        st.push(next)

    while st.isEmpty == False:
            element = st.pop()
            next = -1
            print ("element %s ---- %s " % (element, next))


if __name__ == "__main__":
    arr = [11, 13, 7, 3]
    print(nse(arr))


