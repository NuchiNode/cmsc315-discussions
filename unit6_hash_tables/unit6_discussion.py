"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Create an empty dictionary to stor server IDs and operating systems.
    servers = {}

    # A Python dictionary behaves like a hash table by using a hash
    # of each key to quickly locate its associated value.
    servers["SRV001"] = "RHEL 9"
    servers["SRV002"] = "Windows Server 2022"
    servers["SRV003"] = "RHEL 8"
    servers["SRV004"] = "Windows Server 2019"
    servers["SRV005"] = "RHEL 7"

    # Prints what was added to or inside the dictionary
    print("\nServer inventory after inserting five servers:")
    print(servers)


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # The server ID is used as the key to directly retrieve
    # the operating system stored as its value.
    print("\nSRV001:", servers["SRV001"])
    print("SRV004:", servers["SRV004"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Prints what is in the dictionary
    print("\nBefore updating an item(s) in the dictionary:")
    print(servers)

    # Assigning a new value to an existing key replaces the old value.
    # Here, SRV003 is upgraded from RHEL 8 to RHEL 9.
    servers["SRV003"] = "RHEL 9"

    print("After updating the dictionary SRV0003 from RHEL 8 to RHEL 9:")
    print(servers)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("\nBefore deleting an item(s) in the dictionary:")
    print(servers)

    # del removes the key and its value from the dictionary.
    # The server ID is hashed to find its location, and that entry is removed.
    del servers["SRV005"]
    print("After deleting the dictionary SRV005 from the original servers:")
    print(servers)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1:
    # The get() method searches for a key.
    # If the key does not exist, the provided default value is returned
    # instead of causing a KeyError.
    missing_server = servers.get("SRV700", "Server not found")
    print("\nSearching for SRV700:", missing_server)

    # Edge Case 2:
    # The pop() method attempt to remove a missing key when
    # a default value is provided. This prevents a KeyError.
    removed_server = servers.pop("SRV700", "Server not found")
    print("Attempting to delete SRV700:", removed_server)

    print("Final server inventory:")
    print(servers)

if __name__ == "__main__":
    main()