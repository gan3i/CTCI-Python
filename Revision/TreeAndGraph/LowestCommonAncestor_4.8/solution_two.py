class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def common_ancestor(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q
    sibling = get_sibling(p)
    parent = p.parent
    while not covers(sibling, q):
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent


def covers(root, p):
    if not root:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)


def get_sibling(node):
    if not node or not node.parent:
        return None
    parent = node.parent
    return parent.right if parent.left == node else parent.left


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

print(common_ancestor(root, root.left.left, root.right.right).data)
