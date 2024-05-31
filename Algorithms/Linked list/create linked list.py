class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("null")

    def insert_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, value):
        new_node = Node(value)
        if self.head is None:
            print('Set new head !')
            self.head = new_node
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node

    def insert_after(self, previous_node, value):
        previous_node = self.search(previous_node)
        if previous_node is None:
            print(f'The node is not in LinkedList!')
            return
        new_node = Node(value)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def delete_first(self):

        if self.head is None:
            print('There is no Node to delete !')
            return

        t = self.head
        self.head = self.head.next
        t = None

    def delete_last(self):

        if self.head is None:
            print('There is no Node to delete !')
            return

        if self.head.next is None:
            print('The LinkedList is empty now !')
            self.head = None
            return

        tmp = self.head
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None

    def delete_by_value(self, value):
        temp = self.head
        if temp.data == value:
            self.head = self.head.next
            temp = None
            return

        prev_node = temp
        while temp:
            if temp.data == value:
                break
            prev_node = temp
            temp = temp.next
        if temp is None:
            print('There is no link to delete!')
            return
        prev_node.next = temp.next
        temp = None

    def search(self, value):
        currentNode = self.head
        while currentNode:
            if currentNode.data == value:
                return currentNode
            else:
                currentNode = currentNode.next
        print("Not found!")
        return None

    def update(self, node, new_value):
        node = self.search(node)
        if node is None:
            print('There is no Node to update !')
            return
        node.data = new_value

linked_list = LinkedList()
linked_list.insert_first(1)
linked_list.insert_last(2)
linked_list.insert_last(3)
linked_list.insert_after(1, 'hello')
linked_list.insert_first(0)
linked_list.insert_after(2, 'haha')
linked_list.traverse()

print("\nAfter deletion:")
linked_list.delete_first()
linked_list.delete_last()
linked_list.delete_by_value('haha')
linked_list.traverse()

print("\nAfter update:")
linked_list.update('hello', '10')
linked_list.traverse()
