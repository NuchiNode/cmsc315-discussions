"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================
"""

class Node:
    def __init__(self, value):
        # Each node stores a value and references to its left and right children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty BST does not have a root node, so the root starts as None.
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""

        # Smaller values are assigned to the left side of the node.
        # Larger values are assigned to the right side of the node.
        # This ordering makes BST searching more efficient.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursive helper method for inserting a value."""

        # If there is no node here, this is where
        # the new value should be inserted.
        if node is None:
            return Node(value)

        # Smaller values are placed in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values are placed in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # If the value is equal, nothing is inserted.
        return node

    def search(self, value):
        """Search for a value in the BST."""

        # A BST can search faster than a linear structure
        # because each comparison tells whether to go left
        # or right instead of checking every value.
        return self._search_recursive(self.root, value)


    def _search_recursive(self, node, value):
        """Recursive helper method for BST searching."""

        # Reaching None means the value was not found.
        if node is None:
            return False

        # The value was found at the current node.
        if value == node.value:
            return True

        # If the value is smaller, only search the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # If the value is larger, only search the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """Return the BST values using in-order traversal."""

        # Create an empty list that will hold the values
        # as the tree is traversed.
        values = []

        # Start the recursive traversal at the root.
        self._inorder_recursive(self.root, values)

        # Return the completed list.
        return values

    def _inorder_recursive(self, node, values):
        """Recursive helper method for in-order traversal."""

        if node is not None:
            # First visit all smaller values in the left subtree.
            self._inorder_recursive(node.left, values)

            # Then visit the current node.
            values.append(node.value)

            # Visit the larger values in the right subtree.
            self._inorder_recursive(node.right, values)



def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()

    values = [45,70, 15, 60, 25, 50, 30]

    print("Values inserted into the BST:", values)

    for value in values:
        tree.insert(value)

    # A BST reduces the search because each comparison
    # determines whether the next value could only be on the
    # left or right side of the current node.

    print("\n=== IN-ORDER TRAVERSAL ===")
    traversal = tree.inorder()

    print("In-order traversal:", traversal)

    # In-order traversal visits the left subtree first,
    # then the current node, and the right subtree.
    # Since smaller BST values are stored on the left and
    # larger values are stored on the right, the result is sorted.

    print("\n=== SEARCH TESTS ===")
    # Values that exist in the tree.
    print("Search for 30:", tree.search(30))
    print("Search for 70:", tree.search(70))

    # These values do not exist int the tree,
    # The search reaches None and return False.
    print("Search for 35:", tree.search(35))
    print("Search for 7:", tree.search(7))

    print("\n=== EDGE CASES ===")
    empty_tree = BST()

    # Traversing an empty tree returns an empty list because
    # there are no nodes to visit.
    print("Empty tree traversal:", empty_tree.inorder())

    # Searching an empty tree returns False.
    print("Search empty tree for 10:", empty_tree.search(10))

    # This tree does not allow duplicate values.
    # Inserting 50 again does not create another node.
    tree.insert(50)
    print("After inserting duplicate 50:", tree.inorder())

    # ===============================
    # REAL-WORLD BST EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD BST EXAMPLE ===")

    # In an environment with many server IDs, a BST can find
    # a value with fewer comparisons than scanning the entire list.
    server_tree = BST()

    server_ids = [105, 102, 108, 101, 103, 107, 110]

    for server_id in server_ids:
        server_tree.insert(server_id)

    print("Server IDs in-order:", server_tree.inorder())
    print("Does server ID 107 exist?", server_tree.search(107))
    print("Does server ID 115 exist?", server_tree.search(115))

if __name__ == "__main__":
    main()