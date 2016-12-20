class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if(self.size == self.n):
            raise Exception("Przepełniony stos")
        self.items[self.n] = data
        self.n = self.n + 1

    def pop(self):
        if(self.n == 0):
            raise Exception("Pusty stos")
        self.n = self.n - 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

x = Stack(4)
x.push(1)
x.push(2)
x.push(3)
x.push(4)

y = Stack(0)

try:
    y.push(1)
except Exception as ex:
    print(ex.args[0])