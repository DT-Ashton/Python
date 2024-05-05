class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=", ")
    in_order_traversal(node.right)

def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=", ")

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print("root:", root.data)
print("Nodes at level 1:", root.left.data, root.right.data)
print("A subtree:", nodeA.data, nodeA.left.data, nodeA.right.data)
print("B subtree:", nodeB.data, nodeB.left.data, nodeB.right.data, nodeB.right.left.data)

print("\npre-order traversal:")
pre_order_traversal(root)
print('\nin-order traversal:')
in_order_traversal(root)
print('\npost-order traversal:')
post_order_traversal(root)
