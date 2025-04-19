# Graph Performance Comparison

This repo is related to the **Algorithm All-Hands Projects** (AAHP) described within the [Algorithmology.org](https://algorithmology.org/) curriculum.

This is the third AAHP within the Spring 2025 cohort of Algorithmology at [Allegheny College](https://sites.allegheny.edu/computer-science/) (CMPSC 202-00) taught by [Dr. Gregory M Kapfhammer](https://github.com/gkapfham).

## Algorithm All-Hands Projects

These projects enable students to explore both the scientific and engineering aspects of algorithm analysis, as outlined in the course schedule. During the completion of a scientific study phase of algorithm analysis, students will work in a team to propose an original research question and design an experiment to answer it. When completing an engineering effort phase of algorithm analysis, students work in a team as they design, implement, document, test, and maintain software tools that support the rigorous evaluation of the performance (e.g., time or space overhead) of a Python program. The conclusion of an algorithm all-hands project involves the team-based creation, publication, and oral presentation of a report that overviews all of the experiences during the completion of the scientific study and engineering effort tasks for answering an original research question in the field of algorithm analysis. Students may use external sources, including artificial intelligence coding assistants, during the completion of an algorithm all-hands project provided that they cite these sources and explain how they used them to complete their part(s) of an algorithm all-hands project.

## Team

The group working on the project housed in this repo is:

* [Anoop Guragain](https://github.com/AN00P-G)
* [Kris Hatcher](https://github.com/krishatcher)
* [Anton Hedlund](https://github.com/ahedlund01)
* [Rosa Ruiz](https://github.com/ruizrosa2905)
* [Molly Suppo](https://github.com/suppo01)

## Project Description

### Research Question

How does implementing a tree with Python's `set` and `list` structures impact performance in terms of insertion, deletion, and lookup speed?

### Process

* Each member of the team was assigned a portion of the code implementation to complete.
* Once all code is implemented, each team member will run the same set of benchmarking runs and add their data to the shared Google Sheet.
* Each team member will then complete part of a writeup, specifically a portion of the writeup about the code they implemented. This writeup will be published on [algorithmology.org/allhands](https://algorithmology.org/allhands/) at the conclusion of the project.

Each team member ran the experimental suite 5 times on their own machine. The five runs were with the following vertex counts: 20, 200, 2000, 20000, and 200000.

## Running the Experiment

In order to execute the code in this repo, a user must call the CLI function and pass in options.

### Command Options

To run the program, the minimum required is to simply enter `poetry run comparison` in the command line, while in the context of `/comparison` within this repo's structure. All options have default values (described below) that will be used to run the tool. The commands below would be added to that base command.

* Help
  * `-h` or `--help`: Show help message and exit.
* Quiet
  * `-q` or `--quiet`: Show summary results only.
* Vertices
  * `-v` or `--vertices`: Number of vertices in the tree. Default is 20.

### Output

```command
> poetry run comparison -v 20 -q

Tree Implementation Comparison Results Summary

                                   Experimental Results                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Implementation ┃ Operation       ┃ Repetitions ┃ Total Time (sec) ┃ Average Time (sec) ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ Set            │ Insert          │ 19          │ 0.0000171661     │ 0.0000009035       │
│ Set            │ Lookup          │ 19          │ 0.0000078678     │ 0.0000004141       │
│ Set            │ Delete          │ 9           │ 0.0000090599     │ 0.0000010067       │
│ Set            │ Verify Deletion │ 9           │ 0.0000019073     │ 0.0000002119       │
│ List           │ Insert          │ 19          │ 0.0000064373     │ 0.0000003388       │
│ List           │ Lookup          │ 19          │ 0.0000038147     │ 0.0000002008       │
│ List           │ Delete          │ 9           │ 0.0000042915     │ 0.0000004768       │
│ List           │ Verify Deletion │ 9           │ 0.0000066757     │ 0.0000007417       │
└────────────────┴─────────────────┴─────────────┴──────────────────┴────────────────────┘
```

## References

1. Documentation
    - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
    - [pytest Documentation](https://docs.pytest.org/en/stable/)
    - [geeksforgeeks](https://www.geeksforgeeks.org/python-dictionary-update-method/)
2. Course Slides
    - [Hierarchical Data Structures Course Slides](https://algorithmology.org/slides/weekthirteen/#/title-slide)

### AI Usage in this Project

AI was used in this project for:
- Tree generation algorithms (adapted from Microsoft Copilot)
- Code optimization and refactoring suggestions
- Test case generation and documentation templates
- Error handling and debugging support
- Generating sample data for testing
- Writing documentation
- Autocompletion of repetitive code snippets

All AI-generated content was reviewed and validated by team members.