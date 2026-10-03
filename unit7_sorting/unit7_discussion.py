"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""

def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    """
Sort a list using Bubble Sort.

Bubble Sort compares neighboring values and swaps them
when they are out of order.
"""
    # Create a copy so the original list is not changed.
    sorted_list = lst.copy()

    # Each pass moves the largest remaining value toward the end.
    for i in range(len(sorted_list) - 1):
        swapped = False

        for j in range(len(sorted_list) - 1 - i):

            # Swap neighboring values if they are out of order.
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )
                swapped = True

        # If no swaps occurred, the list is already sorted.
        if not swapped:
            break

    return sorted_list

def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    """
    Sort a list using Merge Sort.

    Merge Sort divides the list into smaller halves,
    recursively sorts each half, and then merges them.
    """

    # Base case: a list with zero or one value is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list.
    middle = len(lst) // 2

    # Divide the list into left and right halves.
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Recursively sort each half.
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves together.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    """
   Merge two sorted lists into one sorted list.
   """

    result = []
    left_index = 0
    right_index = 0

    # Compare values from each list and add the smaller value.
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

        # Add any remaining values from the left list.
        while left_index < len(left):
            result.append(left[left_index])
            left_index += 1

        # Add any remaining values from the right list.
        while right_index < len(right):
            result.append(right[right_index])
            right_index += 1

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    numbers1 = [45, 12, 78, 23, 9, 56, 31]

    print("Original list:   ", numbers1)
    print("Bubble Sort:     ", bubble_sort(numbers1))
    print("Merge Sort:      ", merge_sort(numbers1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    numbers2 = [92, 17, 44, 3, 68, 25, 50, 11]

    print("Original list:   ", numbers2)
    print("Bubble Sort:     ", bubble_sort(numbers2))
    print("Merge Sort:      ", merge_sort(numbers2))

    # Both algorithms should produce the same sorted result.
    print(
        "Same result:     ",
        bubble_sort(numbers2) == merge_sort(numbers2)
    )


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    duplicate_numbers = [30, 10, 30, 20, 10, 40]

    print("\nList with duplicates:")
    print("Original:        ", duplicate_numbers)
    print("Bubble Sort:     ", bubble_sort(duplicate_numbers))
    print("Merge Sort:      ", merge_sort(duplicate_numbers))
    print("Duplicate values are kept and placed in sorted order.")

    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD SORTING EXAMPLE ===")

    # Example: Number of open STIG findings on several systems.
    open_findings = [18, 5, 27, 11, 3, 15, 8]

    print("Open STIG findings:  ", open_findings)
    print("Bubble Sort:         ", bubble_sort(open_findings))
    print("Merge Sort:          ", merge_sort(open_findings))

    print(
        "Sorting finding counts could help an administrator "
        "identify systems based on the number of open findings."
    )


if __name__ == "__main__":
    main()