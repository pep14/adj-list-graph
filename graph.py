from node import Node
import tkinter as tk


NODE_SIZE = 15


class Graph:
    def __init__(self):
        self.colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"]
        self.nodes: dict[str, Node] = {}

    def createNode(self, data: str, x, y):
        if data not in self.nodes:
            self.nodes[data] = Node(data, x, y)
        else:
            print("%s already exists." % data)

    def createEdge(self, data0: str, data1: str, edgeValue: float):
        if  data0 in self.nodes and \
            data1 in self.nodes:
            self.nodes[data0].connect(self.nodes[data1], edgeValue)
        else:
            print("Node pair does not exist.")

    def removeNode(self, data: str):
        self.nodes[data].isolate()
        del self.nodes[data]

    def draw(self, canvas: tk.Canvas):
        canvas.delete("all")

        for node in self.nodes.values():
            for edge in node.edges:
                adj = edge[0]

                ax = (node.x + adj.x) // 2
                ay = (node.y + adj.y) // 2

                canvas.create_line(node.x, node.y, adj.x, adj.y, fill="#aaaaaa")
                canvas.create_text(ax, ay, text=edge[1])

        for node in self.nodes.values():
            node.recolor()

            canvas.create_oval(node.x-NODE_SIZE, node.y-NODE_SIZE, node.x+NODE_SIZE, node.y+NODE_SIZE, fill=self.colors[node.color])
            canvas.create_text(node.x, node.y, text=node.data)