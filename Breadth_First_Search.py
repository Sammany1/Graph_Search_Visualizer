from PyQt5.QtCore import *
from Drawing_Board import DrawingBoard

def Breadth_First_Search(graph, start, draw: DrawingBoard):
    visited = []
    queue = [start]
    loop = QEventLoop()   # Create an event loop

    def process_node():
        draw.paintAllNodes("white")
        for node in visited:
            draw.paintNodeOutline(node, "grey")
            draw.paintNodeFill(node, "grey")
        if queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                neighbours = graph[node]
                draw.paintNodeFill(node, "darkRed")  # current node
                for neighbour in neighbours:
                    if neighbour not in visited:
                        draw.paintNodeOutlineAndLetter(neighbour, "green", "darkGreen") # neighbour node
                        queue.append(neighbour)
            QTimer.singleShot(2000, process_node)  # Schedule the next call
        else:
            print("finished search")
            loop.quit()  # Quit the event loop when the search is finished

    QTimer.singleShot(2000, process_node)  # Start the process
    loop.exec_()  # Start the event loop

    return visited