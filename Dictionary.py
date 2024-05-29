class Dictionary:
    dictionary = {}
    def addNode(cls, nodeName):
        if nodeName not in cls.dictionary:
            cls.dictionary[nodeName] = []

    def addEdge(cls, node1, node2):
        if node1 in cls.dictionary and node2 in cls.dictionary:
            cls.dictionary[node1].append(node2)
            cls.dictionary[node2].append(node1)
    def addEdgeWithWeight(cls, node1, node2, weight):
        if node1 in cls.dictionary and node2 in cls.dictionary:
            cls.dictionary[node1].append((node2, weight))
            cls.dictionary[node2].append((node1, weight))

    def convertEgdeToWeighted(cls, node1, node2, weight):
        if node1 in cls.dictionary and node2 in cls.dictionary:
            for edge in cls.dictionary[node1]:
                if edge == node2:
                    cls.dictionary[node1].remove(edge)
                    cls.dictionary[node1].append((node2, weight))
            for edge in cls.dictionary[node2]:
                if edge == node1:
                    cls.dictionary[node2].remove(edge)
                    cls.dictionary[node2].append((node1, weight))
    def copyUnweightedAndConvertToWeightedGraph(cls, graph):
        newGraph = {}
        for node in cls.dictionary:
            newGraph[node] = []
        added_edges = set()
        for node in cls.dictionary:
            for edge in cls.dictionary[node]:
                if (node, edge) not in added_edges and (edge, node) not in added_edges:
                    newGraph[node].append((edge, 1))
                    newGraph[edge].append((node, 1))  # Add the edge in the opposite direction
                    added_edges.add((node, edge))
        return newGraph
    def allEdgesHaveWeights(cls):
        for node in cls.dictionary:
            for edge in cls.dictionary[node]:
                if len(edge) == 1:
                    return False
        return True



    def getDictionary(cls):
        return cls.dictionary

    def nodeNameExists(cls, nodeName):
        if nodeName in cls.dictionary:
            return True
        return False
    def edgeExists(cls, node1, node2):
        if node1 in cls.dictionary:
            if node2 in cls.dictionary[node1]:
                return True
        return False
    def edgeWeightExists(cls, node1, node2):
        if node1 in cls.dictionary:
            for edge in cls.dictionary[node1]:
                if edge[0] == node2 and len(edge) == 2:
                    return True
        return False

    def removeNode(self, nodeName):
        if nodeName in self.dictionary:
            del self.dictionary[nodeName]
            for node, edges in self.dictionary.items():
                self.dictionary[node] = [edge for edge in edges if edge != nodeName]

    def clearDictionary(cls):
        nodes = list(cls.dictionary.keys())
        for node in nodes:
            cls.removeNode(node)








