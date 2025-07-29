class node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(5)
next_node = Node(12)
head.next = next_node

class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1
    def insertFirst(self, data):
        new_node = Node(data)
        tmp_node = self.head
        self.head = new_node
        self.head.next = temp_node

        self.list_size += 1