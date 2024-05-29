# Graph Search Visualizer (PyQt5)

## Introduction

**Graph Search Visualizer** is an interactive application built with PyQt5 that allows users to visualize graph search algorithms such as Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra's Algorithm, and Bellman-Ford Algorithm. Users can create nodes, connect them with edges, and then run the desired algorithm to see the step-by-step process of the search. The application also maintains a real-time dictionary representation of the graph as it is being constructed.

## Features

- **Interactive Graph Creation**: Users can place nodes anywhere on the screen and connect them with edges.
- **Algorithm Visualization**: Supports BFS, DFS, Dijkstra's, and Bellman-Ford algorithms.
- **Real-Time Graph Dictionary**: Automatically updates a dictionary representation of the graph as nodes and edges are created.
- **Supports Unweighted and Weighted Graphs**: Users can create both unweighted and weighted graphs.
  - If an unweighted graph is used and Dijkstra or Bellman-Ford is selected, the graph is automatically converted to a weighted graph with all edge weights set to one.
- **Search Results Display**: The results of the search algorithms are shown in a separate panel for easy analysis.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sammany1/Graph_Search_Visualizer.git
    cd Graph_Search_Visualizer
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
   - To add weights to edges, double-click on the edge and enter the desired weight.

3. **Selecting and Running Algorithms:**
   - Choose the desired algorithm (BFS, DFS, Dijkstra, Bellman-Ford) from the algorithm selection menu.
   - If running Dijkstra or Bellman-Ford on an unweighted graph, the application will automatically assign a weight of one to all edges.
   - Click the 'Visualize' button to start the visualization.
   - View the search results in the results panel.

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
```
## Contact

For any questions or feedback, please feel free to reach out to [Sammany1](https://github.com/Sammany1) on GitHub.
