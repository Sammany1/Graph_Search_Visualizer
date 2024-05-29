# Graph Search Visualizer (PyQt5)

## Introduction

**Graph Search Visualizer** is an interactive application built with PyQt5 that allows users to visualize graph search algorithms such as Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra's Algorithm, and Bellman-Ford Algorithm. Users can create nodes, connect them with edges, and then run the desired algorithm to see the step-by-step process of the search. The application also maintains a real-time dictionary representation of the graph as it is being constructed.

## Features

- **Interactive Graph Creation**: Users can place nodes anywhere on the screen and connect them with edges.
- **Algorithm Visualization**: Supports BFS, DFS, Dijkstra's, and Bellman-Ford algorithms.
- **Real-Time Graph Dictionary**: Automatically updates a dictionary representation of the graph as nodes and edges are created.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/graph-search-visualizer.git
    cd graph-search-visualizer
    ```

2. **Install the required packages:**
    ```bash
    pip install pyqt5
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **Creating Nodes and Edges:**
   - Click anywhere on the canvas to create a node.
   - Click on a node and drag to another node to create an edge.

3. **Selecting and Running Algorithms:**
   - Choose the desired algorithm (BFS, DFS, Dijkstra, Bellman-Ford) from the algorithm selection menu.
   - Click the 'Run' button to start the visualization.

## Graph Dictionary

As you create the graph, the application maintains a real-time dictionary representation of the graph structure. This dictionary updates automatically with every new node and edge added. The dictionary is displayed in a side panel for reference.

### Example Dictionary Format

```python
{
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 2},
    'C': {'A': 10, 'B': 3},
    'D': {'B': 2}
}
