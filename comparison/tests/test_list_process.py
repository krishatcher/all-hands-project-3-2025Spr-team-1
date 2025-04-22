import pytest

from comparison.list_process import ListProcessor
from comparison.generate import generate_random_tree_with_random_values_list

# Helper function to create a processor with tree pairs
def create_tree_processor():
    processor = ListProcessor()
    processor.insert_tree_pair(1, 2)
    processor.insert_tree_pair(1, 3)
    processor.insert_tree_pair(2, 4)
    return processor

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

def test_tree_clear():
    processor = create_tree_processor()
    assert processor.get_tree_size() == 3
    processor.clear()
    assert processor.get_tree_size() == 0
    assert not any(processor.lookup_tree_pair(p, c) 
                  for p, c in [(1, 2), (1, 3), (2, 4)])

def test_get_children():
    processor = create_tree_processor()
    assert set(processor.get_children(1)) == {2, 3}
    assert set(processor.get_children(2)) == {4}
    assert processor.get_children(3) == []
    assert processor.get_children(4) == []

def test_get_parents():
    processor = create_tree_processor()
    assert processor.get_parents(2) == [1]
    assert processor.get_parents(3) == [1]
    assert processor.get_parents(4) == [2]
    assert processor.get_parents(1) == []

def test_duplicate_tree_pairs():
    processor = ListProcessor()
    assert processor.insert_tree_pair(1, 2) is True
    assert processor.insert_tree_pair(1, 2) is False
    assert processor.get_tree_size() == 1
