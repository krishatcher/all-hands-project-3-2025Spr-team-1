from typing import Dict, Set, List, Tuple
from generate import generate_random_tree_with_random_values_set

class Graph:
    """A class to represent a graph using sets."""
    def __init__(self) -> None:
        """Initializes an empty graph."""
        self.graph: Dict[int, Set[int]] = {}

    def insert(self, node1: int, node2: int) -> None:
        """Inserts an edge between two nodes in the graph."""
        # If node1 is not in the graph, add it with an empty set
        if node1 not in self.graph:
            self.graph[node1] = set()
        # If node2 is not in the graph, add it with an empty set
        if node2 not in self.graph:
            self.graph[node2] = set()
        # Add node2 to the neighbors of node1
        self.graph[node1].add(node2)
        # Add node1 to the neighbors of node2
        self.graph[node2].add(node1)

    def update(self, node1: int, node2: int, add_edge: bool = True) -> None:
        """Updates the graph by adding or removing an edge between two nodes."""
        # If either node1 or node2 is not in the graph, do nothing
        if node1 not in self.graph or node2 not in self.graph:
            return
        if add_edge:
            # Add an edge between node1 and node2
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)
        else:
            # Remove the edge between node1 and node2
            self.graph[node1].discard(node2)
            self.graph[node2].discard(node1)

    def delete(self, node: int) -> None:
        """Deletes a node and all its edges from the graph."""
        # If the node is not in the graph
        if node not in self.graph:
            return
        # Remove the node from the neighbors of all its nodes
        for neighbor in list(self.graph[node]):
            self.graph[neighbor].remove(node)
        # Delete the node from the graph
        del self.graph[node]

    def get_graph(self) -> Dict[int, Set[int]]:
        """Returns the graph as an dictionary."""
        return self.graph


def generate_and_process_tree(num_nodes: int) -> Dict[int, Set[int]]:
    """Generates a random tree, processes it, and returns the resulting graph."""
    # Generate a random tree as a list of edges (parent, child)
    tree = generate_random_tree_with_random_values_set(num_nodes)
    # Create a new Graph object
    graph = Graph()

    # Add all edges from the tree to the graph
    for parent, child in tree:
        graph.insert(parent, child)

    # Get a list of all nodes in the graph
    existing_nodes = list(graph.graph.keys())
    if len(existing_nodes) >= 2:
        # Add an edge between the first two nodes (if they exist)
        graph.update(existing_nodes[0], existing_nodes[1], add_edge=True)

    if existing_nodes:
        # Delete the first node from the graph
        graph.delete(existing_nodes[0])

    # Return the final graph as a dictionary
    return graph.get_graph()

