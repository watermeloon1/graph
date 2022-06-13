import graph, node
from math import cos, sin, sqrt, pi

class Globe(graph.Graph):
    def __init__(self, origo: tuple, number_of_nodes: int, radius):
        super().__init__(origo, radius)

        phi = pi * (3. - sqrt(5.))

        for i in range(number_of_nodes):
            y = 1 - (i / float(number_of_nodes - 1)) * 2
            radius = sqrt(1 - y * y)

            theta = phi * i

            x = cos(theta) * radius
            z = sin(theta) * radius

            coordinate = (self.radius * x, self.radius * y, self.radius * z)

            self.add_node(node.Node(coordinate))

