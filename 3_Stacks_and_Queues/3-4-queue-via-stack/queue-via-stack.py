class Queue:
    newStack = []
    oldStack = []

    def enqueue(self, item):
        self.newStack.append(item)

    def dequeue(self):
        while self.newStack:
            self.oldStack.append(self.newStack.pop())

        if self.oldStack:
            return self.oldStack.pop()
        else:
            return None

    def peek(self):
        while self.newStack:
            self.oldStack.append(self.newStack.pop())

        if self.oldStack:
            return self.oldStack[-1]
        else:
            return None

queue = Queue()
assert(queue.dequeue() == None)
queue.enqueue(1)
assert(queue.dequeue() == 1)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
assert(queue.peek() == 1)
assert(queue.dequeue() == 1)
assert(queue.peek() == 2)
assert(queue.dequeue() == 2)
assert(queue.peek() == 3)
assert(queue.dequeue() == 3)
