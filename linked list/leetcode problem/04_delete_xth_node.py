# we have to delete a xth node from a linked list
# given that index is start from 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(2)
b = Node(4)
c = Node(3)
d = Node(7)
e = Node(8)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head = a
# main logic
def method_1(head,x):
    temp=head
    if x==1:
        head=head.next
        return head
    
    for i in range(1,x-1):
        temp=temp.next
    temp.next=temp.next.next
    return head

method_1(head,3)

def print_linkedlist(head):
    temp = head
    while temp != None:
        print(temp.data, end="\n")
        temp = temp.next
print_linkedlist(head)