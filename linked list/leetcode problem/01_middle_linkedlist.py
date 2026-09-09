# middle of linked list
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


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


def middle(head):
    temp = head
    l = 0
    while (temp != None):
        temp = temp.next
        l += 1
    temp = head
    for i in range(l//2):
        temp = temp.next
    return temp

# method 2 is fast and slow pointer   through this when the fast is on last then slow is on the middle
def method_2(head):
    slow=head
    fast=head

    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next

        

value = middle(head)
print(value.data)
