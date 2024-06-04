class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.values.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.values[-1]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)


stack = Stack()


stack.push(10)
stack.push(12)
stack.push(14)


print(stack.size())

print(stack.peek())


print(stack.pop()) 
print(stack.size()) 


try:
    stack.pop()
except Exception as erorr:
    print(erorr) 
