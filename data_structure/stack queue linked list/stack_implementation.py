class Stack(object):

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self,item):

        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":

    print("stack implementation ")

    s = Stack()

    print s.isEmpty()

    s.push(5)
    s.push(4)
    s.push(6)
    s.push("ptr")
    s.push("stack")
    s.push(50)

    print s.peek()
    print s.isEmpty()
    print s.size()
    print s.pop()
    print s.size()
    print s.pop()
    print s.size()
