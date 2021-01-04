from typing import Optional, List


class BinaryTreeNode:
    def __init__(self, data, parent):
        self.data = data
        self.right = None
        self.left = None
        self.parent = parent



def successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not node:
        return None
    root = get_root(node)
    sorted_items: List[BinaryTreeNode] = []
    fill_sorted_items(root, sorted_items)
    for index in range(len(sorted_items)):
        if sorted_items[index].data > node.data:
            return sorted_items[index]
    return None



def fill_sorted_items(root: BinaryTreeNode, sorted_items: List[BinaryTreeNode]) -> None:
    if not root:
        return 
    fill_sorted_items(root.left, sorted_items)
    sorted_items.append(root)
    fill_sorted_items(root.right, sorted_items)



def get_root(node: BinaryTreeNode) -> BinaryTreeNode:
    if not node.parent:
        return node
    return get_root(node.parent)
    


root = BinaryTreeNode(6, None)
root.left = BinaryTreeNode(3, root)
root.right = BinaryTreeNode(9, root)
root.left.left = BinaryTreeNode(1, root.left)
root.left.right = BinaryTreeNode(4, root.left)
root.right.left = BinaryTreeNode(7, root.right)
root.right.right = BinaryTreeNode(10, root.right)

 #         6
 #      /      \
 #    3         9
 #  /   \      /  \
 # 1     4    7    10
print(successor(root.right.left).data)

