# Binary Search Tree and AVL Tree Operations

This repository contains implementations for various tasks involving binary search trees (BSTs) and AVL trees. The tasks include finding the largest value, the smallest value, and the sum of all values in these trees. Each task is implemented as a separate function in the BST class.

## Tasks Overview

### Task 1: Find the Largest Value in a Tree

**Description**: Write an algorithm that finds the largest value in a binary search tree (BST) or AVL tree.

**Algorithm**: 
- Start from the root node.
- Continuously move to the right child node until a node with no right child is found.
- The value of this node is the largest value in the tree.

**Acceptance Criteria**:
- The function is executed and successfully finds the largest value in the tree.

### Task 2: Find the Smallest Value in a Tree

**Description**: Write an algorithm that finds the smallest value in a binary search tree (BST) or AVL tree.

**Algorithm**: 
- Start from the root node.
- Continuously move to the left child node until a node with no left child is found.
- The value of this node is the smallest value in the tree.

**Acceptance Criteria**:
- The function is executed and successfully finds the smallest value in the tree.

### Task 3: Find the Sum of All Values in a Tree

**Description**: Write an algorithm that finds the sum of all values in a binary search tree (BST) or AVL tree.

**Algorithm**:
- Use a tree traversal method (in-order, pre-order, or post-order) to visit all nodes in the tree.
- Accumulate the values of all visited nodes.
- Return the total sum.

**Acceptance Criteria**:
- The function is executed and successfully calculates the sum of all values in the tree.

# Explanation

**TreeNode Class**: Represents a node in the binary search tree with a value (val) and pointers to the left and right children (left, right).

**BinarySearchTree Class:**
- insert(key): Inserts a key into the BST. If the tree is empty, the key becomes the root. Otherwise, it calls _insert to find the correct spot for the new key.
- _insert(node, key): Recursively finds the correct spot for the new key and inserts it.
- find_largest(): Initiates the process of finding the largest value starting from the root.
- _find_largest(node): Iteratively follows the right child pointers until it finds the node with no right child, which is the largest node.
- find_smallest(): Initiates the process of finding the smallest value starting from the root.
- _find_smallest(node): Iteratively follows the left child pointers until it finds the node with no left child, which is the smallest node.
- sum_values(): Initiates the process of summing all values in the tree starting from the root.
- _sum_values(node): Recursively calculates the sum of all values in the tree using a simple tree traversal method. It adds the value of the current node to the sum of the values of its left and right subtrees.

# Testing Code

To test the implementation, you can use the provided example where we insert multiple values into the BST and then call find_largest(), find_smallest(), and sum_values() to get the largest value, smallest value, and sum of all values, respectively.
