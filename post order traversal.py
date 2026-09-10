# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Postorder traversal function
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create the binary tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)

# Perform postorder traversal
postorder(root)