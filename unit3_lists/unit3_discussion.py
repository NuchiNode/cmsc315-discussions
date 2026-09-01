"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """Insert a value at the specified index."""

    # Everything at this index and after has to shift right.
    # Nothing is overwritten because the list grows.
    # Where I insert the item affects how much work Python has to do.
    # Adding near the beginning moves more items than adding near the end.
    lst.insert(index, value)


def delete_at(lst, index):
    """Remove and return the value at the specified index. Returns None if invalid."""

    # Check the index first so pop() does not crash with an IndexError.
    # I also reject negative indexes because -1 is valid in Python and
    # would remove the last item instead of being treated as invalid.
    if index < 0 or index >= len(lst):
        return None

    # pop removes the item, returns it and shift items to the left.
    return lst.pop(index)


def search_value(lst, value):
    """Return the index of value, or -1 if it is not present."""

    # Linear search checks each item in order until it finds a match.
    # In the worst case, it has to check the entire list, which is O(n).
    for i, item in enumerate(lst):
        if item == value:
            return i

    # Return -1 when the value is not found
    return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")
    print("\n=== INSERTION TESTS ===")

    # Using another example connecting to system administartor's backgroud
    servers = ["web01", "web02", "db01", "app01"]
    print("Original list:", servers)

    # Insert value at the beginning of the list. All items are moved to the right.
    # Value at index 2 (web02) becomes index 3 and the rest shift right.
    insert_at(servers, 0, "fw01")
    print("\nValue inserted at the beginning:", servers)
    insert_at(servers, 2, "web03")
    print("Value inserted in the middle:   ", servers)

    # Insert at the end using len() as the next open index.
    # Existing items do not need to shift.
    insert_at(servers, len(servers), "client01")
    print("Value inserted at the end:      ", servers)

    print("\n=== DELETION TESTS ===")

    # Removed value at the beginning of the list and created a varible for the print().
    remove_beginning = delete_at(servers, 0)
    print("First value removed:", remove_beginning)
    print("Updated list:", servers)

    # Find the middle index and remove that item.
    remove_middle = len(servers) // 2
    removed = delete_at(servers, remove_middle)
    print("Middle value removed:", remove_middle)
    print("Updated list:", servers)

    # Remove the last item. The last valid index is len(servers) - 1
    remove_last = len(servers) - 1
    remove = delete_at (servers, remove_last)
    print("Last value removed:", remove_last)
    print("Updated list:", servers)

    print("\n=== SEARCH TESTS ===")

    # Print the list first because the earlier deletion tests changed it.
    print("Searching current list:", servers)

    # Use one variable for a value that should be found
    # and another for a value that should not be found.

    # Search for a value that exist.
    search_found = search_value(servers, "web02")
    print("Search for 'web02' value returned:", search_found)

    # Search for a value that does not exist.
    search_missing = search_value(servers, "app02")
    print("Search for 'app02' value returned:", search_missing)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")
    # Create an empty list to use for the edge case tests.
    new_list = []
    print("Empty list:", new_list)

    # Insert a value into the created empty list.
    insert_at(new_list, 0, "dc01")
    print("Value inserted at the beginning:", new_list)

    # Try to delete an index that does not exist.
    result = delete_at(new_list, 5)
    print("Deleting index 5, value returned:",result)

    new_list.clear()
    new_result = delete_at(new_list, 0)
    print("Deleting index 0, value returned:",new_result)

    new_result = search_value(new_list, "dc01")
    print("Search for 'dc01' value returned:", new_result)

    # ===============================
    # TODO REAL-WORLD SCENARIO
    # ===============================
    print("\n=== REAL-WORLD SCENARIO: STIG REMEDIATION LIST ===")

    # Open STIG findings waiting to be fixed.
    # Their order represents the current remediation priority.
    findings = ["web02: V-260469","app01: V-260471","db01: V-260478",]

    # Prints the current list.
    print("Open findings:", findings)

    # A higher-priority CAT I finding is placed at the front of the list.
    insert_at(findings, 0, "dc01: V-260453 (CAT I)")
    print("CAT I moved to the front:", findings)

    # Search for a specific finding before closing it.
    position = search_value(findings, "db01: V-260478")
    print("Located db01 finding at index", position)

    # Remove the finding after remediation is complete.
    # delete_at returns the removed value so I can show what was closed.
    closed = delete_at(findings, position)
    print("Closed", closed)
    print("\nRemaining findings:", findings)

    # Try to close the same finding again.
    # search_value returns -1 and delete_at rejects negative indexes.
    # Without that check, -1 would remove the last item in the list.
    position = search_value(findings, "db01: V-260478")
    print("Search for the closed finding: ", position)
    print("Attempt to close it again:", delete_at(findings, position))

if __name__ == "__main__":
    main()