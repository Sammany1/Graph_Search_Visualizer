from PyQt5.QtCore import *
from Drawing_Board import DrawingBoard

def Depth_First_Search(graph, start, draw: DrawingBoard):
    visited = []
    stack = [start]
    loop = QEventLoop()   # Create an event loop

    def process_node():
        draw.paintAllNodes("white")
        for node in visited:
            draw.paintNodeOutline(node, "grey")
            draw.paintNodeFill(node, "grey")
        if stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                neighbours = graph[node]
                draw.paintNodeFill(node, "darkRed")  # current node
                for neighbour in neighbours:
                    if neighbour not in visited:
                        draw.paintNodeOutlineAndLetter(neighbour, "green", "darkGreen") # neighbour node
                        stack.append(neighbour)
            QTimer.singleShot(2000, process_node)  # Schedule the next call
        else:
            print("finished search")
            loop.quit()  # Quit the event loop when the search is finished

    QTimer.singleShot(2000, process_node)  # Start the process
    loop.exec_()  # Start the event loop

    return visited