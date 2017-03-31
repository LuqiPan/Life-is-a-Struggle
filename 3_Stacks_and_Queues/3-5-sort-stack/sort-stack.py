class SortStack:
    tempStack = []
    stack = []

    def is_empty(self):
        return len(self.stack + self.tempStack) == 0

    def peek(self):
        while self.tempStack:
            self.stack.append(self.tempStack.pop())

        if stack:
            return self.stack[-1]
        else:
            return None

    def pop(self):
        while self.tempStack:
            self.stack.append(self.tempStack.pop())

        if self.stack:
            return self.stack.pop()
        else:
            return None

    def push(self, item):
        while self.stack and item > self.stack[-1]:
            self.tempStack.append(self.stack.pop())

        while self.tempStack and item < self.tempStack[-1]:
            self.stack.append(self.tempStack.pop())

        self.stack.append(item)

ss = SortStack()
assert(ss.is_empty())
ss.push(4)
ss.push(1)
ss.push(3)
ss.push(2)
assert(ss.pop() == 1)
assert(ss.pop() == 2)
assert(ss.pop() == 3)
assert(ss.pop() == 4)
