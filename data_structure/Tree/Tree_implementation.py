class BinaryTree(object):

    def __init__(self,newNode):

        self.key=newNode
        self.leftChild=None
        self.rightChild=None

    def insertLeftChild(self,newNode):

        if self.leftChild == None: # if left child is none adding child to left side
            self.leftChild=BinaryTree(newNode)
        else: # if child exists push the existing child to down and new child will be append
            val =BinaryTree(newNode)
            val.leftChild=self.leftChild
            self.leftChild=val

    def getLeftChild(self):
        return self.leftChild

    def getValue(self):
        return self.key

    def insertRightChild(self,newValue):

        if self.rightChild == None:
            self.rightChild = BinaryTree(newValue)
        else:

            val = BinaryTree(newValue)
            val.rightChild=self.rightChild
            self.rightChild=val
    def getRightChild(self):

        return self.rightChild



obj=BinaryTree(12)
obj.insertLeftChild(13)
obj.insertLeftChild(15)

print obj.key

print obj.getLeftChild().getValue()


obj.insertRightChild(14)
obj.insertRightChild(16)
print obj.getRightChild().getValue()
