class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    class ListNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def insert(self, data):
        if not self.head:
            self.head = self.ListNode(data)
            self.tail = self.head
        else:
            self.tail.next = self.ListNode(data)
            self.tail = self.tail.next
        self.size +=1

    def __len__(self):
        return self.size