#Questions to ask
# is the binary tree balanced or can it skewed as well, this doesn't affect the solution but it's goot to ask.
# what should be the out put format.
# what all data should the linked list node hold? shoul I include depth of tree in each node?.
# what type  of data does the tree hold? is it int/float/string/object?. 
# what is the range of values in tree?
# sigly linked list or doubly linked list?
# can tree nodes have null as data? or is it safe to assume that data will be valid

from typing import List
from queue import Queue

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next



def get_list_depth(root: TreeNode) -> List[LinkedList]:
    delimeter, q = None, Queue()
    q.put(root)
    q.put(delimeter)
    node_list : List[List[TreeNode]] = []
    temp_list : List[TreeNode] = []

    while not q.empty():
        curr_node = q.get()
        if curr_node is delimeter:
            node_list.append(temp_list)
            temp_list = []
            if not q.empty():
                q.put(None)
            continue
        temp_list.append(curr_node)
        if curr_node.left:
            q.put(curr_node.left)
        if curr_node.right:
            q.put(curr_node.right)

    result : List[LinkedList] = []

    for nodes in node_list:
        result.append(build_linked_list(nodes))

    return result

def build_linked_list(tree_nodes: List[TreeNode]) -> LinkedList:
    result_list: LinkedList = LinkedList()
    for node in tree_nodes:
        result_list.insert(node.data)
    return result_list

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.left.left.left = TreeNode('G')
root.right.right = TreeNode('C')
root.right.right.left = TreeNode('H')
root.right.right.right = TreeNode('I')

for linked_list in get_list_depth(root):
    result = []
    curr = linked_list.head
    while curr:
        result.append(curr.data)
        curr = curr.next

    print(result)


