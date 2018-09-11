class Queue(object):

    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):

        return len(self.items)

q1 = Queue()
print(type(q1))

if  __name__ == "__main__":

    q = Queue()

    print q.isEmpty()
    q.enqueue(5)
    q.enqueue(2)
    print q.dequeue()
    print q.dequeue()
    print(type(q))



