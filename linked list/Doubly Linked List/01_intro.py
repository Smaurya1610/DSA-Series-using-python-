class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

a=Node(2)
b=Node(3)
c=Node(4)

a.next=b
b.prev=a
b.next=c
c.prev=b


