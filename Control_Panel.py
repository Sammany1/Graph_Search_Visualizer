from Dictionary import Dictionary
from Bellman_Ford_algorithm import Bellman_Ford_algorithm
from Dijkstras_algorithm import Dijkstra_algorithm
from Depth_First_Search import Depth_First_Search
from Breadth_First_Search import Breadth_First_Search
from Drawing_Board import DrawingBoard
import pprint
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        self.graph = Dictionary()
        uic.loadUi('GUI.ui', self)
        self.draw = DrawingBoard()
        self.verticalLayout.addWidget(self.draw)
        self.show()

        self.hasWeight = False
        self.hasNegativeWeights = False
        self.label_4.setEnabled(False)
        self.edge_weight_TextField.setDisabled(True)
        self.dictionary_viewer_TextEdit.setReadOnly(True)
        self.algorithms_results_viewer_TextEdit.setReadOnly(True)

        self.add_node_Button.clicked.connect(self.allow_drawing)
        self.make_edge_Button.clicked.connect(self.makeEdgeClicked)
        self.allow_weight_Button.clicked.connect(self.allowWeights)
        self.visualize_Button.clicked.connect(self.run_selected_algorithm)
        self.reset_Button.clicked.connect(self.resetSystem)

        group_radioButtons = QButtonGroup(self)
        group_radioButtons.addButton(self.bfs_radioButton)
        group_radioButtons.addButton(self.ballman_ford_radioButton)
        group_radioButtons.addButton(self.dijkstra_radioButton)
        group_radioButtons.addButton(self.dfs_radioButton)


    def allow_drawing(self):
        self.draw.canAddNode = True
        self.add_node_Button.setEnabled(False)
        self.add_node_Button.setText("Click anywhere on the white board\n to add a Node")
    def makeEdgeClicked(self):
        node1 = self.enter_First_nodeName_edge_TextField.toPlainText().upper()
        node2 = self.enter_Second_nodeName_edge_TextField.toPlainText().upper()
        weightString = self.edge_weight_TextField.toPlainText()
        try:
            weight = int(weightString)
        except ValueError:
            weight = None

        if weightString is None and self.hasWeight:
            QMessageBox.critical(self, "Error", "Please enter a weight!")
        elif weightString == "0":
            QMessageBox.critical(self, "Error", "Weight cannot be 0!")
        elif weight is None and self.hasWeight:
            QMessageBox.critical(self, "Error", "Weight must be a number!")
        elif not self.graph.nodeNameExists(node1):
            QMessageBox.critical(self, "Error", "First node does not exist!")
        elif node1 == node2:
            QMessageBox.critical(self, "Error", "Both nodes are the same!")
        elif not self.graph.nodeNameExists(node2):
            QMessageBox.critical(self, "Error", "Second node does not exist!")
        elif not self.hasWeight and self.graph.edgeExists(node1, node2):
            QMessageBox.critical(self, "Error", "Edge already exists!")
        elif self.hasWeight and self.graph.edgeWeightExists(node1, node2):
            QMessageBox.critical(self, "Error", "Edge with weight already exists!")

        else:
            self.addEdge(node1,node2, weight)

    def addEdge(self, node1, node2, weight):
        if weight is not None and weight < 0 and not self.hasNegativeWeights:
            QMessageBox.information(self, "Information", "Dijkstra's can't handle Negative Weights!")
            self.allowNegativeWeights()
        if self.hasWeight:
            # add to dictionary
            if self.graph.edgeExists(node1, node2):
                self.graph.convertEgdeToWeighted(node1, node2, weight)
            else:
                self.graph.addEdgeWithWeight(node1, node2, weight)
            # draw edge
            self.draw.drawEdge(node1, node2)
            self.draw.paintWeight(node1, node2, weight)
        else:
            # add to dictionary
            self.graph.addEdge(node1, node2)
            # draw edge
            self.draw.drawEdge(node1, node2)
        self.showDictionary()

    def showDictionary(self):
        formatted_graph = pprint.pformat(self.graph.getDictionary(), indent=4, width=40)
        self.dictionary_viewer_TextEdit.setPlainText(formatted_graph)
        print(formatted_graph)

    def run_BFS_algorithm(self):
        print("Running BFS algorithm...")
        self.visualize_Button.setEnabled(False)
        results = Breadth_First_Search(self.graph.getDictionary(), 'A', self.draw)
        self.visualize_Button.setEnabled(True)
        self.algorithms_results_viewer_TextEdit.setPlainText(str(results))
        print("results")
        print(results)

    def run_DFS_algorithm(self):
        print("Running DFS algorithm...")
        self.visualize_Button.setEnabled(False)
        results = Depth_First_Search(self.graph.getDictionary(), 'A', self.draw)
        self.visualize_Button.setEnabled(True)
        self.algorithms_results_viewer_TextEdit.setPlainText(str(results))
    def run_Ballman_Ford_algorithm(self):
        print("Running Ballman-Ford algorithm...")
        if self.hasWeight:
            self.visualize_Button.setEnabled(False)
            result = Bellman_Ford_algorithm(self.graph.getDictionary(), 'A', self.draw)
            self.visualize_Button.setEnabled(True)
        else:
            weightedGraph = self.graph.copyUnweightedAndConvertToWeightedGraph(self.graph)
            print("printin weighted graph...")
            print(weightedGraph)
            self.visualize_Button.setEnabled(False)
            result = Bellman_Ford_algorithm(weightedGraph, 'A', self.draw)
            self.visualize_Button.setEnabled(True)
        formatted_graph = pprint.pformat(result, indent=4, width=40)
        self.algorithms_results_viewer_TextEdit.setPlainText(formatted_graph)


    def run_Dijkstra_algorithm(self):
        print("Running Dijkstra algorithm...")
        if self.hasWeight:
            self.visualize_Button.setEnabled(False)
            results = Dijkstra_algorithm(self.graph.getDictionary(), 'A', self.draw)
            self.visualize_Button.setEnabled(True)
        else:
            weightedGraph = self.graph.copyUnweightedAndConvertToWeightedGraph(self.graph)
            print("printin weighted graph...")
            print(weightedGraph)
            self.visualize_Button.setEnabled(False)
            results = Dijkstra_algorithm(weightedGraph, 'A', self.draw)
            self.visualize_Button.setEnabled(True)
        formatted_graph = pprint.pformat(results, indent=4, width=40)
        self.algorithms_results_viewer_TextEdit.setPlainText(formatted_graph)
    def run_selected_algorithm(self):
        if self.bfs_radioButton.isChecked() and not self.hasWeight:
            self.run_BFS_algorithm()
        elif self.dfs_radioButton.isChecked() and not self.hasWeight:
            self.run_DFS_algorithm()
        elif self.ballman_ford_radioButton.isChecked():
            if self.hasWeight:
                if self.graph.allEdgesHaveWeights():
                    self.run_Ballman_Ford_algorithm()
                else:
                    QMessageBox.critical(self, "Error", "All edges must have weights to run Ballman-Ford algorithm!")
            else:
                self.run_Ballman_Ford_algorithm()
        elif self.dijkstra_radioButton.isChecked():
            if self.hasWeight:
                if self.graph.allEdgesHaveWeights():
                    self.run_Dijkstra_algorithm()
                else:
                    QMessageBox.critical(self, "Error", "All edges must have weights to run Dijkstra algorithm!")
            else:
                self.run_Dijkstra_algorithm()
        else:
            QMessageBox.critical(self, "Error", "Please select an algorithm to run!")
    def allowWeights(self):
        self.hasWeight = True
        self.allow_weight_Button.setEnabled(False)
        self.bfs_radioButton.setEnabled(False)
        self.dfs_radioButton.setEnabled(False)
        self.edge_weight_TextField.setEnabled(True)
        self.label_4.setEnabled(True)
        if self.bfs_radioButton.isChecked() or self.dfs_radioButton.isChecked():
            self.dijkstra_radioButton.setChecked(True)
        QMessageBox.information(self, "Information", "BFS and DFS can't handle weighted Graphs!")
    def allowNegativeWeights(self):
        print("Negative weights enterd")
        self.dijkstra_radioButton.setEnabled(False)
        self.ballman_ford_radioButton.setChecked(True)
        self.hasNegativeWeights = True

    def resetSystem(self):
        reply = QMessageBox.question(self, 'Reset System',
                                     "Are you sure you want to reset?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.graph.clearDictionary()
            self.draw.restBoard()
            self.draw.update()
            self.hasNegativeWeights = False
            self.add_node_Button.setEnabled(True)
            self.add_node_Button.setText("Add Node")
            self.algorithms_results_viewer_TextEdit.clear()
            self.allow_weight_Button.setEnabled(True)
            self.bfs_radioButton.setEnabled(True)
            self.dfs_radioButton.setEnabled(True)
            self.dijkstra_radioButton.setEnabled(True)
            self.edge_weight_TextField.setDisabled(True)
            self.label_4.setEnabled(False)
            self.hasWeight = False
            self.bfs_radioButton.setChecked(False)
            self.dijkstra_radioButton.setChecked(False)
            self.ballman_ford_radioButton.setChecked(False)
            self.dfs_radioButton.setChecked(False)
            self.visualize_Button.setEnabled(True)
            self.enter_First_nodeName_edge_TextField.clear()
            self.enter_Second_nodeName_edge_TextField.clear()
            self.edge_weight_TextField.clear()
            self.dictionary_viewer_TextEdit.clear()
            self.algorithms_results_viewer_TextEdit.clear()

    def on_click(self):
            pass