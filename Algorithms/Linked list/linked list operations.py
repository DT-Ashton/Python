class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def delete_node(head, node_to_delete):
    # if the node to be deleted is the first node, the new head returned will be the next node
    if head == node_to_delete:
        return head.next
    currentNode = head

    while currentNode.next != node_to_delete:
        currentNode = currentNode.next

    # if the node to be deleted is the last node, there is no need to change the link of the previous node
    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next  # change the link to the node after the deleted node
    return head


def insert_node(head, new, position):
    if position == 1:
        new.next = head
        return new

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    new.next = currentNode.next
    currentNode.next = new
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original:")
traverse(node1)

# Delete node4
node1 = delete_node(node1, node4)
print("\nAfter deletion:")
traverse(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insert_node(node1, newNode, 2)
print("\nAfter insertion:")
traverse(node1)
