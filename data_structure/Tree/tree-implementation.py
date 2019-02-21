"""
The Tree data structure has a root , brnaches and leaves .

All the childrun of one node is independent of another node.
Each leaf node is unique

Node: node is the fundamental part of the tree it can have name, which call as "key"
     Node may also have an additional information this is called as "payload"
     Payload information is not central for many algorithm it's often critical application that make use of tree.

Edge : Edge is another fundamental part of the tree. It's connects the two nodes and shows relationship between them
        Every node  except root is connecting from the another incoming edge from another node.
        Each node may have several outgoing edges.

Root: Root of the tree is the only node which don't have any incoming edges.

PAth : PAth is the ordered list of node connected by edges

Children : The set of node "c" that are incoming edges from the same node they are called it has children of that node.

PArent : A node is parent of all the nodes which connects with outgoing edges.

Sibling : A node in tree which is children of the same parents called as sibling.

SubTree : Subtree is the set of nodes and edges comprised of the parents and all the descendants of that parents.

LeafNode: Node in tree doesn't have children node called as leafnode.

Level : Level of the node "n" is the number of edges on the path from the root node to "n".

Height : The height of the tree is equal to maximum level of any node in the tree.

"""