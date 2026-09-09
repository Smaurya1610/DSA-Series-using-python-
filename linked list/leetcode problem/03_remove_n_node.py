# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(2)
b = Node(4)
c = Node(5)
d = Node(7)
e = Node(8)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head=a

def print_linkedlist(head):
    temp = head
    while temp != None:
        print(temp.data, end="-")
        temp = temp.next


def count_length(head):
    temp=head
    l=0
    while(temp!=None):
        l+=1
        temp=temp.next
    return l


def remove_nth_node(head, n):
    l = count_length(head)
    
    # ❗ agar first node delete karna hai
    if n == l:
        return head.next
    
    temp = head
    for i in range(l - n - 1):
        temp = temp.next
    
    temp.next = temp.next.next
    return head

def method_2(head,n):
    slow=head
    fast=head
    for i in range(n):
        fast=fast.next
    if fast==None:
        return head.next
    
    while(fast.next!=None):
        fast=fast.next
        slow=slow.next
    slow.next=slow.next.next
    return head

print_linkedlist(head)
head = method_2(head, 2)
print(f"after removing element, the linked list is", end="\n")
print_linkedlist(head)