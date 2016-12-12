class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:      # na prawo
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:    # na lewo
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass    # ignoruję duplikaty

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return False
    def bst_max(self):
        max = -10000
        if(self.left == None) and (self.right == None) and (self.data == None):
            raise ValueError("Puste drzewo")
        if(self.left == None) and (self.right == None):
            max = self.data
        while (self.right != None):
            max = self.right
            self = self.right
        return max
    def bst_min(self):
        min = 10000
        if(self.left == None) and (self.right == None) and (self.data == None):
            raise ValueError("Puste drzewo")
        if(self.left == None) and (self.right == None):
            min = self.data
        while (self.left != None):
            min = self.left
            self = self.left
        return min

root = Node(3,None,None)
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(8)
root.insert(12)
root.insert(-5)
print("Max = " + str(root.bst_max()))
print("Min = " + str(root.bst_min()))

root2 = Node(0,None,None)
root2.insert(150)
root2.insert(234)
root2.insert(-300)
root2.insert(23)
root2.insert(53)
root2.insert(122)
root2.insert(-34)
print("Max = " + str(root2.bst_max()))
print("Min = " + str(root2.bst_min()))