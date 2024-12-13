# Node of a Singly Linked List
class Node:
    # Constructor
    def __init__(self):
        self.data = None
        self.next = None


    # Method for setting the data field of the node
    def setData(self, data):
        self.data = data

    # Method for getting the data field of the node
    def getData(self):
        return self.data

    # Method for setting the next field of the node
    def setNext(self, next_node):
        self.next = next_node

    # Method for getting the next field of the node
    def getNext(self):
        return self.next

    # Returns True if the node points to another node
    def hasNext(self):
        return self.next is not None
