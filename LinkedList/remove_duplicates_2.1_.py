
#ask questions 
# 1. is it a doubly linked list or singly linked list
# 2. what type of data are we storing, integer? float? string? can there be negatives,
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

# in interview do not write the linked list class assume that it's given
class LinkedList():
    def __init__(self):
        self.head = None

    # linear space and time complexity        
    def remove_duplicates(self):
        
        if self.head == None:
            return 
        # hash set the keeps track of values that we have already seen    
        hash_set =set()

        current = self.head
        prev = None
        while current:

            if current.data in hash_set: # found the duplicate  node
                temp = current
                current = current.next
                self.remove_node(temp, prev)
            else:
                hash_set.add(current.data)
                prev = current
                current = current.next


    # quadratic time and constant space
    def remove_duplicates1(self):
        current = self.head

        while current:
            prev_node = current
            next_node = current.next
            
            while next_node:

                if prev_node.data == next_node.data:
                    temp = next_node
                    next_node = next_node.next
                    self.remove_node(temp,prev_node)
                else:
                    prev_node = next_node
                    next_node = next_node.next

            current = current.next

    def remove_node(self,node, prev):
        prev.next = node.next
        node = None



    # algorithm ends here rest is just are just helper methods for linked list


    @staticmethod
    # to add a new Node to the sigly linked list
    def add_node(head,data):
        
        # if the head is None return new node
        if head == None:
            return Node(data)
        # else travel to the end of the Node recursively and insert the new node at the end
        head.next = LinkedList.add_node(head.next,data) 

        return head

    def add(self,data):
        # self.head = LinkedList.add_node(self.head, data)

        if self.head == None:
            self.head = Node(data)

        end = self.head

        while end.next:
            end = end.next

        end.next = Node(data)

    def print(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


linked_list = LinkedList()
linked_list.add(1)
# linked_list.add(1)
# linked_list.add(3)
# linked_list.add(3)
# linked_list.add(4)

linked_list.remove_duplicates1()

linked_list.print()





