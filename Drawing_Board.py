from Node import Node
from Dictionary import Dictionary
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class DrawingBoard(QWidget):
    nodesArray = []   # carry drawn nodes as QRect() objects
    canAddNode = False
    canDragNode = True
    def __init__(self): # (cls) is (this) in cpp
        super().__init__()
        self.graph = Dictionary()
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)
        self.pix = QPixmap(self.rect().size())
        boardColor = QColor(247, 245, 243)
        self.pix.fill(boardColor)

        self.begin, self.destination = QPoint(), QPoint() # initialize begin & dest with zero

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pix)
        if not self.begin.isNull() and not self.destination.isNull():
            rect = QRect(self.begin, self.destination)

    def mousePressEvent(self, event):
        print('pressred left click')
        if event.buttons() & Qt.LeftButton & self.canAddNode: # (& Qt.LeftButton) is just to make sure we are using lef click not right click
            self.begin = event.pos()
            self.destination = self.begin
            self.begin = QPoint(self.begin.x() + 20, self.begin.y() + 20)
            # cls.update()

    def mouseReleaseEvent(self, event):
        print('release left click')
        if event.button() & Qt.LeftButton & self.canAddNode:
            asciiValue = 65 + len(self.nodesArray)
            nodeName = chr(asciiValue)
            node = Node(self.begin, self.destination, nodeName)

            painter = QPainter(self.pix)

            painter.drawEllipse(node.normalized())
            painter.drawText(node, Qt.AlignCenter, Node.getName(node))
            self.begin, self.destination = QPoint(), QPoint() # reset the points to zero
            self.nodesArray.append(node)
            self.graph.addNode(nodeName)
            self.update()
            self.canAddNode = False
            myGui = QtWidgets.QApplication.instance().topLevelWidgets()[0] # get the instance of the main window
            myGui.add_node_Button.setEnabled(True)
            myGui.add_node_Button.setText("Add Node")
            myGui.showDictionary()

        if event.button() & Qt.RightButton:
            print(self.graph.getDictionary())


    def paintAllNodes(self, color):
        print('Paint All Nodes')
        painter = QPainter(self.pix)
        painter.setPen(QPen(QColor("black"), 3))  # Set pen color to red and width to 3
        painter.setBrush(QColor(color))  # Set brush to NoBrush to make the circle empty
        for node in self.nodesArray:
            painter.drawEllipse(node.normalized())
            painter.setPen(QPen(QColor("black"), 3))
            painter.drawText(node.normalized(), Qt.AlignCenter, Node.getName(node))
        self.update()

    def getNodesArray(self):
        return self.nodesArray
    def drawEdge(self, firstNodeNameEdge, secondNodeNameEdge):
        painter = QPainter(self.pix)
        painter.setPen(QPen(Qt.black, 3))
        for node in self.nodesArray:
            if node.getName() == firstNodeNameEdge:
                firstNode = node
            if node.getName() == secondNodeNameEdge:
                secondNode = node


        # drawings Line
        painter.drawLine(firstNode.normalized().center(), secondNode.normalized().center())
        # now we draw the node again with colors to make it on top of the edge
        painter.setPen(QPen(Qt.darkBlue, 3))
        painter.setBrush(QColor(Qt.lightGray))
        painter.drawEllipse(firstNode.normalized())
        painter.drawEllipse(secondNode.normalized())
        painter.drawText(firstNode.normalized(), Qt.AlignCenter, Node.getName(firstNode))
        painter.drawText(secondNode.normalized(), Qt.AlignCenter, Node.getName(secondNode))

        self.update()
    def paintNodeOutline(self, nodeName, color):
        painter = QPainter(self.pix)
        painter.setPen(QPen(QColor(color), 3))
        painter.setBrush(QColor("white"))
        for node in self.nodesArray:
            if node.getName() == nodeName:
                painter.drawEllipse(node.normalized())
                painter.setPen(QPen(QColor("black"), 3))
                painter.drawText(node.normalized(), Qt.AlignCenter, node.getName())
        self.update()
    def paintNodeFill(self, nodeName, color):
        painter = QPainter(self.pix)
        painter.setPen(QPen(QColor("black"), 3))
        painter.setBrush(QColor(color))
        for node in self.nodesArray:
            if node.getName() == nodeName:
                painter.drawEllipse(node.normalized())
                painter.setPen(QPen(QColor("black"), 3))
                painter.drawText(node.normalized(), Qt.AlignCenter, node.getName())
        self.update()

    def paintNodeOutlineAndLetter(self, nodeName, color):
        painter = QPainter(self.pix)
        painter.setPen(QPen(QColor(color), 3))
        painter.setBrush(QColor("white"))
        for node in self.nodesArray:
            if node.getName() == nodeName:
                painter.drawEllipse(node.normalized())
                painter.setPen(QPen(QColor(color), 3))
                painter.drawText(node.normalized(), Qt.AlignCenter, node.getName())
        self.update()

    def paintNodeOutlineAndLetter(self, nodeName, outlineColor, letterColor):
        painter = QPainter(self.pix)
        painter.setPen(QPen(QColor(outlineColor), 3))
        painter.setBrush(QColor("white"))
        for node in self.nodesArray:
            if node.getName() == nodeName:
                painter.drawEllipse(node.normalized())
                painter.setPen(QPen(QColor(letterColor), 3))
                painter.drawText(node.normalized(), Qt.AlignCenter, node.getName())
        self.update()

    def paintWeight(self, enterdFirstNodeNameEdge, enterdSecondNodeNameEdge, weight):
        painter = QPainter(self.pix)
        painter.setPen(QPen(QColor("black"), 3))
        for node in self.nodesArray:
            if node.getName() == enterdFirstNodeNameEdge:
                firstNode = node
            if node.getName() == enterdSecondNodeNameEdge:
                secondNode = node
        firstNodeCenter = firstNode.normalized().center()
        secondNodeCenter = secondNode.normalized().center()
        midpoint = QPoint((firstNode.normalized().center().x() + secondNode.normalized().center().x()) // 2,
                              (firstNode.normalized().center().y() + secondNode.normalized().center().y()) // 2)
        path = QPainterPath()
        font = QFont("Uni Sans", 12, QFont.Thin)
        font.setWeight(QFont.Thin)
        path.addText(midpoint, font, str(weight))
        # Draw the text using the QPainterPath
        painter.drawPath(path)
        self.update()
    def restBoard(self):
        self.nodesArray.clear()
        self.canAddNode = False
        self.pix = QPixmap(1200, 800)
        boardColor = QColor(247, 245, 243)
        self.pix.fill(boardColor)



