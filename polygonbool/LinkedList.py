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