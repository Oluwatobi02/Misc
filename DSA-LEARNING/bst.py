import matplotlib.pyplot as plt
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def insert(root, val):
    if root is None:
        return Node(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
    return root
        

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)
root = Node(10)
for i in range(1, 21):
    root = insert(root, i)

def plot_tree(node, x, y, dx, dy):
    if node is not None:
        plt.text(x, y, str(node.val), style='italic', ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))
        if node.left is not None:
            plt.plot([x, x-dx], [y-dy, y-20], 'bo-')
            plot_tree(node.left, x-dx, y-20, dx/2, dy)
        if node.right is not None:
            plt.plot([x, x+dx], [y-dy, y-20], 'bo-')
            plot_tree(node.right, x+dx, y-20, dx/2, dy)

def visualize_tree(root):
    plt.figure(figsize=(10, 10))
    plot_tree(root, 0, 0, 50, 50)
    plt.axis('off')
    plt.show()



def invert(root):
    if root:
        left = root.left
        right = root.right
        root.right = left
        root.left = right
        invert(root.left)
        invert(root.right)
invert(root)
visualize_tree(root)



