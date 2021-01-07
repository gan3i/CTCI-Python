# ask can each tree node have a pointer to it's parent node
# is it guaranteed that nodes are present in tree. 
# can one of the node be the lCA


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def common_ancestor(p, q):
    delta = depth(p) - depth(q)
    if delta < 0:
        p, q = q, p
    delta = abs(delta)
    while delta:
        p = p.parent
        delta -=1
    while p != q:
        p, q = p.parent, q.parent
    return p

def depth(node):
    depth = 0
    while node:
        depth +=1
        node = node.parent
    return depth
    
#         6
#      /      \
#    3         9
#  /   \      /  \
# 1     4    7    10
#        \
#         5
#          \
#           90
    
root = BinaryTreeNode(6)

root.left = BinaryTreeNode(3)
root.left.parent = root
root.right = BinaryTreeNode(9)
root.right.parent = root

root.left.left = BinaryTreeNode(1)
root.left.left.parent = root.left
root.left.right = BinaryTreeNode(4)
root.left.right.parent = root.left
x = root.left.right
x.right = BinaryTreeNode(5)
x.right.parent = x
x.right.right = BinaryTreeNode(90)
x.right.right.parent = x.right

root.right.left = BinaryTreeNode(7)
root.right.left.parent = root.right
root.right.right = BinaryTreeNode(10)
root.right.right.parent = root.right

print(common_ancestor(root.left.left,x.right.right).data)

    


