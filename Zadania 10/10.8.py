from random import choice


class RandomQueue:
    def __init__(self, size=0):
        self.size = size
        self.queue = size * [None]
        self.clear = []
        self.full = []
        for i in range(0, size):
            self.clear.append(i)

    def insert(self, item):
        if self.is_full():
            raise Exception("Kolejka jest pelna")
        i = self.clear.pop()
        self.full.append(i)
        self.queue[i] = item


    def remove(self):
        if self.is_empty():
            raise Exception("Kolejka jest pusta")
        random_index = choice(self.full)
        element = self.queue[random_index]
        last_used = self.full.pop()
        self.queue[random_index] = self.queue[last_used]
        self.queue[last_used] = None
        self.clear.append(random_index)
        return element

    def is_empty(self):
        if (len(self.clear) == self.size):
            return True
        else:
            return False

    def is_full(self):
        if (len(self.full) == self.size):
            return True
        else:
            return False



a = RandomQueue(6)
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
print(a.remove())
print(a.remove())
a.insert(7)
print(a.remove())