class Cat:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, name):
        self.name = name

class AnimalShelter:
    catQueue = []
    dogQueue = []
    timestamp = 0 # the smaller the timestamp, the older

    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.catQueue.append([animal, self.timestamp])

        if isinstance(animal, Dog):
            self.dogQueue.append([animal, self.timestamp])

        self.timestamp = self.timestamp + 1

    def dequeueDog(self):
        if self.dogQueue:
            return self.dogQueue.pop()[0]
        else:
            return None

    def dequeueCat(self):
        if self.catQueue:
            return self.catQueue.pop()[0]
        else:
            return None

    def dequeueAny(self):
        if not self.dogQueue:
            return self.dequeueCat()
        else:
            if not self.catQueue:
                return self.dequeueDog()
            else:
                if self.catQueue[-1] < self.dogQueue[-1]:
                    return self.dequeueCat()
                else:
                    return self.dequeuDog()

ans = AnimalShelter()
assert(ans.dequeueDog() == None)
assert(ans.dequeueAny() == None)
assert(ans.dequeueCat() == None)

ans.enqueue(Cat('first'))
assert(ans.dequeueDog() == None)
assert(ans.dequeueAny().name == 'first')
ans.enqueue(Cat('first'))
assert(ans.dequeueCat().name == 'first')

ans.enqueue(Cat('first'))
ans.enqueue(Dog('second'))
assert(ans.dequeueDog().name == 'second')
assert(ans.dequeueAny().name == 'first')

ans.enqueue(Cat('third'))
