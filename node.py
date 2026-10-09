class Node:
    def __init__(self, data: str, x, y) -> None:
        self.color = 0
        self.data = data
        self.x, self.y = x, y
        self.edges: list[list[Node, float]] = []

    def recolor(self) -> None:
        self.color = 0
        edgeColors = {edge[0].color for edge in self.edges}

        # cycle through all connections, make sure theres no color match
        while self.color in edgeColors:
            self.color += 1
    
    def connect(self, node: Node, edgeValue: float) -> bool:
        if type(node) != Node:
            print("Node %s is not a node." % node)
            return False
        
        if type(edgeValue) not in (float, int):
            print("NaN: %s" % edgeValue)
            return False
        
        nodeIndex = self.findEdge(node)
        selfIndex = node.findEdge(self)

        if nodeIndex == -1:         # node not found, new connection
            self.edges.append([node, edgeValue])
            node.edges.append([self, edgeValue])
        else:                       # node found, updates connection
            self.edges[nodeIndex][1] = edgeValue
            node.edges[selfIndex][1] = edgeValue
        
        return True

    def isolate(self) -> None:
        edges = self.edges.copy()
        for edge in edges:
            node = edge[0]
            self.mutualDisconnect(node)

    def mutualDisconnect(self, node: Node) -> None:
        self.disconnect(node)
        node.disconnect(self)

    def disconnect(self, node: Node) -> None:
        i = self.findEdge(node)
        del self.edges[i]

    def findEdge(self, node: Node) -> int:
        for i, edge in enumerate(self.edges):
            if node == edge[0]:
                return i
            
        return -1