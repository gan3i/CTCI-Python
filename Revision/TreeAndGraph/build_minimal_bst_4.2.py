# quetions to ask
# can there buplicates in the given array
# what is the range of values is it just going to be integer or?


# to make it minimal hight bst we need to equal number elements on the subtrees as much as possible
# we can divide the array and make the mid as the root and insert left subarray to left sub tree and right subarray
# to right subtree recursively
# NlogN solutiion is to write a BST.insert method insert picked mid element into BST resurively
# O(N) solution find mid make that as root and resursively create left and right nodes using left and right subarrays respectively
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# O(n)
from typing import List


def build_minimal_height_bst(nums: List[int], left: int, right: int) -> Node:
    if left > right:
        return None
    mid = left + (right - left) // 2
    root = Node(nums[mid])
    root.left = build_minimal_height_bst(nums, left, mid - 1)
    root.right = build_minimal_height_bst(nums, mid + 1, right)
    return root


# O(nlog(n))
from bintrees import RBTree


def build_minimal_height_bst_bintrees(nums):
    # here SelfBalancingBST would be your implementaion of BST with self balancing property.
    # tree = SelfBalancingBST()
    tree = RBTree()
    for i in nums:
        tree.insert(i, i)
    return tree


# O(nlog(n))
from sortedcontainers import SortedList


def build_minimal_height_bst_sortedlist(nums):
    tree = SortedList()
    for i in nums:
        tree.add(i)
    return tree


def get_height(root):
    if not root:
        return 0
    left = get_height(root.left) + 1
    right = get_height(root.right) + 1
    return max(left, right)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = build_minimal_height_bst(nums, 0, len(nums) - 1)
print(get_height(root))
print(build_minimal_height_bst_bintrees(nums))
print(build_minimal_height_bst_sortedlist(nums))
