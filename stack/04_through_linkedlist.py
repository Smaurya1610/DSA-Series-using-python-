#  generate a stack using linked list
# to implement stack using this we push element from the head pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        if self.top == None:
            self.top = Node(x)
            return
        else:
            newnode = Node(x)
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if self.top == None:
            return "No element present"

        else:
            temp = self.top
            self.top = self.top.next
            return temp.data

    def peek(self):
        if self.top == None:
            return "No element present"

        return self.top.data
    
    def display(self):
            if self.top==None:
              return "No element present"
            temp=self.top
            while(temp!=None):
                print(temp.data)
                temp=temp.next

    def size(self):
        temp=self.top
        l=0
        while temp!=None:
            l+=1
            temp=temp.next
        return l


stack=Stack()
stack.push(2)
stack.push(4)
stack.push(5)
stack.push(8)
print("The element of stack is --")
stack.display()
print(f"{stack.size()} is the size of stack")
print(f"{stack.peek()} is the top most element in stack")

print(f"{stack.pop()} is pop now")
print("The element of stack is --")
stack.display()
print(f"{stack.size()} is the size of stack")
print(f"{stack.peek()} is the top most element in stack")
            
            

