#!/usr/bin/env python3

import sys
import pytest
from unittest.mock import patch, MagicMock
import io

from comparison.main import run_demo, show_help, main
from comparison.set import Graph as SetGraph
from comparison.list_process import ListProcessor
from comparison.generate import generate_random_tree_with_random_values_list


class TestMainFunctionality:
    """Test cases for main.py functionality."""

    def test_generate_random_tree(self):
        """Test that the tree generator creates valid parent-child pairs."""
        num_vertices = 10
        tree = generate_random_tree_with_random_values_list(num_vertices)
        
        # Check if we have the correct number of pairs (n-1 edges for n vertices)
        assert len(tree) == num_vertices - 1
        
        # Check that pairs are in the right format
        for pair in tree:
            assert isinstance(pair, tuple)
            assert len(pair) == 2
            assert isinstance(pair[0], int)
            assert isinstance(pair[1], int)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_demo_output_format(self, mock_stdout):
        """Test that run_demo produces expected output format."""
        run_demo(num_vertices=5, quiet=False)
        output = mock_stdout.getvalue()
        
        # Check that the output contains the expected table headers
        assert "Tree Implementation Comparison" in output
        assert "Tree Node Insertion Operations" in output
        assert "Tree Node Lookup Operations" in output
        assert "Tree Node Deletion Operations" in output
        assert "Deletion Verification Operations" in output
        
        # Check that the table columns are present
        assert "Parent-Child Edge" in output
        assert "Set Implementation" in output
        assert "List Implementation" in output
        
        # Check that operation results are shown
        assert "Success" in output
        assert "True" in output
        assert "Removed" in output
        assert "False" in output

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_demo_quiet_mode(self, mock_stdout):
        """Test that quiet mode produces minimal output."""
        run_demo(num_vertices=5, quiet=True)
        output = mock_stdout.getvalue()
        
        # In quiet mode, only insertion table and summary should be shown
        assert "Tree Node Insertion Operations" in output
        assert "Performed" in output
        assert "insertions" in output
        assert "lookups" in output
        assert "deletions" in output
        
        # These should not be in the quiet output
        assert "Tree Node Lookup Operations" not in output
        assert "Tree Node Deletion Operations" not in output
        assert "Deletion Verification Operations" not in output

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_display(self, mock_stdout):
        """Test that help display shows the correct information."""
        show_help()
        output = mock_stdout.getvalue()
        
        # Check help content
        assert "USAGE:" in output
        assert "Command Options" in output
        assert "-v, --vertices" in output
        assert "-q, --quiet" in output
        assert "--help" in output

    @patch('comparison.main.run_demo')
    @patch('sys.argv', ['comparison', '-v', '15'])
    def test_main_with_vertex_argument(self, mock_run_demo):
        """Test main function with vertex count argument."""
        main()
        # Check that run_demo was called with the right arguments
        mock_run_demo.assert_called_once_with(15, False)

    @patch('comparison.main.run_demo')
    @patch('sys.argv', ['comparison', '-q'])
    def test_main_with_quiet_argument(self, mock_run_demo):
        """Test main function with quiet mode argument."""
        main()
        # Check that run_demo was called with quiet=True
        mock_run_demo.assert_called_once_with(20, True)

    @patch('comparison.main.show_help')
    @patch('sys.argv', ['comparison', '--help'])
    def test_main_with_help_argument(self, mock_show_help):
        """Test main function with help argument."""
        main()
        # Check that show_help was called
        mock_show_help.assert_called_once()

    @patch('sys.stderr', new_callable=io.StringIO)
    @patch('sys.argv', ['comparison', '-v', '1'])
    def test_main_with_invalid_vertex_count(self, mock_stderr):
        """Test error handling for invalid vertex count."""
        with pytest.raises(SystemExit):
            main()
        # Check that the error message was printed
        assert "Number of vertices must be at least 2" in mock_stderr.getvalue()

    def test_set_tree_operations(self):
        """Test that SetGraph operations work correctly."""
        set_tree = SetGraph()
        
        # Test insertion
        set_tree.insert_edge(1, 2)
        set_tree.insert_edge(2, 3)
        
        # Test lookup
        assert set_tree.lookup_edge(1, 2) is True
        assert set_tree.lookup_edge(2, 3) is True
        assert set_tree.lookup_edge(1, 3) is False
        
        # Test deletion
        set_tree.update_edge(1, 2, False)
        assert set_tree.lookup_edge(1, 2) is False
        assert set_tree.lookup_edge(2, 3) is True

    def test_list_tree_operations(self):
        """Test that ListProcessor operations work correctly."""
        list_tree = ListProcessor()
        
        # Test insertion
        list_tree.insert_tree_pair(1, 2)
        list_tree.insert_tree_pair(2, 3)
        
        # Test lookup
        assert list_tree.lookup_tree_pair(1, 2) is True
        assert list_tree.lookup_tree_pair(2, 3) is True
        assert list_tree.lookup_tree_pair(1, 3) is False
        
        # Test deletion
        list_tree.delete_tree_pair(1, 2)
        assert list_tree.lookup_tree_pair(1, 2) is False
        assert list_tree.lookup_tree_pair(2, 3) is True

    def test_both_implementations_same_results(self):
        """Test that both implementations give the same results."""
        # Create test edges
        test_edges = [(1, 2), (2, 3), (3, 4)]
        
        # Set implementation
        set_tree = SetGraph()
        for v1, v2 in test_edges:
            set_tree.insert_edge(v1, v2)
        
        # List implementation
        list_tree = ListProcessor()
        for v1, v2 in test_edges:
            list_tree.insert_tree_pair(v1, v2)
        
        # Check lookup results match
        for v1, v2 in test_edges:
            assert set_tree.lookup_edge(v1, v2) == list_tree.lookup_tree_pair(v1, v2)
        
        # Check non-existent edges
        non_existent = [(5, 6), (1, 4), (2, 4)]
        for v1, v2 in non_existent:
            assert set_tree.lookup_edge(v1, v2) == list_tree.lookup_tree_pair(v1, v2)


if __name__ == "__main__":
    pytest.main()
