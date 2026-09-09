# Given a Singly Linked List, Delete all alternate nodes of the list ie delete all the nodes present in even positions.
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


def method_1(head):
    temp=head
    while temp!=None and temp.next!=None:
        temp.next=temp.next.next
        temp=temp.next

    return head

