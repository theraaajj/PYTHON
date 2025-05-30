## GREAT LEARNING YouTube Channel

## DOUBLY LINKED LIST



## class for creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

## class for creating an empty doubly linked list to initiate
class DoublyLL():
    def __init__(self):
        self.head = None

    def ftraversal(self):
        a = self.head
        while a is not None:
            print(a.data, end=" ")
            a = a.next

    def btraversal(self):
        if self.head is None:
            print("Empty")
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            while a is not None:
                print(a.data, end=" ")
                a = a.prev

    def insert_at_begin(self, data):
        node = Node(data)
        a = self.head
        a.prev = node
        node.next = a
        self.head = node
    
    def insert_at_end(self, data):
        node = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = node
        node.prev = a
        node.next = None

    def insert_at_pos(self, idx, data):
        node = Node(data)
        a = self.head
        for i in range(1, idx):
            a = a.next
        node.next = a.next
        a.next.prev = node
        a.next = node
        node.prev = a

    def delete_at_begin(self):
        a = self.head
        self.head = a.next
        a.next = None
        self.head.prev = None

    


ll = DoublyLL()
n1 = Node(1)
ll.head = n1
n2 = Node(2)
n1.next = n2
n2.prev = n1
n3 = Node(3)
n2.next = n3
n3.prev = n2
n4 = Node(4)
n3.next = n4
n4.prev = n3
n5 = Node(5)
n4.next = n5
n5.prev = n4

# ll.ftraversal()
# ll.btraversal()

ll.insert_at_begin(0)
ll.insert_at_end(6)
ll.insert_at_pos(2, 1.5)
# ll.ftraversal()

ll.delete_at_begin()
ll.btraversal()