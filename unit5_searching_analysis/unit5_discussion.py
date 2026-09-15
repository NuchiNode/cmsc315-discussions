"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Check each item in the list one at a time,
    # starting at index 0.
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Initialize low to the first index of the list.
    low = 0
    # Initialize high to the last index of the list.
    high = len(lst) - 1

    while low <= high:
        # Find the middle index of the current search area.
        mid = (low + high) // 2

        # If the target is larger than the middle value,
        # search only the right half of the list.
        if lst[mid] < target:
            low = mid + 1

        # If the target is smaller than the middle value,
        # search only the left half of the list.
        elif lst[mid] > target:
            high = mid - 1

        # The target was found at the middle of the list.
        else:
            return mid

    # Returns -1 if the target is not in the list.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Search for a value that exists.
    # Both searches return index 3
    small_dataset = [15, 20, 25, 30, 35]
    print("\nSmall dataset values:", small_dataset)
    print("Linear Search - The target 30 is located at index:", linear_search(small_dataset, 30))
    print("Binary Search - The target 30 is located at index:", binary_search(small_dataset, 30))

    # Search for a value that does not exist
    # Both searches return -1
    print("Linear Search - The target 100 does not exist:", linear_search(small_dataset, 100))
    print("Binary Search - The target 100 does not exist:", binary_search(small_dataset, 100))


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Initialized a large dataset containing numbers from 1 to 3499.
    large_dataset = list(range(1, 3500))
    print("\nLarge dataset values: 1 - 3499")

    # Linear search may need to check thousands of values
    # sequentially before reaching the target value.
    print("Linear Search - The target 3210 is located at index:", linear_search(large_dataset, 3210))

    # Binary search eliminates half of the remaining search area
    # during each iteration, making it more efficient on large datasets.
    print("Binary Search - The target 3210 is located at index:", binary_search(large_dataset, 3210))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1
    # An empty list contains no values. Both searches will return -1.
    empty_list = []
    print("\nEmpty list has value:", empty_list)
    print("Linear Search - The target 10 on an empty list returns:", linear_search(empty_list, 10))
    print("Binary Search - The target 10 on an empty list returns:", binary_search(empty_list, 10))

    # Edge case 2
    # A single-element list only has one possible location to check.
    single_element = [35]
    print("\nSingle element is:", single_element)
    print("Linear Search - The target 35 is located at index:", linear_search(single_element, 35))
    print("Binary Search - The target 35 is located at index:", binary_search(single_element, 35))

    # Edge case 3
    # Test values located at the first and last positions of the list.
    # Both searches return index 0 for 20 and index 3 for 50.
    edge_list = [20, 30, 40, 50]
    print("\nNew list has values:", edge_list)
    print("Linear Search - The target value 20 at first position:", linear_search(edge_list, 20))
    print("Binary Search - The target value 20 at first position:", binary_search(edge_list, 20))
    print("Linear Search - The target value 50 at last position:", linear_search(edge_list, 50))
    print("Binary Search - The target value 50 at last position:", binary_search(edge_list, 50))

if __name__ == "__main__":
    main()