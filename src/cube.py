import graph, node, random
from math import sqrt

class Cube(graph.Graph):
    def __init__(self, origo: tuple, number_of_nodes: int, radius: int):
        super().__init__(origo, radius)

        for i in range(number_of_nodes):

            size = round((2 * self.radius) / (sqrt(3) * 2), 0)

            x = random.randrange(-size, size)
            y = random.randrange(-size, size)
            z = random.randrange(-size, size)

            coordinate = (x, y, z)

            self.add_node(node.Node(coordinate))
