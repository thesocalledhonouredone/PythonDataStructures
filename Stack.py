class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __del__(self):
        print(end="")


class Stack:
    def __init__(self):
        self.top = None

    def push(self, number):
        new_node = Node(number)
        temp_node = self.top
        self.top = new_node
        new_node.next = temp_node

    def pushes(self, *values_to_push):
        for i in values_to_push:
            self.push(i)

    def peek(self):
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def pop(self):
        current_node = self.top
        self.top = current_node.next
        current_node.__del__()

    def pops(self, number_of_pops):
        for i in range(number_of_pops):
            current_node = self.top
            self.top = current_node.next
            current_node.__del__()

