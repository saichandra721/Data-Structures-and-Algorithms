from ListNode import Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = self.listLength() if head else 0

    # Traversing the Linked List
    def listLength(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    # Method for inserting a new node at the beginning of the Linked List (at the head)
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    # Method for inserting a new node at the end of a Linked List
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(newNode)
        self.length += 1

    # Method for inserting a new node at any position in a Linked List
    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            elif pos == self.length:
                self.insertAtEnd(data)
            else:
                newNode = Node()
                newNode.setData(data)
                count = 0
                current = self.head
                while count < pos - 1:
                    count += 1
                    current = current.getNext()
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1

    # Method to delete the first node of the linked list
    def deleteFromBeginning(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1

    # Method to delete the last node of the linked list
    def deleteLastNode(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = None
            while currentnode.getNext() is not None:
                previousnode = currentnode
                currentnode = currentnode.getNext()
            if previousnode is None:
                # Only one node in the list
                self.head = None
            else:
                previousnode.setNext(None)
            self.length -= 1

    # Delete a specific node from the linked list
    def deleteNode(self, node):
        if self.length == 0:
            raise ValueError("List is empty")
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in Linked List")
                else:
                    previous = current
                    current = current.getNext()
            if previous is None:
                # Node to be deleted is the head
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            self.length -= 1

    # Delete a node by value from the linked list
    def deleteValue(self, value):
        currentnode = self.head
        previousnode = None
        while currentnode is not None:
            if currentnode.data == value:
                if previousnode is None:
                    # Deleting the head
                    self.head = currentnode.getNext()
                else:
                    previousnode.setNext(currentnode.getNext())
                self.length -= 1
                return
            previousnode = currentnode
            currentnode = currentnode.getNext()
        print("The value provided is not present")

    # Method to delete a node at a particular position
    def deleteAtPosition(self, pos):
        if pos < 0 or pos >= self.length:
            print("Invalid position")
            return
        count = 0
        current = self.head
        previous = None
        while count < pos:
            count += 1
            previous = current
            current = current.getNext()
        if previous is None:
            # Deleting the head
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1
