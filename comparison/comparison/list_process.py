class ListProcessor:
    def __init__(self):
        self.data = []
        self.tree = []

    def insert(self, value):
        """Insert a value into the list."""
        self.data.append(value)

    def insert_tree_pair(self, parent, child):
        """Insert a parent-child pair into the tree structure."""
        self.tree.append((parent, child))

    def delete(self, value):
        """Delete a value from the list if it exists."""
        try:
            self.data.remove(value)
            return True
        except ValueError:
            return False

    def delete_tree_pair(self, parent, child):
        """Delete a parent-child pair from the tree structure."""
        try:
            self.tree.remove((parent, child))
            return True
        except ValueError:
            return False

    def lookup(self, value):
        """Check if a value exists in the list."""
        return value in self.data

    def lookup_tree_pair(self, parent, child):
        """Check if a parent-child pair exists in the tree structure."""
        return (parent, child) in self.tree

    def get_size(self):
        """Get the current size of the list."""
        return len(self.data)

    def get_tree_size(self):
        """Get the current size of the tree (number of pairs)."""
        return len(self.tree)

    def clear(self):
        """Clear all data from the list and tree."""
        self.data.clear()
        self.tree.clear()

    def get_tree(self):
        """Get the current tree structure."""
        return self.tree.copy()

    def get_data(self):
        """Get the current list data."""
        return self.data.copy()
