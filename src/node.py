import array

class Node:

    def __init__(self, coordinates : tuple, neighbours : array = [None]):
        
        self.position_x = coordinates[0]
        self.position_y = coordinates[1]
        self.position_z = coordinates[2]

        self.neighbours = neighbours

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def get_tuple(self):
        return (self.position_x, self.position_y, self.position_z)