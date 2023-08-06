class LinkedList:
    head = None
    length = 0

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            self.length += 1
            return element

        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)
        self.length += 1

    def insert(self, index, element):
        i = 0
        node = self.head
        prev_node = self.head

        if index == 0:
            temp_node = self.head
            self.head = self.Node(element, next_node=temp_node)
        else:

            while i < index:
                prev_node = node
                node = node.next_node
                i += 1

            prev_node.next_node = self.Node(element, next_node=node)
        self.length += 1

    def delete(self, index):
        i = 0
        node = self.head
        prev_node = self.head

        if index == 0:
            self.head = node.next_node
            print(node.element)
            self.length -= 1

        else:
            while i < index:
                prev_node = node
                node = node.next_node
                i += 1

            prev_node.next_node = node.next_node
            print(node.element)
            self.length -= 1

    def assign(self, index, element):
        i = 0
        node = self.head

        while i < index:
            node = node.next_node
            i += 1

        node.element = element

    def get(self, index):
        i = 0
        node = self.head

        while i < index:
            node = node.next_node
            i += 1

        print(node.element)

    def get_len(self):
        if not self.head:
            return 0

        i = 1
        node = self.head
        while node.next_node:
            i += 1
            node = node.next_node

        return i

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)


