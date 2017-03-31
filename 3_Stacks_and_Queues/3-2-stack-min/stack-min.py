import sys

class MinStack:
    globalMin = sys.maxint
    actualStack = []
    minStack = []

    def push(self, item):
        if item < self.globalMin:
            self.globalMin = item

        self.actualStack.append(item)
        self.minStack.append(self.globalMin)

    def pop(self):
        if not self.minStack:
            return None

        self.minStack.pop()
        if self.minStack:
            self.globalMin = self.minStack[-1]
        else:
            self.globalMin = sys.maxint
        return self.actualStack.pop()

    def min(self):
        if not self.minStack:
            return None

        return self.minStack[-1]

minStack = MinStack()
assert(minStack.pop() == None)
assert(minStack.min() == None)
minStack.push(100)
assert(minStack.min() == 100)
minStack.pop()
assert(minStack.pop() == None)
assert(minStack.min() == None)
minStack.push(100)
assert(minStack.min() == 100)
minStack.push(10)
assert(minStack.min() == 10)
minStack.pop()
assert(minStack.min() == 100)
minStack.pop()
assert(minStack.min() == None)
