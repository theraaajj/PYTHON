## GREAT LEARNING YouTube Channel

## SINGLY LINKED LIST



## class for creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## creating a node
# n = Node(8)
# print(n.data)
# print(n.next)

## class for creating an empty linked list to initiate
class SinglyLL():
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Epmty")
        else:
            a = self.head
            while a is not None:
                print(a.data)
                a = a.next

    def insert_at_begin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = node
    
    def insert_at_pos(self, data, pos):
        node = Node(data)
        a = self.head
        for i in range (1, pos-1):
            a = a.next
        node.next = a.next
        a.next = node

    def delete_at_begin(self):
        self.head = self.head.next
    
    def delete_at_end(self):
        a = self.head
        while a.next.next is not None:
            a = a.next
        a.next = None
    
    def delete_at_pos(self, pos):
        a = self.head
        for i in range (1, pos-1):
            a = a.next
        a.next = a.next.next


n1 = Node(5)
n2 = Node(15)
n3 = Node(52)
n4 = Node(35)
n5 = Node(45)
ll = SinglyLL()       ## created an empty list
## connecting all the nodes
ll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# ll.traversal()
ll.insert_at_begin(100)
# ll.traversal()
ll.insert_at_end(200)
# ll.traversal()
ll.insert_at_pos(300, 3)
# ll.traversal()

ll.delete_at_begin()
# ll.traversal()
ll.delete_at_end()
# ll.traversal()
ll.traversal()
ll.delete_at_pos(4)
ll.traversal()







# myLL = SinglyLL()          # an empty LL with the name myLL was made

# ## traversal
# a = myLL.head
# while a is not None:
#     print(a.head)
#     a = a.next

