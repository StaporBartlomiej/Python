class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie
    @staticmethod
    def find_max(node):
        if(Node == None):
            raise ValueError("Node is none")
        max = node.data
        while node:
            if(max < node.data):
                max = node.data
            if (node.next == None):
                break
            else:
                node = node.next
        return max
    @staticmethod
    def find_min(node):
        if (Node == None):
            raise ValueError("Node is none")
        min = node.data
        while node:
            if(min > node.data):
                min = node.data
            if(node.next == None):
                break
            else:
                node = node.next
        return min
    def print_list(node):
        while node:
            print(node)
            node = node.next

head = None;
head = Node(3,head)
head = Node(2,head)
head = Node(4,head)
Node.print_list(head)
print("Max = " + str(Node.find_max(head)) + "\nMin = " + str(Node.find_min(head)))

print("")
head = Node(3,head)
head = Node(32,head)
head = Node(21,head)
head = Node(-8,head)
head = Node(-25,head)
head = Node(0,head)
Node.print_list(head)

print("Max = " + str(Node.find_max(head)) + "\nMin = " + str(Node.find_min(head)))





