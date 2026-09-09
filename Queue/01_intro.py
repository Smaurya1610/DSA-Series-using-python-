# using list

class Queue:
    def __init__(self):
        self.st = []
        self.rear = -1
        self.front = -1

    def push(self, x):
        if self.rear == -1 and self.front == -1:
            self.front += 1
            self.rear += 1
            self.st.append(x)
        else:
            self.rear += 1
            self.st.append(x)

    def pop(self):
        if self.front == -1 and self.rear == -1:
            return "Underflow"
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            x = self.st[self.front]
            self.front += 1
            return x

    def peek(self):
        if self.front == -1 and self.rear == -1:
            return "No element present"
        return self.st[self.front]

    def display(self):
        if self.front == -1 and self.rear == -1:
            return "No element present"
        
        i=self.front
        while(i<self.rear+1):
            print(self.st[i])
            i+=1

    def size(self):
        l=0
        temp=self.front
        while temp!=self.rear:
            l+=1
            temp+=1
        l+=1
        return l

q = Queue()
q.push(10)
q.push(20)
q.push(30)

q.display()
print("Pop:", q.pop())
print("Peek:", q.peek())
print("Size:", q.size())