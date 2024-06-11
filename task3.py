# It's upgraded from task2 and add SUM of all values in tree 

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_largest(self):
        if self.root is None:
            return None
        return self._find_largest(self.root)

    def _find_largest(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.val

    def find_smallest(self):
        if self.root is None:
            return None
        return self._find_smallest(self.root)

    def _find_smallest(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.val

    def sum_values(self):
        if self.root is None:
            return 0
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.val + self._sum_values(node.left) + self._sum_values(node.right)

# Example usage:
bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(5)
bst.insert(15)

print("The largest value in the tree is:", bst.find_largest())
print("The smallest value in the tree is:", bst.find_smallest())
print("The sum of all values in the tree is:", bst.sum_values())
