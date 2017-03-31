class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.set_of_stacks = [[]]
        self.current_stack = 0

    def push(self, item):
        if len(self.set_of_stacks[self.current_stack]) < self.threshold:
            self.set_of_stacks[self.current_stack].append(item)
        else:
            self.current_stack = self.current_stack + 1
            self.set_of_stacks.append([item])

    def pop(self):
        if self.set_of_stacks[self.current_stack]:
            return self.set_of_stacks[self.current_stack].pop()
        else:
            if self.current_stack > 0:
                self.set_of_stacks.pop()
                self.current_stack = self.current_stack - 1
                return self.set_of_stacks[self.current_stack].pop()
            else:
                return None

stack = SetOfStacks(2)
assert(stack.pop() == None)
stack.push(1)
stack.push(2)
stack.push(3)
assert(stack.pop() == 3)
assert(stack.pop() == 2)
assert(stack.pop() == 1)
assert(stack.pop() == None)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
assert(stack.pop() == 5)
assert(stack.pop() == 4)
assert(stack.pop() == 3)
assert(stack.pop() == 2)
assert(stack.pop() == 1)
assert(stack.pop() == None)
