


#quetions to ask
# can there buplicates in the given array
# what is the range of values is it just going to be integer or?


# to make it minimal hight bst we need to equal number elements on the subtrees as much as possible
# we can divide the array and make the mid as the root and insert left subarray to left sub tree and right subarray
# to right subtree recursively 
# NlogN solutiion is to write a BST.insert method insert picked mid element into BST resurively 
#O(N) solution find mid make that as root and resursively create left and right nodes using left and right subarrays respectively
class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def buildMinimalHeightBST(nums, left, right):

    if left > right:
        return None

    mid = left + (right - left)//2

    root = Node(nums[mid])

    root.left = buildMinimalHeightBST(nums, left, mid -1)
    root.right = buildMinimalHeightBST(nums, mid+1, right)

    return root

def getHeight(root):

    if not root:
        return 0 

    left = getHeight(root.left) + 1
    right = getHeight(root.right) + 1

    return max(left , right)

nums = [1,2,3,4,5,6,7,8,9]
root = buildMinimalHeightBST(nums, 0 , len(nums)-1)

print(getHeight(root))