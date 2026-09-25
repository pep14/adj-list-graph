class Node:
    def __init__(self, data: str, x, y) -> None:
        self.data = data
        self.x, self.y = x, y
        self.edges: list[list[Node, float]] = []
    
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
    
    def findEdge(self, node: Node) -> int:
        for i, edge in enumerate(self.edges):
            if node == edge[0]:
                return i
            
        return -1
    
    def draw(self, canvas, visited: list[str]):
        visited.append(self.data)

        for edge in self.edges:
            node = edge[0]
            if node.data not in visited:
                canvas.create_line(node.x, node.y, self.x, self.y)

                ax = (node.x + self.x) // 2
                ay = (node.y + self.y) // 2

                node.draw(canvas, visited)

        canvas.create_oval(self.x-15, self.y-15, self.x+15, self.y+15)
        canvas.create_text(self.x, self.y, self.data)