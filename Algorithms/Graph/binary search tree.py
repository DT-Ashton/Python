class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node

def delete(node, data):
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Node with only one child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        # Node with two children, get the in-order successor
        node.data = min_value(node.right).data
        node.right = delete(node.right, node.data)

    return node

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=", ")
    in_order_traversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# test:
print('Original:')
in_order_traversal(root)

print('\nAfter insert:')
insert(root, 10)
in_order_traversal(root)

print("\nAfter delete:")
delete(root, 3)
in_order_traversal(root)

result = search(root, 8)
if result:
    print(f"\nFound the node with value: {result.data}")
else:
    print("\nValue not found in the BST.")

print("Lowest value:", min_value(root).data)
