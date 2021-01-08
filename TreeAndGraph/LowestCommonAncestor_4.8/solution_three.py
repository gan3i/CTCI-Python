
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def common_ancestor(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None

    return ancestor_helper(root, p, q)

def ancestor_helper(root, p, q):
    if not root or root == p or root == q:
        return root

    p_onleft = covers(root.left, p)
    q_onleft = covers(root.left, q)

    if p_onleft is not q_onleft:
        return root

    if p_onleft and q_onleft:
        return ancestor_helper(root.left, p, q)
    else:
        return ancestor_helper(root.left, p, q)

def covers(root, p):
    if not root:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)


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
root.right = BinaryTreeNode(9)

root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(4)
x = root.left.right
x.right = BinaryTreeNode(5)
x.right.right = BinaryTreeNode(90)

root.right.left = BinaryTreeNode(7)
root.right.right = BinaryTreeNode(10)

r = BinaryTreeNode(10)



print(common_ancestor(root, root.left.left, r).data)