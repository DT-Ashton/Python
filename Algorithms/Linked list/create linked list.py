class Node:  # Creating doubly circular linked lists
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1  # Used for circular linked lists

node4.previous = node3
node3.previous = node2
node2.previous = node1
node1.previous = node4  # Used for circular linked lists

print("Traversing forward:")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:  # stop so that it only goes through the list one time, or it will be infinite loop :))
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("...")  # Indicating it's circular

print("\nTraversing backward:")
currentNode = node4
startNode = node4
print(currentNode.data, end=" -> ")
currentNode = currentNode.previous

while currentNode != startNode:  # stop so that it only goes through the list one time, or it will be infinite loop :))
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.previous
print("...")  # Indicating it's circular
