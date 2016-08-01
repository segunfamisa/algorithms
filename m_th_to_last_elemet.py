
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = data

    def __str__(self):
        return str(self.data)


def Solution():
    m = int(input(''))
    numbers = int(raw_input('').split(' '))
