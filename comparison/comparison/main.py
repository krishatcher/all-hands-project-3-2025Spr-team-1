#!/usr/bin/env python3

import argparse
import sys
import time
from typing import List

from rich.console import Console
from rich.table import Table

from .set import Graph as SetGraph
from .list_process import ListProcessor
from .generate import generate_random_tree_with_random_values_list


def run_demo(num_vertices=20, quiet=False):
    console = Console()

    # Generate tree data
    try:
        edges = generate_random_tree_with_random_values_list(num_vertices)
    except ValueError:
        edges = [(1, 2), (2, 3), (3, 4), (4, 5)]

    # Initialize implementations
    set_tree = SetGraph()
    list_tree = ListProcessor()

    set_insert_times = []
    list_insert_times = []
    set_lookup_times = []
    list_lookup_times = []
    set_delete_times = []
    list_delete_times = []
    set_verify_times = []
    list_verify_times = []

    # Table for insertion
    insertion_table = Table(title="Tree Node Insertion Operations")
    insertion_table.add_column("Parent-Child Edge", style="cyan")
    insertion_table.add_column("Set Implementation", style="green")
    insertion_table.add_column("List Implementation", style="yellow")

    # Perform insertions
    for v1, v2 in edges:
        set_start_time = time.time()
        set_tree.insert_edge(v1, v2)
        set_end_time = time.time()
        set_insert_times.append((set_end_time - set_start_time))

        list_start_time = time.time()
        list_tree.insert_tree_pair(v1, v2)
        list_end_time = time.time()
        list_insert_times.append((list_end_time - list_start_time))

        insertion_table.add_row(f"({v1}, {v2})", "Success", "Success")

    # Table for lookup
    lookup_table = Table(title="Tree Node Lookup Operations")
    lookup_table.add_column("Parent-Child Edge", style="cyan")
    lookup_table.add_column("Set Implementation", style="green")
    lookup_table.add_column("List Implementation", style="yellow")

    # Perform lookups
    for v1, v2 in edges:
        set_start_time = time.time()
        set_result = str(set_tree.lookup_edge(v1, v2))
        set_end_time = time.time()
        set_lookup_times.append((set_end_time - set_start_time))

        list_start_time = time.time()
        list_result = str(list_tree.lookup_tree_pair(v1, v2))
        list_end_time = time.time()
        list_lookup_times.append((list_end_time - list_start_time))

        lookup_table.add_row(f"({v1}, {v2})", set_result, list_result)

    # Table for deletion
    deletion_table = Table(title="Tree Node Deletion Operations")
    deletion_table.add_column("Parent-Child Edge", style="cyan")
    deletion_table.add_column("Set Implementation", style="green")
    deletion_table.add_column("List Implementation", style="yellow")

    # Perform deletions
    deletion_count = len(edges) // 2
    for v1, v2 in edges[:deletion_count]:
        set_start_time = time.time()
        set_tree.update_edge(v1, v2, False)
        set_end_time = time.time()
        set_delete_times.append((set_end_time - set_start_time))

        list_start_time = time.time()
        list_tree.delete_tree_pair(v1, v2)
        list_end_time = time.time()
        list_delete_times.append((list_end_time - list_start_time))

        deletion_table.add_row(f"({v1}, {v2})", "Removed", "Removed")

    # Table for verification
    verification_table = Table(title="Deletion Verification Operations")
    verification_table.add_column("Parent-Child Edge", style="cyan")
    verification_table.add_column("Set Implementation", style="green")
    verification_table.add_column("List Implementation", style="yellow")

    # Verify deletions
    for v1, v2 in edges[:deletion_count]:
        set_start_time = time.time()
        set_result = str(set_tree.lookup_edge(v1, v2))
        set_end_time = time.time()
        set_verify_times.append((set_end_time - set_start_time))

        list_start_time = time.time()
        list_result = str(list_tree.lookup_tree_pair(v1, v2))
        list_end_time = time.time()
        list_verify_times.append((list_end_time - list_start_time))

        verification_table.add_row(f"({v1}, {v2})", set_result, list_result)

    results_table = Table(title="Experimental Results")
    results_table.add_column("Implementation", style="green")
    results_table.add_column("Operation", style="cyan")
    results_table.add_column("Repetitions", style="yellow")
    results_table.add_column("Total Time (sec)", style="white")
    results_table.add_column("Average Time (sec)", style="magenta")

    results_table.add_row(
    	"Set",
		"Insert",
		str(len(set_insert_times)),
		f"{sum(set_insert_times):.10f}",
		f"{(sum(set_insert_times) / len(set_insert_times)):.10f}")
    results_table.add_row(
    	"Set",
		"Lookup",
		str(len(set_lookup_times)),
		f"{sum(set_lookup_times):.10f}",
		f"{(sum(set_lookup_times) / len(set_lookup_times)):.10f}")
    results_table.add_row(
    	"Set",
		"Delete",
		str(len(set_delete_times)),
		f"{sum(set_delete_times):.10f}",
		f"{(sum(set_delete_times) / len(set_delete_times)):.10f}")   
    results_table.add_row(
    	"Set",
		"Verify Deletion",
		str(len(set_verify_times)),
		f"{sum(set_verify_times):.10f}",
		f"{(sum(set_verify_times) / len(set_verify_times)):.10f}")
    results_table.add_row(
    	"List",
		"Insert",
		str(len(list_insert_times)),
		f"{sum(list_insert_times):.10f}",
		f"{(sum(list_insert_times) / len(list_insert_times)):.10f}")
    results_table.add_row(
    	"List",
		"Lookup",
		str(len(list_lookup_times)),
		f"{sum(list_lookup_times):.10f}",
		f"{(sum(list_lookup_times) / len(list_lookup_times)):.10f}")
    results_table.add_row(
    	"List",
		"Delete",
		str(len(list_delete_times)),
		f"{sum(list_delete_times):.10f}",
		f"{(sum(list_delete_times) / len(list_delete_times)):.10f}") 
    results_table.add_row(
    	"List",
		"Verify Deletion",
		str(len(list_verify_times)),
		f"{sum(list_verify_times):.10f}",
		f"{(sum(list_verify_times) / len(list_verify_times)):.10f}")

    if quiet:
        console.print("\n[bold blue]Tree Implementation Comparison Results Summary[/bold blue]\n")
        console.print(results_table)
    else:
        console.print("\n[bold blue]Tree Implementation Comparison Results Detail[/bold blue]\n")
        console.print(insertion_table)
        console.print(lookup_table)
        console.print(deletion_table)
        console.print(verification_table)


def show_help():
    console = Console()
    console.print("[bold]USAGE:[/bold] poetry run comparison [OPTIONS]")
    console.print()

    options_table = Table(title="Command Options")
    options_table.add_column("Option", style="cyan")
    options_table.add_column("Description", style="white")
    options_table.add_column("Default", style="yellow")

    options_table.add_row("-v, --vertices", "Number of vertices in the test tree", "20")
    options_table.add_row("-q, --quiet", "Reduce output verbosity", "False")
    options_table.add_row("--help", "Show this help message", "")

    console.print(options_table)

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        show_help()
        return

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-v", "--vertices", type=int, default=20, help=argparse.SUPPRESS)
    parser.add_argument("-q", "--quiet", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--help", "-h", action="store_true", help=argparse.SUPPRESS)

    args = parser.parse_args()

    if args.vertices < 2:
        parser.error("Number of vertices must be at least 2")

    run_demo(args.vertices, args.quiet)

if __name__ == "__main__":
    main()


# References and Source Links:
# Algorithmology: https://algorithmology.org/schedule/weekthirteen/
# Tree Data Structures: https://en.wikipedia.org/wiki/Tree_(data_structure)
# Rich Library for Tables: https://rich.readthedocs.io/en/stable/tables.html
# Graph vs Tree Data Structures: https://www.geeksforgeeks.org/difference-between-graph-and-tree/
# Cursor AI(Claude 3.5 Sonnet and 3.7 sonnet): Used for the information, fixing various issues with the code and also for the test cases generation.
