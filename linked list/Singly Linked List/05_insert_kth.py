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


#  to traverse


def print_linkedlist(head):
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
    return temp
# in list  first index = 0
#  insert at kth position
k=2
newnode=Node(6)
temp=head
for i in range(0,k-1):
    temp=temp.next
    
newnode.next=temp.next
temp.next=newnode

print_linkedlist(head)
    
    