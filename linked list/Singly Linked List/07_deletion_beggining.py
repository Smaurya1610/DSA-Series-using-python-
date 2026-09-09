class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(2)
b=Node(4)
c=Node(5)
d=Node(6)
e=Node(7)
        
a.next=b
b.next=c
c.next=d
d.next=e

head=a
#  to traverse
def print_linkedlist(head):
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
    return temp

# deletion from beggining
temp=head
head=head.next # node isolate ho gya 
temp.next=None # node none
temp=None
print_linkedlist(head)