import heapq
from PyQt5.QtCore import QTimer, QEventLoop
from Drawing_Board import DrawingBoard

def Dijkstra_algorithm(graph, start, draw: DrawingBoard):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    priority_queue = [(0, start)]
    visited = []

    loop = QEventLoop()

    while priority_queue:
        draw.paintAllNodes("white")
        for node in visited:
            draw.paintNodeOutline(node, "grey")
            draw.paintNodeFill(node, "grey")

        current_distance, node = heapq.heappop(priority_queue)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            draw.paintNodeFill(node, "darkRed")

            for neighbour, weight in neighbours:
                if neighbour not in visited:
                    new_distance = current_distance + weight
                    if new_distance < distance[neighbour]:
                        distance[neighbour] = new_distance
                        heapq.heappush(priority_queue, (new_distance, neighbour))
                        draw.paintNodeOutlineAndLetter(neighbour, "green", "darkGreen")

        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        loop = QEventLoop()

    print("finished search")
    print(distance)
    return distance