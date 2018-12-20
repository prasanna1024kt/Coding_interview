# write a function to reverse the  singly linked list, function will take in the head of the list as input and return the new head of the list

class node(object):

    def __init__(self,value):
        self.value=value
        self.nextnode=None

def reverse(head):

    current=head
    prev=None
    next_node=None

    while current:

        next_node=current.nextnode

        current.nextnode=prev

        prev=current

        current=next_node

    return prev

a=node(1)
b=node(2)
c=node(3)
d=node(4)
e=node(5)

f=node(6)
g=node(7)
h=node(8)

a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e
e.nextnode=f
f.nextnode=g
g.nextnode=h

print("before reversing linked list")
print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)
#print(a.nextnode)
print("After reversing linked list")
reverse(a)
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)

'''
o/p 

before reversing linked list
2
3
4
After reversing linked list
3
2
1


'''