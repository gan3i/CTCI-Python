# Questions to ask
# is the binary tree balanced or can it skewed as well, this doesn't affect the solution but it's goot to ask.
# what should be the out put format.
# what all data should the linked list node hold? shoul I include depth of tree in each node?.
# what type  of data does the tree hold? is it int/float/string/object?.
# what is the range of values in tree?
# sigly linked list or doubly linked list?
# can tree nodes have null as data? or is it safe to assume that data will be valid
# null check on root
# should I build the linked list from the data or from the actual nodes

from typing import List
from Nodes import BinaryTreeNode
from LinkedList import LinkedList

#  a modfication of bfs where we travese level by level and build linked list
def get_list_of_depths_bfs(root: BinaryTreeNode) -> List[LinkedList]:
    result=[]
    curr=LinkedList()
    curr.insert(root)
    while len(curr)>0:
        result.append(curr)
        parent, curr=curr.head, LinkedList()
        while parent:
            if parent.data.left:
                curr.insert(parent.data.left)
            if parent.data.right:
                curr.insert(parent.data.right)
            parent = parent.next

    return result


# driver code
root = BinaryTreeNode("A")
root.left = BinaryTreeNode("B")
root.right = BinaryTreeNode("C")
root.left.left = BinaryTreeNode("D")
root.left.right = BinaryTreeNode("E")
root.left.left.left = BinaryTreeNode("G")
root.right.right = BinaryTreeNode("C")
root.right.right.left = BinaryTreeNode("H")
root.right.right.right = BinaryTreeNode("I")

for linked_list in get_list_of_depths_bfs(root):
    result = []
    curr = linked_list.head
    while curr:
        result.append(curr.data.data)
        curr = curr.next

    print(result)
