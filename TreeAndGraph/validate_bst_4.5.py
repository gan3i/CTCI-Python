from Nodes import BinaryTreeNode


def is_bst(root: BinaryTreeNode) -> bool:
    def fill_sorted_items(root):
        if not root:
            return
        fill_sorted_items(root.left)
        sorted_items.append(root.data)
        fill_sorted_items(root.right)

    sorted_items = []
    fill_sorted_items(root)
    i = 1
    while i < len(sorted_items):
        if sorted_items[i - 1] >= sorted_items[i]:
            return False
        i += 1

    return True


class WrapPreviousNodeData:
    def __init__(self, data):
        self.data = data


def is_bst1(root: BinaryTreeNode) -> bool:
    def validate_bst(root):
        if not root:
            return True
        if not validate_bst(root.left):
            return False
        if root.data <= previous_node_data.data:
            return False
        previous_node_data.data = root.data
        if not validate_bst(root.right):
            return False
        return True

    previous_node_data: WrapPreviousNodeData = WrapPreviousNodeData(float("-inf"))
    return validate_bst(root)


def is_bst2(root: BinaryTreeNode) -> bool:
    def validate_bst(root, min, max):
        if not root:
            return True
        if root.data <= min or root.data >= max:
            return False
        if not (
            validate_bst(root.left, min, root.data)
            and validate_bst(root.right, root.data, max)
        ):
            return False
        return True

    return validate_bst(root, float("-inf"), float("+inf"))


root = BinaryTreeNode(6)
root.left = BinaryTreeNode(3)
root.right = BinaryTreeNode(9)
root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(8)
root.right.left = BinaryTreeNode(7)
root.right.right = BinaryTreeNode(10)


print(is_bst1(root))
