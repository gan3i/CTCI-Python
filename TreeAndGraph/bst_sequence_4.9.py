from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def all_sequences(root):
    result = []
    if not root:
        result.append(deque())
        return result
    # get the sequences from left and right subtrees
    left_sequences = all_sequences(root.left)
    right_sequences = all_sequences(root.right)
    # weave together each sequence from left sequece to right sequence
    for left in left_sequences:
        for right in right_sequences:
            weaved = []
            weave_lists(left, right, weaved, deque([root.data]))
            result.extend(weaved)
    return result


def weave_lists(first, second, results, prefix):
    if not first or not second:
        # deep clone the prefix since it will be changed
        # once we go back in recursion
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return
    # remove one element from the begining of the list and
    # append it to prefix and recurse, and once returned back from
    # from recusrion add the element back to begining of the list
    # remove  it from prefix.
    head_first = first.popleft()
    prefix.append(head_first)
    weave_lists(first, second, results, prefix)
    first.appendleft(head_first)
    prefix.pop()
    # do the exact steps for second list.
    head_second = second.popleft()
    prefix.append(head_second)
    weave_lists(first, second, results, prefix)
    second.appendleft(head_second)
    prefix.pop()


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
# x = root.left.right
# x.right = BinaryTreeNode(5)
# x.right.right = BinaryTreeNode(90)

# root.right.left = BinaryTreeNode(7)
# root.right.right = BinaryTreeNode(10)


from pprint import pprint

pprint([list(x) for x in all_sequences(root)])
pprint(len(all_sequences(root)))
