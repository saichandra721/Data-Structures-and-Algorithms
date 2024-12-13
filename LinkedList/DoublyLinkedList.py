class Node:
    # If data is not given by the user, it's taken as None
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

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

    # Returns true if the node points to another node
    def hasNext(self):
        return self.next is not None

    # Method for setting the previous field of the node
    def setPrev(self, prev_node):
        self.prev = prev_node

    # Method for getting the previous field of the node
    def getPrev(self):
        return self.prev

    # Returns true if the node points to another node
    def hasPrev(self):
        return self.prev is not None

    # str returns string equivalent of the object
    def __str__(self):
        return "Node(Data = %s)" % (self.data,)
