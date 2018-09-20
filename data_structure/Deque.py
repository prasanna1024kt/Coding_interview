class Deque():

    def __init__(self):
        self.items=[]

    def isEmpty(self):

        return self.items ==[]

    def addRear(self,item):
        return self.items.insert(0,item)

    def addFront(self,item):
        return self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):

        return len(self.items)

d = Deque()

print(type(d))

d.addFront(2)
d.addRear(3)
d.addRear(4)
print(d.items)

print(d.removeFront())

print (d.removeRear())
