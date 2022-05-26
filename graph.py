from cmath import pi
from math import sqrt
import node
import random

RADIUS = 250

def random_tuple():
    x = random.randrange(-RADIUS, RADIUS)
    y = random.randrange(-RADIUS, RADIUS)
    z = random.randrange(-RADIUS, RADIUS)
    return(x, y, z)

def random_coordinate():
    tuple = random_tuple()
    while RADIUS <= sqrt(pow(tuple[0], 2) + pow(tuple[1], 2) + pow(tuple[2], 2)):
        tuple = random_tuple()
    return tuple

class Graph:
    def __init__(self, number : int):
        self.nodes = []
        print("Generating nodes...")

        for i in range(number):
            self.nodes.append(node.Node(random_coordinate()))
    
    def add_node(self, node : node.Node):
        self.nodes.append(node)

    def distance(self, n1 : int , n2 : int):        
        
        x = pow(self.nodes[n1].position_x - self.nodes[n2].position_x, 2)
        y = pow(self.nodes[n1].position_y - self.nodes[n2].position_y, 2)
        z = pow(self.nodes[n1].position_z - self.nodes[n2].position_z, 2)

        return sqrt(x + y + z)
