
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class Result:
    def __init__(self,node,is_ancestor):
        self.node: BinaryTreeNode  = node
        self.is_ancestor: bool = is_ancestor



def common_ancestor(root, p, q):
    result = common_ancestor_helper(root, p, q)
    if result.is_ancestor:
        return result.node
    return None

def common_ancestor_helper(root, p, q):
    if not root:
        return Result(None, False)
    if root == p and root == q:
        return Result(root, True)
    r_left = common_ancestor_helper(root.left, p, q)
    if r_left.is_ancestor:
        return r_left
    r_right = common_ancestor_helper(root.right, p, q)
    if r_right.is_ancestor:
        return r_right
    if r_left.node and r_right.node:
        return Result(root, True)
    elif root == p or root == q:
        is_ancestor = (r_left.node or r_right.node)
        return Result(root, is_ancestor)
    else:
        return Result(r_left.node if r_left.node else r_right.node, False)



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

print(common_ancestor(root, root.right.right, x.right.right).data)
