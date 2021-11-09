class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

ll=LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)

# Print the linked list item
while ll.head != None:
    print(ll.head.item, end=" ")
    ll.head = ll.head.next

    
#print("hello")
