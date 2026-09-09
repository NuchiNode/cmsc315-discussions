# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduced Binary Search Trees (BSTs) and recursive tree operations. I built a BST that stored values 
using left and right child references and used recursion to insert, search, and traverse the tree.

The BST followed the rule that smaller values were stored in the left subtree and larger values were stored in the right
subtree. This ordering helped reduce the search space because each comparison determined which side of the tree needed 
to be searched next.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

In earlier units, I used loops for most list operations, so writing methods that call a helper and return a node 
reference took some getting used to. What made sense was realizing that insert has to assign the helper's return value 
back to the parent's left or right, or the new node never attaches to the tree.

A challenge that I faced was in-order traversal. The recursive helper worked, but the wrapper method was still empty, so
every traversal printed None. Once I created a list in the wrapper and passed it into the recursive calls, all the nodes
appended to the same list and the output came back sorted.

A BST is efficient because of its ordering rule. Each comparison tells me which subtree a value could be in, which can 
reduce the number of values that need to be searched. Searching a linear list can have a runtime complexity of O(N), 
meaning elements may need to be checked one at a time until a match is found. Balance is key. If I inserted server IDs 
in sorted order, every node would chain to the right and the tree would behave more like a linked list.