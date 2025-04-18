import pytest

from comparison.list_process import ListProcessor
from comparison.generate import generate_random_tree_with_random_values_list

# Helper function to create a processor with initial values
def create_filled_processor():
    processor = ListProcessor()
    for i in range(1, 4):
        processor.insert(i)
    return processor

# Helper function to create a processor with tree pairs
def create_tree_processor():
    processor = ListProcessor()
    processor.insert_tree_pair(1, 2)
    processor.insert_tree_pair(1, 3)
    processor.insert_tree_pair(2, 4)
    return processor

# Basic List Operations Tests
def test_insert():
    processor = ListProcessor()
    processor.insert(1)
    processor.insert(2)
    processor.insert(3)
    assert processor.get_size() == 3
    assert all(processor.lookup(i) for i in [1, 2, 3])

def test_delete():
    processor = create_filled_processor()
    assert processor.delete(2) is True
    assert processor.get_size() == 2
    assert processor.lookup(2) is False
    assert processor.delete(4) is False
    assert processor.get_size() == 2

def test_lookup():
    processor = ListProcessor()
    processor.insert(1)
    processor.insert(2)
    assert all(processor.lookup(i) for i in [1, 2])
    assert processor.lookup(3) is False

def test_clear():
    processor = create_filled_processor()
    assert processor.get_size() == 3
    processor.clear()
    assert processor.get_size() == 0
    assert not any(processor.lookup(i) for i in [1, 2, 3])

# Advanced List Operations Tests
def test_multiple_operations():
    processor = ListProcessor()
    # Insert multiple values
    for i in range(10):
        processor.insert(i)
    assert processor.get_size() == 10
    
    # Delete some values
    processor.delete(5)
    processor.delete(7)
    assert processor.get_size() == 8
    assert not any(processor.lookup(i) for i in [5, 7])
    
    # Insert more values
    processor.insert(20)
    processor.insert(21)
    assert processor.get_size() == 10
    assert all(processor.lookup(i) for i in [20, 21])

@pytest.mark.parametrize("value,expected_size", [
    (1, 2),
    ("test", 2),
    (3.14, 2),
    ([1, 2, 3], 2)
])
def test_different_data_types(value, expected_size):
    processor = ListProcessor()
    processor.insert(value)
    processor.insert(value)  # Duplicate insert
    assert processor.get_size() == expected_size
    assert processor.lookup(value) is True

def test_empty_list_operations():
    processor = ListProcessor()
    assert processor.get_size() == 0
    assert processor.lookup(1) is False
    assert processor.delete(1) is False
    processor.clear()
    assert processor.get_size() == 0

def test_large_number_of_operations():
    processor = ListProcessor()
    # Insert 1000 items
    for i in range(1000):
        processor.insert(i)
    assert processor.get_size() == 1000
    
    # Delete every other item
    for i in range(0, 1000, 2):
        assert processor.delete(i) is True
    assert processor.get_size() == 500
    
    # Verify remaining items
    assert all(processor.lookup(i) for i in range(1, 1000, 2))
    assert not any(processor.lookup(i) for i in range(0, 1000, 2))

# Tree Operations Tests
def test_basic_tree_operations():
    processor = create_tree_processor()
    assert processor.get_tree_size() == 3
    assert all(processor.lookup_tree_pair(p, c) 
              for p, c in [(1, 2), (1, 3), (2, 4)])

def test_tree_deletion():
    processor = create_tree_processor()
    assert processor.delete_tree_pair(1, 2) is True
    assert processor.get_tree_size() == 2
    assert not processor.lookup_tree_pair(1, 2)
    assert processor.delete_tree_pair(5, 6) is False
    assert processor.get_tree_size() == 2

def test_tree_with_generated_data():
    processor = ListProcessor()
    num_nodes = 10
    tree = generate_random_tree_with_random_values_list(num_nodes)
    
    for parent, child in tree:
        processor.insert_tree_pair(parent, child)
    
    assert processor.get_tree_size() == num_nodes - 1
    assert all(processor.lookup_tree_pair(p, c) for p, c in tree)
    
    processor.clear()
    assert processor.get_tree_size() == 0
    assert not any(processor.lookup_tree_pair(p, c) for p, c in tree)

# Mixed Operations Tests
def test_tree_and_list_operations_together():
    processor = ListProcessor()
    processor.insert(1)
    processor.insert_tree_pair(1, 2)
    processor.insert(2)
    processor.insert_tree_pair(2, 3)
    
    assert processor.get_size() == 2
    assert processor.get_tree_size() == 2
    
    processor.clear()
    assert processor.get_size() == 0
    assert processor.get_tree_size() == 0

def test_get_tree_and_data_methods():
    processor = ListProcessor()
    processor.insert(1)
    processor.insert(2)
    processor.insert(3)
    processor.insert_tree_pair(1, 2)
    processor.insert_tree_pair(2, 3)
    
    data = processor.get_data()
    tree = processor.get_tree()
    
    assert isinstance(data, list)
    assert isinstance(tree, list)
    assert len(data) == 3
    assert len(tree) == 2
    assert all(i in data for i in [1, 2, 3])
    assert all(pair in tree for pair in [(1, 2), (2, 3)])
    
    # Verify copies are returned
    data.append(4)
    tree.append((3, 4))
    assert processor.get_size() == 3
    assert processor.get_tree_size() == 2
