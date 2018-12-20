class node(object):

    def __init__(self,value):

        self.value=value
        self.nextnode=None

class circular_linked_list():

    def __init__(self):

        self.head=None

    def append(self,data):

        # if the no node is pesent in the list means empty linked list

       if not self.head:
           self.head=node(data)
           # node is available in the linked list , In circular linked list node is linked to head
           self.head.nextnode=self.head
       else:
           new_node = node(data)
           cur = self.head
           while cur.nextnode != self.head:
               cur=cur.nextnode
           cur.nextnode=new_node
           new_node.nextnode=self.head
    def print_circular_linked_list(self):

        cur = self.head

        while cur:
            print(cur.value)
            cur=cur.nextnode
            if cur.nextnode==self.head:
                break

    def prepend(self,data):
        new_node=node(data)
        cur=self.head
        new_node.nextnode=self.head

        # if no node in the list means empty linked list

        if not self.head:
            new_node.nextnode=new_node
        else:
            while cur.nextnode !=self.head:
                cur=cur.nextnode
            cur.nextnode=new_node
        self.head=new_node
    def pop(self,key):

        # while removing the keys from the circular linked list we need to consider 2 points namely
        # 1 if the key element is head
        if self.head.value == key:
            cur = self.head
            while cur.nextnode != self.head:
                cur=cur.nextnode
            cur.nextnode=self.head.nextnode
            self.head=self.head.nextnode
        else: #2. if key element is not head
            cur=self.head
            prev=None
            while cur.nextnode!=self.head:
                prev=cur
                cur= cur.nextnode
                if cur.value==key:
                    prev.nextnode=cur.nextnode
                    cur=cur.nextnode





circular_list =circular_linked_list()
circular_list.append("4")
circular_list.append("5")
circular_list.append("6")
print(type(circular_list))

print("appneding the data into list")
circular_list.print_circular_linked_list()
print("prepending the data into list")
circular_list.prepend("3")
circular_list.prepend("2")
circular_list.prepend("1")
circular_list.print_circular_linked_list()

circular_list.pop("2")
print("removing the data from list")
circular_list.print_circular_linked_list()

print(type(node))



