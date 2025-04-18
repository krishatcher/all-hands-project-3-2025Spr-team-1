"""Generates data for the project."""

import random
from typing import Any


# Sourced Using Microsoft Copilot and Adapted (https://copilot.microsoft.com/chats/8Y3Xi2vkHinE5SUGrRXCU)
# Generates a tree with random values, between 0 and 1000, as a list of pairs
def generate_random_tree_with_random_values_list(num_nodes: int) -> Any:
    """Generates a random tree with randomly assigned integer values for nodes."""
    if num_nodes < 2:
        raise ValueError("A tree must have at least 2 nodes (root and one child).")

    tree = []
    # Generates random values for nodes
    node_values = [random.randint(0, 1000) for _ in range(num_nodes)]
    # Assigns the first random value to the root
    root = node_values.pop(0)

    # Starts with the root as the only available parent
    available_parents = [root]

    for value in node_values:
        # Randomly selects an available parent
        parent = random.choice(available_parents)
        # Creates and adds a parent-child pair
        tree.append((parent, value))
        # Adds the new node as an available parent
        available_parents.append(value)

    return tree


# Sourced Using Microsoft Copilot and Adapted (https://copilot.microsoft.com/chats/8Y3Xi2vkHinE5SUGrRXCU)
# Generates a tree with random values, between 0 and 1000, as a set of pairs
def generate_random_tree_with_random_values_set(num_nodes: int) -> Any:
    """Generates a random tree as a set of relationships with random node values."""
    if num_nodes < 2:
        raise ValueError("A tree must have at least 2 nodes (root and one child).")

    tree = set()
    # Generates random values for nodes
    node_values = [random.randint(0, 1000) for _ in range(num_nodes)]
    # Assigns the first random value to the root
    root = node_values.pop(0)

    # Starts with the root as the only available parent
    available_parents = [root]

    for value in node_values:
        # Randomly selects an available parent
        parent = random.choice(available_parents)
        # Adds a parent-child tuple
        tree.add((parent, value))
        # Adds the new node as an available parent
        available_parents.append(value)

    return tree
