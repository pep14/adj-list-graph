from graph import Graph
from tkinter import *


if __name__ == "__main__":
    graph = Graph()
    canvas = Canvas(height=800, width=800)
    canvas.pack()

    graph.createNode("1", 50, 50)
    graph.createNode("2", 300, 500)
    graph.createNode("3", 100, 300)
    graph.createEdge("1", "2", 50)
    graph.createEdge("1", "3", 100)
    graph.draw(canvas)

    canvas.mainloop()