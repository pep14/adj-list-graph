class Node:
    def __init__(self, data, x, y) -> None:
        self.data = data
        self.x, self.y = x, y
        self.edges = []
    
    def connect(self, node: Node, edgeValue: float) -> bool:
        if type(node) != Node:
            print("Node %s is not a node." % node)
            return False
        
        if type(edgeValue) not in (float, int):
            print("NaN %s" % edgeValue)
            return False
        
        othernIndex = self.findEdge(node)
        mutualIndex = node.findEdge(self)

        if othernIndex == -1:
            self.edges.append([node, edgeValue])
            node.edges.append([self, edgeValue])
        else:
            self.edges[othernIndex][1] = edgeValue
            node.edges[mutualIndex][1] = edgeValue
        
        return True
    
    def findEdge(self, node: Node) -> int:
        for i, edge in enumerate(self.edges):
            if node == edge[0]:
                return i
            
        return -1