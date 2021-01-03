# Questions to ask
# what is the definition of balanced? if not given
from Nodes import BinaryTreeNode


def is_balanced(root: BinaryTreeNode) -> bool:
    if not root:
        return True
    if abs(get_height(root.left) - get_height(root.right)) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


def get_height(root):
    if not root:
        return -1
    else:
        return max(get_height(root.left), get_height(root.right)) + 1



import collections


def is_balanced1(root: BinaryTreeNode) -> bool:
    BalancedStatuswithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(root: BinaryTreeNode) ->bool:
        if not root: 
            return BalancedStatuswithHeight(True, -1)
        else:
            left = check_balanced(root.left)
            if not left.balanced:
                return left
            right = check_balanced(root.right)
            if not right.balanced:
                return right

            if abs(right.height - left.height) > 1:
                return BalancedStatuswithHeight(False, 0)
            
            return BalancedStatuswithHeight(True, max(left.height, right.height) + 1)

    return check_balanced(root).balanced


# driver code
root = BinaryTreeNode("A")
root.left = BinaryTreeNode("B")
root.right = BinaryTreeNode("C")
root.left.left = BinaryTreeNode("D")
root.left.right = BinaryTreeNode("E")
root.left.left.left = BinaryTreeNode("G")
root.right.right = BinaryTreeNode("C")
# root.right.left = BinaryTreeNode("Z")
root.right.right.left = BinaryTreeNode("H")
root.right.right.right = BinaryTreeNode("I")

print(is_balanced1(root))
