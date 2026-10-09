from graph import Graph
from tkinter import *


NODE_SIZE = 15


class Main(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.graph = Graph()
        self.selectedData = None

        self.l1 = Label(self, text="new vertex name")
        self.e1 = Entry(self)
        self.l1.grid(row=0, column=0)
        self.e1.grid(row=0, column=1)

        self.l2 = Label(self, text="edge value (float)")
        self.e2 = Entry(self)
        self.l2.grid(row=1, column=0)
        self.e2.grid(row=1, column=1)

        self.b1 = Button(
            self,
            text="clear",
            command=self.clear
        )
        self.b1.grid(row=2, column=0, columnspan=2)

        self.canvas = Canvas(
            self,
            height=800,
            width=800
        )
        self.canvas.grid(row=0, column=2, rowspan=50)

        self.canvas.bind("<Button-1>", self.createNode)
        self.canvas.bind("<Button-2>", self.removeNode)
        self.canvas.bind("<Button-3>", self.selectNode)

        self.graph.draw(self.canvas)

    def getNodeAt(self, x, y) -> str | None:
        for data, node in self.graph.nodes.items():
            dx = node.x - x
            dy = node.y - y

            if dx**2 + dy**2 <= NODE_SIZE**2:
                return data

        return None

    def selectNode(self, event) -> None:
        data = self.getNodeAt(event.x, event.y)

        if data == None:
            return
        
        if self.selectedData == None:
            self.selectedData = data
            return
        
        if self.selectedData != data:
            self.createEdge(
                data0=self.selectedData,
                data1=data
            )
            self.selectedData = None

    def createNode(self, event) -> None:
        x, y = event.x, event.y

        if self.getNodeAt(x, y) == None:
            self.graph.createNode(self.e1.get(), event.x, event.y)
            self.graph.draw(self.canvas)

    def removeNode(self, event) -> None:
        data = self.getNodeAt(event.x, event.y)
       
        if data != None:
            self.graph.removeNode(data)

        self.graph.draw(self.canvas)

    def createEdge(self, data0, data1) -> None:
        rawValue = self.e2.get()

        try:
            edgeValue = float(rawValue)
        except:
            edgeValue = 0

        self.graph.createEdge(
            data0=data0,
            data1=data1,
            edgeValue=edgeValue
        )
        self.graph.draw(self.canvas)

    def clear(self) -> None:
        self.graph.nodes = {}
        self.graph.draw(self.canvas)


if __name__ == "__main__":
    root = Main()
    root.mainloop()