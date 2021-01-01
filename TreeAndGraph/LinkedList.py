class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def insert(self, data):
        if not self.head:
            self.head = self.Node(data)
            self.tail = self.head
        else:
            self.tail.next = self.Node(data)
            self.tail = self.tail.next