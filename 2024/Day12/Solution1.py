
class Graph:
    def __init__(self):
        self.root = None

    def append(self,node):
        if self.root is None:
            self.root = node
            return
        self.root.append(node)

    def print(self):
        if self.root is None:
            print("Graph is empty")
            return
        print(self.root.print())

class Node:
    def __init__(self,x,y):
        self.right_neighbor = None
        self.bottom_neighbor = None
        self.x = x
        self.y = y

    def append(self,node):
        if not node == self.right_neighbor and not node == self.bottom_neighbor:
            if node.x == self.x+1 and node.y == self.y:
                self.right_neighbor = node
                print(f"Append Node({node.x},{node.y}) to Node({self.x},{self.y})")
                return
            elif node.x == self.x and node.y == self.y+1:
                self.bottom_neighbor = node
                print(f"Append Node({node.x},{node.y}) to Node({self.x},{self.y})")
                return

            if node.x == self.right_neighbor.x+1 and node.y == self.right_neighbor.y:
                print("Try right neighbor")
                self.right_neighbor.append(node)
            elif node.x == self.bottom_neighbor.x and node.y == self.bottom_neighbor.y+1:
                print("Try bottom neighbor")
                self.bottom_neighbor.append(node)

    def print(self):
        txt = f"Node({self.x},{self.y})"
        if self.right_neighbor:
            txt += f" -> {self.right_neighbor.print()}"
        if self.bottom_neighbor:
            txt += f"\n|\nv\n{self.bottom_neighbor.print()}"

        return txt

def readInput():
    with open("example.txt","r") as file:
        return file.read()

if __name__ == '__main__':
    content = readInput().split("\n")

    graph = Graph()
    graph.append(Node(0,0))
    graph.append(Node(0,1))
    graph.append(Node(1,0))
    graph.append(Node(2,0))
    graph.append(Node(2,1))
    graph.append(Node(0,2))
    graph.append(Node(1,2))

    graph.print()