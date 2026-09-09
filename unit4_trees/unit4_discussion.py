"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Each node stores a value and references to its left and right children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # An empty BST does not have a root node,
        # so the root starts as None.

        # An empty BST does not have a root node, so the root starts as None.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Smaller values are assigned to the left side of the node.
        # Larger values are assigned to the right side of the node.
        # This ordering makes BST searching more efficient.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
     TODO (Student):
     Implement recursive BST insertion.

     Requirements:
     - Create a new node when a position is found.
     - Insert smaller values into the left subtree.
     - Insert larger values into the right subtree.
     - Return the updated node reference.
     """

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
        """
       TODO (Student):
       Search for a value in the BST.

       Requirements:
       - Return True if found.
       - Return False if not found.
       - Add comments explaining why BST search is often
         more efficient than linear search.
       """

        # A BST can search faster than a linear structure
        # because each comparison tells whether to go left
        # or right instead of checking every value.
        return self._search_recursive(self.root, value)


    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

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
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        """Return the BST values using in-order traversal."""

        # Create an empty list that will hold the values
        # as the tree is traversed.
        values = []

        # Start the recursive traversal at the root.
        self._inorder_recursive(self.root, values)

        # Return the completed list.
        return values

    def _inorder_recursive(self, node, values):
        """
       TODO (Student):
       Implement in-order traversal.

       Requirements:
       - Visit the left subtree.
       - Visit the current node.
       - Visit the right subtree.
       - Add comments explaining why this traversal
         produces sorted output in a BST.
       """

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

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    tree = BST()

    values = [45, 70, 15, 60, 25, 50, 30]

    print("Values inserted into the BST:", values)

    for value in values:
        tree.insert(value)

    # A BST reduces the search space because each comparison
    # determines whether the value could be on the
    # left or right side of the current node.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    traversal = tree.inorder()

    print("In-order traversal:", traversal)

    # In-order traversal visits the left subtree first,
    # then the current node, and then the right subtree.
    # Since smaller BST values are stored on the left and
    # larger values are stored on the right, the result is sorted.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # These values exist in the tree.
    print("Search for 30:", tree.search(30))
    print("Search for 70:", tree.search(70))

    # These values do not exist in the tree.
    # The searches eventually reach None and return False.
    print("Search for 35:", tree.search(35))
    print("Search for 7:", tree.search(7))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    empty_tree = BST()

    # Traversing an empty tree returns an empty list because
    # there are no nodes to visit.
    print("Empty tree traversal:", empty_tree.inorder())

    # Searching an empty tree returns False.
    print("Search empty tree for 10:", empty_tree.search(10))

    # This BST implementation does not allow duplicate values.
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