# given a linked list we have to delete a node in the linked list  
# given that node is present in between list and we donot have access to head 
# we havd to return the original list by deleting that node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(3)
b=Node(4)
c=Node(6)
a.next=b
b.next=c

def delete(node):
    node.data=node.next.data
    node.next=node.next.next

delete(b)


def print_linkedlist(head):
    temp = head
    while temp != None:
        print(temp.data, end=" ")
        temp = temp.next

print_linkedlist(a)