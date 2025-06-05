class binary_tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branch_bums(root):
    if root is None:
        return 0
    
    total = 0

    
    if root.right and not root.right.left and not root.right.right:
        total += root.right.value
    
     
    total += branch_bums(root.left)
    total += branch_bums(root.right)
    
    return total

"""
    3
   / \
  9  20
    /  \
   15   7
"""
root = binary_tree(3)
root.left = binary_tree(9)
root.right = binary_tree(20)
root.right.left = binary_tree(15)
root.right.right = binary_tree(7)

print(branch_bums(root))  