import array
from pickle import NONE

class Node:

    def __init__(self, coordinates : tuple, neighbours : array = [NONE]):
        
        self.position_x = coordinates[0]
        self.position_y = coordinates[1]
        self.position_z = coordinates[2]

        self.neighbours = neighbours

    def add_neighbour(self, node):
        self.neighbours.append(node)