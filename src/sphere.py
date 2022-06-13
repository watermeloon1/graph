import graph, node, random
from math import cos, sin, acos, pi

class Sphere(graph.Graph):
    
    def __init__(self, origo: tuple, number_of_nodes: int, radius: int):
        super().__init__(origo, radius)

        for i in range(number_of_nodes):
            v = random.random()
            u = random.random()
            r = random.random() ** (1./3.)

            theta = u * 2.0 * pi
            phi = acos(2.0 * v - 1.0)
            sin_theta = sin(theta)
            cos_theta = cos(theta)
            sin_phi = sin(phi)
            cos_phi = cos(phi)

            x = r * sin_phi * cos_theta * self.radius
            y = r * sin_phi * sin_theta * self.radius
            z = r * cos_phi * self.radius

            coordinate = (x, y, z)

            self.add_node(node.Node(coordinate))
