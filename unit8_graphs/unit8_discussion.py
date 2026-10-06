"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    """
    Perform Breadth-First Search (BFS) starting from a selected node.
    """

    # If the staring node is not in the graph, return an empty list.
    if start not in graph:
        return []

    # Keep track of nodes that have been visited.
    # This prevents BFS from repeatedly visiting the same node.
    visited = set()

    # Store the order that the nodes are visited
    traversal_order = []

    # BFS uses a queue because it works First-In, First-Out (FIFO).
    # This makes the nodes that were found first get checked first
    # and allows BFS to move through the graph level by level.
    queue = deque([start])

    # Mark the starting node as visited.
    visited.add(start)

    while queue:
        # Remove the first node from the queue.
        current = queue.popleft()

        # Add the current node to the traversal order.
        traversal_order.append(current)

        # Check all the neighbors connected to the current node.
        for  neighbor in graph[current]:
            if neighbor not in visited:
                # Mark the neighbor as visited so it is not added again.
                visited.add(neighbor)

                # Neighbors are added to the queue so BFS can come back
                # and check their connections after the current level.
                queue.append(neighbor)


    # BFS is different from depth-first search because BFS checks
    # nearby nodes first. Depth-first search follows one path as far
    # as it can before going back and checking another path.

    return traversal_order

def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # I used a small computer network for my graph.
    # Each node represents a network device and each edge represents
    # a direct connection between two devices.

    graph = {"Router": ["Switch1", "Switch2"],
             "Switch1": ["Router", "Server1", "Server2"],
             "Switch2": ["Router", "Server3"],
             "Server1": ["Switch1"],
             "Server2": ["Switch1"],
             "Server3": ["Switch2"]
             }

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # Print each device and its direct connections.
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    # Starting from the Router, BFS first checks the Router.
    # It then checks Switch1 and Switch2 because they are directly
    # connected to the Router. After that, it moves to the servers
    # connected to those switches. This shows how BFS moves through
    # the graph one level at a time.

    # Start the traversal from the Router.
    start_node = "Router"

    print(f"Starting node: {start_node}")

    traversal = bfs(graph, start_node)

    print("BFS traversal order:")
    print(traversal)

    # I added Server4 to Switch2 to see how adding another node
    # changes the BFS traversal.

    graph["Server4"] = ["Switch2"]
    graph["Switch2"].append("Server4")

    print("\n=== UPDATED GRAPH ===")

    # Display the graph again after adding Server4.
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    print("\nUpdated BFS traversal:")

    updated_traversal = bfs(graph, start_node)

    print(updated_traversal)

    # Server4 now appears in the traversal because it is connected
    # to Switch2 and can be reached from the Router.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1:
    # Start from Server1 instead of the Router.
    # This shows that BFS can start from any valid node in the graph.

    print("Edge Case 1: Start from Server1")

    traversal_from_server = bfs(graph, "Server1")

    print(traversal_from_server)

    # Starting from Server1 changes the traversal order because BFS
    # now works outward from Server1 instead of the Router.

    # Edge Case 2:
    # Test a starting node that does not exist in the graph.
    # The bfs function should return an empty list instead of
    # causing an error.

    print("\nEdge Case 2: Missing start node")

    missing_node = bfs(graph, "Server99")

    print(missing_node)

    # Since Server99 is not in the graph, an empty list is returned.

    # Edge Case 3:
    # Test a graph with only one node and no connections.

    print("\nEdge Case 3: Single-node graph")

    single_node_graph = {
        "Server1": []
    }

    single_node_result = bfs(single_node_graph, "Server1")

    print(single_node_result)

    # Since Server1 does not have any neighbors, BFS only visits
    # the starting node.


if __name__ == "__main__":
    main()