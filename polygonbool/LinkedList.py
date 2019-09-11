class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

    def __eq__(self, other):
        if self.data == other.data:
            return True
        return False


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def __getitem__(self, item):
        curr = self.head
        for i in range(item):
            curr = curr.next
        return curr

    def __setitem__(self, key, value):
        if key == 0:
            self.head = Node(data=value, next=self.head.next)
            return
        prev = self.head
        for i in range(key - 1):
            prev = prev.next
        prev.next = Node(data=value, next=prev.next.next)

    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def prepend(self, data):
        self.head = Node(data=data, next=self.head)

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def find(self, data):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        return curr

    def insert(self, data, prev):
        if self.find(prev):
            prev = self.find(prev)
            node = Node(data=data, next=prev.next)
            prev.next = node

    def remove(self, data):
        curr = self.head
        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def is_empty(self):
        if self.head is not None:
            return True
        return False
