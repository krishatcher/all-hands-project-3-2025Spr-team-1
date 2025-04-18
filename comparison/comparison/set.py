from typing import Dict, Set

class Graph:
    def __init__(self) -> None:
        """Initialize an empty graph using a dictionary of sets."""
        self.graph: Dict[int, Set[int]] = {}

    def insert_edge(self, node1: int, node2: int) -> None:
        """Insert an edge between two nodes."""
        if node1 not in self.graph:
            self.graph[node1] = set()
        if node2 not in self.graph:
            self.graph[node2] = set()
        self.graph[node1].add(node2)
        self.graph[node2].add(node1)

    def delete_node(self, node: int) -> bool:
        """Delete a node and all its connections from the graph."""
        if node not in self.graph:
            return False
        for neighbor in list(self.graph[node]):
            self.graph[neighbor].remove(node)
        del self.graph[node]
        return True

    def update_edge(self, node1: int, node2: int, add_edge: bool = True) -> None:
        """Add or remove an edge between two nodes."""
        if node1 not in self.graph or node2 not in self.graph:
            return
        if add_edge:
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)
        else:
            self.graph[node1].discard(node2)
            self.graph[node2].discard(node1)

    def lookup_node(self, node: int) -> bool:
        """Check if a node exists in the graph."""
        return node in self.graph

    def lookup_edge(self, node1: int, node2: int) -> bool:
        """Check if an edge exists between two nodes."""
        return node1 in self.graph and node2 in self.graph[node1]

    def get_neighbors(self, node: int) -> Set[int]:
        """Return all neighbors of a given node."""
        return self.graph.get(node, set())

    def get_graph_size(self) -> int:
        """Return the number of nodes in the graph."""
        return len(self.graph)

    def get_graph_structure(self) -> Dict[int, Set[int]]:
        """Return the current graph structure."""
        return self.graph.copy()

if __name__ == "__main__":
    g = Graph()
    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(3, 4)

    print("Graph structure:", g.get_graph_structure())
    print("Does node 2 exist?", g.lookup_node(2))
    print("Is there an edge between 2 and 3?", g.lookup_edge(2, 3))

    g.delete_node(2)
    print("Graph after deleting node 2:", g.get_graph_structure())
    print("Does node 2 still exist?", g.lookup_node(2))


# Results:

# Graph structure: {1: {2}, 2: {1, 3}, 3: {2, 4}, 4: {3}}
# Does node 2 exist? True
# Is there an edge between 2 and 3? True
# Graph after deleting node 2: {1: set(), 3: {4}, 4: {3}}
# Does node 2 still exist? False