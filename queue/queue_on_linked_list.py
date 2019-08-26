class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.tail:
            self.tail.next = node

        self.tail = node

        if not self.head:
            self.head = self.tail

    def remove(self):
        if not self.head:
            return None

        temp = self.head
        self.head = self.head.next

        if not self.head:
            self.last = None

        return temp.data

    def peek(self):
        if not self.head:
            return None

        return self.head.data

    def is_empty(self):
        return bool(self.head)
