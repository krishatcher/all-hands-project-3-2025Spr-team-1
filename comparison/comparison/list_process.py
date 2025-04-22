from typing import List, Tuple, TypeVar, Any

T = TypeVar('T')  # Generic type for values

class ListProcessor:
    def __init__(self) -> None:
        self.data: List[T] = []
        self.tree: List[Tuple[T, T]] = []

    def insert(self, value: T) -> None:
        """Insert a value into the list.
        
        Args:
            value: The value to insert
        """
        self.data.append(value)

    def insert_tree_pair(self, parent: T, child: T) -> bool:
        """Insert a parent-child pair into the tree structure.
        
        Args:
            parent: The parent node value
            child: The child node value
            
        Returns:
            bool: True if the pair was inserted, False if it already exists
        """
        if (parent, child) in self.tree:
            return False
        self.tree.append((parent, child))
        return True

    def delete(self, value: T) -> bool:
        """Delete a value from the list if it exists.
        
        Args:
            value: The value to delete
            
        Returns:
            bool: True if the value was deleted, False if it didn't exist
        """
        try:
            self.data.remove(value)
            return True
        except ValueError:
            return False

    def delete_tree_pair(self, parent: T, child: T) -> bool:
        """Delete a parent-child pair from the tree structure.
        
        Args:
            parent: The parent node value
            child: The child node value
            
        Returns:
            bool: True if the pair was deleted, False if it didn't exist
        """
        try:
            self.tree.remove((parent, child))
            return True
        except ValueError:
            return False

    def lookup(self, value: T) -> bool:
        """Check if a value exists in the list.
        
        Args:
            value: The value to look up
            
        Returns:
            bool: True if the value exists, False otherwise
        """
        return value in self.data

    def lookup_tree_pair(self, parent: T, child: T) -> bool:
        """Check if a parent-child pair exists in the tree structure.
        
        Args:
            parent: The parent node value
            child: The child node value
            
        Returns:
            bool: True if the pair exists, False otherwise
        """
        return (parent, child) in self.tree

    def get_size(self) -> int:
        """Get the current size of the list.
        
        Returns:
            int: The number of elements in the list
        """
        return len(self.data)

    def get_tree_size(self) -> int:
        """Get the current size of the tree (number of pairs).
        
        Returns:
            int: The number of pairs in the tree
        """
        return len(self.tree)

    def clear(self) -> None:
        """Clear all data from the list and tree."""
        self.data.clear()
        self.tree.clear()

    def get_tree(self) -> List[Tuple[T, T]]:
        """Get the current tree structure.
        
        Returns:
            List[Tuple[T, T]]: A copy of the tree as a list of (parent, child) tuples
        """
        return self.tree.copy()

    def get_data(self) -> List[T]:
        """Get the current list data.
        
        Returns:
            List[T]: A copy of the data list
        """
        return self.data.copy()

    def get_children(self, parent: T) -> List[T]:
        """Get all children of a given parent node.
        
        Args:
            parent: The parent node value
            
        Returns:
            List[T]: A list of child values
        """
        return [child for p, child in self.tree if p == parent]

    def get_parents(self, child: T) -> List[T]:
        """Get all parents of a given child node.
        
        Args:
            child: The child node value
            
        Returns:
            List[T]: A list of parent values
        """
        return [parent for parent, c in self.tree if c == child]
