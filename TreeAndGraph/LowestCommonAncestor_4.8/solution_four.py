
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class Result:
    def __init__(self,node,is_ancestor):
        node: BinaryTreeNode  = node
        is_ancestor: bool = is_ancestor


def common_ancestor(root, p, q):
    result = common_ancestor_helper(root, p, q)
    if result.is_ancestor:
        return r.node
    return None

def common_ancestor_helper(root, p, q):
    if not root:
        return Result(None, False)
    if root == p and root == q:
        return REsult(root, True)
    r_left = common_ancestor_helper(root.left, p, q)
    if r_left.is_ancestor:
        return r_left
    r_right = common_ancestor_helper(root.right, p, q)
    if r_right.is_ancestor:
        return r_right
    if not r_left.node and not r_right.node:
        return Result(root, True)
    elif root == p or root == q:
        is_ancestor = (root == q or root == p)
        return Result(root, is_ancestor)
    else:
        return Result(r_left.node if r_left.node else r_right.node, False) 

