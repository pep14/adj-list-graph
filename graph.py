from node import Node
import tkinter as tk
import random
import heapq


NODE_SIZE = 15


class Graph:
    def __init__(self) -> None:
        self.colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"]
        self.nodes: dict[str, Node] = {}

    def createNode(self, data: str, x, y) -> None:
        if data not in self.nodes:
            self.nodes[data] = Node(data, x, y)
        else:
            print("%s already exists." % data)

    def removeNode(self, data: str) -> None:
        self.nodes[data].isolate()
        del self.nodes[data]

    def createEdge(self, data0: str, data1: str, edgeValue: float) -> None:
        if  data0 in self.nodes and \
            data1 in self.nodes:
            self.nodes[data0].connect(self.nodes[data1], edgeValue)
        else:
            print("Node pair does not exist.")  

    def draw(self, canvas: tk.Canvas) -> None:
        canvas.delete("all")

        for node in self.nodes.values():
            for edge in node.edges:
                adj = edge[0]

                ax = (node.x + adj.x) // 2
                ay = (node.y + adj.y) // 2

                canvas.create_line(node.x, node.y, adj.x, adj.y, fill="#aaaaaa")
                canvas.create_text(ax, ay, text=edge[1])

        # reset colors
        for node in self.nodes.values():
            node.color = -1

        for node in self.nodes.values():
            node.recolor()

            # add new color
            if len(self.colors) == node.color:
                r = lambda: random.randint(0,255)
                self.colors.append("#%02X%02X%02X" % (r(), r(), r()))

            canvas.create_oval(node.x-NODE_SIZE, node.y-NODE_SIZE, node.x+NODE_SIZE, node.y+NODE_SIZE, fill=self.colors[node.color])
            canvas.create_text(node.x, node.y, text=node.data)

    def primMST(self, node: Node | None = None) -> tuple[set, list]:
        if not node:
            node = next(iter(self.nodes.values()))

        mem = {node.data}
        connections = []
        edges = []

        for adj, value in node.edges:
            heapq.heappush(
                edges,
                (value, node.data, adj)
            )

        while edges and len(mem) < len(self.nodes):
            value, current, adj = heapq.heappop(edges)

            if adj.data in mem:
                continue

            mem.add(adj.data)
            connections.append([current, adj.data, value])

            for neighbor, edge_weight in adj.edges:
                if neighbor.data not in mem:
                    heapq.heappush(
                        edges,
                        (edge_weight, adj.data, neighbor)
                    )

        return mem, connections
    
    def kruskalMST(self):
        edges = []

        for node in self.nodes.values():
            for adj, value in node.edges:
                edges.append((node.data, adj.data, value))

        edges.sort(key=lambda x: x[2])

        parent = {}
        weight = {}

        for node in self.nodes.values():
            data = node.data
            parent[data] = data
            weight[data] = 0

        def findAncestor(x):
            if parent[x] != x:
                parent[x] = findAncestor(parent[x])

            return parent[x]

        def unify(a, b):
            ancA = findAncestor(a)
            ancB = findAncestor(b)

            if ancA == ancB:
                return False

            if weight[ancA] < weight[ancB]:
                ancA, ancB = ancB, ancA

            parent[ancB] = ancA

            if weight[ancA] == weight[ancB]:
                weight[ancA] += 1

            return True

        connections = []

        for current, adj, value in edges:
            if unify(current, adj):
                connections.append([current, adj, value])

                if len(connections) == len(self.nodes) - 1:
                    break

        return None, connections

    
    def drawMST(self, canvas: tk.Canvas, alg: int) -> None:
        match alg:
            case 0:
                mem, MST = self.primMST()
            case 1:
                mem, MST = self.kruskalMST()

        print("MST: %s\nmem: %s" % (MST, mem))

        for connection in MST:
            node = self.nodes[connection[0]]
            adj  = self.nodes[connection[1]]

            canvas.create_line(node.x, node.y, adj.x, adj.y, fill="#ff0000", width=5, tags="MST")