class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if(self.is_full()):
            raise Exception("Pelna kolejka")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if(self.is_empty()):
            raise Exception("Pusta kolejka")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data



x = Queue(4)
x.put(1)
x.put(2)
x.put(3)
x.put(4)

y = Queue(0)

try:
    y.put(5)
except Exception as ex:
    print(ex.args[0])