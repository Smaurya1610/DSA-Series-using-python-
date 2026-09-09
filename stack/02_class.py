# without top pointer
# through array
class Stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        # if len(self.st)==0:
        #     return -1
        if not self.st:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x

    def top(self):
        #    if len(self.st)==0:
        #     return -1
        if not self.st:
            return -1
        return self.st[-1]

    def size(self):
        return len(self.st)

    def display(self):
        if not self.st:
            return "No element present in stack"

        i = len(self.st)-1
        while (i >= 0):
            print(self.st[i])
            i -= 1


stack = Stack()

stack.push(4)
stack.push(7)
stack.push(8)
stack.push(9)

stack.display()

print(f"{stack.pop()} is poped from stack")

stack.display()

print(f"{stack.top()} is now the top most element in stack")

print(f"{stack.size()} is size of stack")
