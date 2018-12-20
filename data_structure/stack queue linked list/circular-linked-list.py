# Problem : Write function which takes in the first node in singly linked list and returns boolean indicating if the linked list contains a "cycle "


class node(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None


def cycle_check(node):

        marker1 = node
        marker2=node

        while marker2 != None and marker2.nextnode != None:

            marker1 = marker1.nextnode
            marker2 = marker2.nextnode.nextnode

            if marker2 == marker1:
                return True
        return False


# cyclic linked list
a=node(1)
b=node(2)
c=node(3)
d=node(4)
e=node(5)

a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=a

print(cycle_check(a))

# Non cyclic linked list
x=node(1)
y=node(2)
z=node(3)
x1=node(7)

x.nextnode=y
y.nextnode=z
z.nextnode=x1
print(cycle_check(x))