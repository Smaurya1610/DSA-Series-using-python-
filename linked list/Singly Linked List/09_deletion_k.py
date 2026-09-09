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

# from k th position
k=2
temp=head
for i in range(0,k-1):
    temp=temp.next
temp.next=temp.next.next
print_linkedlist(head)
