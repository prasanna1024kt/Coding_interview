"""

Traversal is the process of visiting the all the nodes and printing the value too.

There are 3 way which can be used to traverse a tree.

1.In-order Traversal: In this traversal method, left subtree is visited first then the root and later right side.
  left node->root node->right node

2.Pre-order Traversal: In this traversal method,root node is visited first then left subtree and later right side.
  root node -> left node -> right node

3.Post-order Traversal: In this traversal method, First we traverse left subtree, then right subtree and finally root node.

  left subtree -> right subtree -> root node



"""

class binaryTree(object):

    def __init__(self,newValue):

        self.data = newValue
        self.left=None
        self.right=None

    def insertBSTree(self,data):

        if self.data:

            if data < self.data:

                if self.left is None:
                    self.left=binaryTree(data)
                else:
                    self.left.insertBSTree(data)
            elif data > self.data:

                if self.right is None:
                    self.right=binaryTree(data)
                else:
                    self.right.insertBSTree(data)
        else:
                self.data=data

    def print_tree(self):

        if self.left:
            self.left.print_tree()
        #print self.data,
        if self.right:
            self.right.print_tree()
        print self.data,

    def lookup(self,findval):

        if findval < self.data:

            if self.left is None:
                return str(findval)+" Not Found"
            return self.left.lookup(findval)

        elif findval > self.data :

            if self.right is None:
                return str(findval)+ " Not Found"
            return self.right.lookup(findval)

        else:

            return str(findval)+" Found"


    def inOrderTraversal(self,root):
     # left node->root node->right node
        res=[]

        if root:

            res= self.inOrderTraversal(root.left)
            res.append(root.data),
            res = res + self.inOrderTraversal(root.right)
        return res

    def preOrderTraversal(self,root):
        res=[]
     #root node -> left node -> right node

        if root:
            res.append(root.data)
            res= res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res

    def postOrderTraversal(self,root):
 #left subtree -> right subtree -> root node
        res=[]
        if root:

            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)

        return res


bst=binaryTree(8)
bst.insertBSTree(7)
bst.insertBSTree(9)
bst.insertBSTree(10)
bst.insertBSTree(5)
bst.insertBSTree(4)
bst.insertBSTree(6)

print bst.print_tree()

print bst.lookup(6)
print("in 0rder traversal ")
print bst.inOrderTraversal(bst)
print("pre order traversal ")
print bst.preOrderTraversal(bst)
print("post order traversal ")
print bst.postOrderTraversal(bst)
