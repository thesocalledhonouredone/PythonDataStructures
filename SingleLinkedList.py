class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, someData):
        newNode = Node(someData)
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def printList(self):
        currentNode = self.head.next
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next
        print("End of List")

    def lengthOfList(self):
        len = 0
        currentNode = self.head.next
        while currentNode:
            len += 1
            currentNode = currentNode.next
        print("Length of List: ", len)

    def visualizeList(self):
        currentNode = self.head.next
        while currentNode:
            print(currentNode.data, " -> ", end="")
            currentNode = currentNode.next
        print("END")

    def isEmpty(self):
        if self.head.next == None:
            print("List is Empty")
        else:
            print("List is NOT Empty")

    def reverseList(self):
        reverse = []
        currentNode = self.head.next
        while currentNode:
            reverse.append(currentNode.data)
            currentNode = currentNode.next

        print("Reversed List: ")
        reverse.reverse()
        for i in reverse:
            print(i)

    

