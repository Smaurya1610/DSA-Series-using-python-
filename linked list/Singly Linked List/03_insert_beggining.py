class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(2)
b = Node(4)
c = Node(5)

a.next = b
b.next = c

head = a
print(head.data)
print(head.next.data)

def print_linkedlist(head):
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
    return temp

# to insert At beggining
newnode = Node(4)
newnode.next = head
head = newnode
print_linkedlist(head)
