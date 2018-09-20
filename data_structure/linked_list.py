class node(object):

    def __init__(self,data ):
        self.data = data
        self.nextNode = None

class linkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self,data):
        self.size += 1

        newNode = node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):
        return self.size

    def insertEnd(self,data):
        self.size +=1
        newNode = node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%s " %actualNode.data)
            actualNode = actualNode.nextNode


    def remove(self,data):

        if self.head is not None:
            return
        currentNode = self.head
        prevNode =None

        while currentNode.nextNode != data:
            prevNode = currentNode
            currentNode = currentNode.nextNode
        if prevNode is None:
            self.head =currentNode.nextNode
        else:
            prevNode.nextNode = currentNode.nextNode

ln = linkedList()
ln.insertStart(1)
ln.insertStart(11)
ln.insertStart(12)
ln.insertEnd(19)
ln.traverseList()
ln.remove(1)
ln.traverseList()
#print(ln.size())