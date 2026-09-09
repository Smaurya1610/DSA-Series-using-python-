# with top pointer implement a stack
# through array
class Stack:
    # to create a stack
    def __init__(self):
        self.st = []
        self.top = -1

    # to push element in stack
    def push(self, x):
        self.top += 1
        self.st.append(x)

    # to pop element
    def pop(self):
        if self.top == -1:
            return "No element is present"
        else:
            x = self.st[self.top]
            self.top -= 1
        return x

    # to show the top most element
    def peek(self):
        if self.top == -1:
            return "No element is present"

        return self.st[self.top]

    # to show all the element in stack
    def display(self):
        if self.top == -1:
            return "No element is present in stack"
        else:
            i = self.top
            while (i >= 0):
                print(self.st[i])
                i -= 1

    # to count the length of stack
    def len(self):
        # return len(self.st)
        i = self.top
        l = 0
        while i >= 0:
            l += 1
            i -= 1
        return l


stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

stack.display()
print(f"{stack.pop()} is poped")
stack.display()
print(f"{stack.peek()} is the top most element")

print(f"{stack.len()} is the length of stack")
