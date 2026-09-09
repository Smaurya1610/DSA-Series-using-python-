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

#  insertion at end

newnode=Node(1)
temp=head
while(temp.next!=None):
    temp=temp.next
temp.next=newnode
print_linkedlist(head)