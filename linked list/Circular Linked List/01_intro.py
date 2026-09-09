class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(2)
b=Node(3)
c=Node(4)

head=a

a.next=b
b.next=c
c.next=head
# traverse
temp = head

while True:
    print(temp.data)
    temp = temp.next
    if temp == head:
        break