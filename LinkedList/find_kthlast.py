
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

# recursive solution linear time and space complexity, 
    # questions to ask
    # what's maximum length of linked list
    # what type of values are stored in linked list
    # can k be greated than length of the linked list
    # k = 0 is the last element or k = is the last element (in simple terms what's the range of k)
    # whether he wants node as retun value or value of the node as return value
    


    # assumption is k is always less than the length of the linked list
    # and k >= 1 ( 1<=k<= len(linkedlist))
    # we return None when head is None

def find_kthlast(head, k):

    if head == None:
        return 
    index = 0
    #to mimic the pass by reference so that all recursive stacks have the same value
    # this can also be done by creating a class with two prperties index and kth_value
    kth_value = [] 

    find_kth(head,k,index,kth_value)

    return kth_value[0]



def find_kth(head,k,index,kth_value):

    if head == None:
        return 0
    else:
        index = find_kth(head.next,k,index,kth_value) + 1
    
        
        if index == k:
            # the kth value
            kth_value.append(head.data)

        return index


# iterative solution linear time amd constant space
# clarify with intervierwer 
def find_kthlast1(head, k):

    if head == None:
        return None

    p1 = head
    p2 = head

    i = k
    # place p2 k distance apart from the beginning of the linked list
    while i> 0:
        i -=1
        # if k can be greater than length of linked list then put a null check
        p2 = p2.next

    #slide the windo until p2 hits the end 
    while p2:
        p2 = p2.next
        p1 = p1.next

    return p1.data

    



a = Node(1)
b = Node(2)
a.next = b
c = Node(3)
b.next = c
d = Node(4)
c.next = d


print(find_kthlast1(a,4))
print(find_kthlast(a,4))