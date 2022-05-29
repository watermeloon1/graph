from math import sqrt, sin, cos, isclose
import node
import random
import pygame

RADIUS = 300
ORIGO = (0, 0, 0)

def random_tuple():
    x = float(random.randrange(-RADIUS, RADIUS))
    y = float(random.randrange(-RADIUS, RADIUS))
    z = float(random.randrange(-RADIUS, RADIUS))
    return(x, y, z)

def random_coordinate():
    tuple = random_tuple()
    while RADIUS <= sqrt(pow(tuple[0], 2) + pow(tuple[1], 2) + pow(tuple[2], 2)):
        tuple = random_tuple()
    return tuple

def distance_3D(node1 : tuple , node2 : tuple):       
    x = pow(node1[0] - node2[0], 2)
    y = pow(node1[1] - node2[1], 2)
    z = pow(node1[2] - node2[2], 2)
    return sqrt(x + y + z)

def distance_2D(node1 : tuple, node2 : tuple):
    x = pow(node1[0] - node2[0], 2)
    y = pow(node1[1] - node2[1], 2)
    return sqrt(x + y)

def on_sphere(coordinates : tuple, radius : float):
    return isclose(pow((coordinates[0] - ORIGO[0]), 2) + pow((coordinates[1] - ORIGO[1]), 2) + pow((coordinates[2] - ORIGO[2]), 2), pow(radius, 2))

class Graph:
    def __init__(self, number : int):
        self.nodes = []
        print("Generating nodes...")

        for i in range(number):
            self.nodes.append(node.Node(random_coordinate()))

        self.radius_11 = distance_3D(ORIGO, self.nodes[11].get_tuple())
    
    def add_node(self, node : node.Node):
        self.nodes.append(node)

    def distance(self, n1 : int , n2 : int):    
        node1 = (self.nodes[n1].position_x, self.nodes[n1].position_y, self.nodes[n1].position_z)
        node2 = (self.nodes[n2].position_x, self.nodes[n2].position_y, self.nodes[n2].position_z)
        return distance_3D(node1, node2)

    def draw(self, screen : pygame.Surface, WINDOW_WIDTH : int, WINDOW_HEIGHT : int):

        nodes_drawn = 0

        for i in self.nodes: 
            if i.position_z < 0:
                alpha = (RADIUS - (abs(i.position_z) / 2)) / RADIUS
            elif i.position_z > 0:
                alpha = (RADIUS + (abs(i.position_z) / 2)) / RADIUS
            else: alpha = 1

            RGB = (255 - (alpha * (255 / 2)), 255 - (alpha * (255 / 2)), 255 - (alpha * (255 / 2)))

            if i == self.nodes[11]:
                pygame.draw.circle(screen, (255,0,0), ((WINDOW_WIDTH / 2 + i.position_x) , (WINDOW_HEIGHT / 2 + i.position_y)), 2 * alpha)
                nodes_drawn += 1
                continue

            if pygame.draw.circle(screen, RGB , ((WINDOW_WIDTH / 2 + i.position_x) , (WINDOW_HEIGHT / 2 + i.position_y)), 2 * alpha):
                nodes_drawn += 1

        if len(self.nodes) != nodes_drawn:
            print("ERROR: could not draw " + str(len(self.nodes) - nodes_drawn) + " nodes!")

    def rotate_X(self, length : float):

        for i in self.nodes:
            theta =length / distance_3D(ORIGO, i.get_tuple())

            sin_theta = sin(theta)
            cos_theta = cos(theta)

            pos_y = i.position_y * cos_theta + i.position_z * sin_theta
            pos_z = i.position_z * cos_theta - i.position_y * sin_theta
            
            i.position_y = pos_y
            i.position_z = pos_z

    def rotate_Y(self, length : float):

        for i in self.nodes:
            theta = length / distance_3D(ORIGO, i.get_tuple())

            sin_theta = sin(theta)
            cos_theta = cos(theta)

            pos_x = i.position_x * cos_theta + i.position_z * sin_theta
            pos_z = i.position_z * cos_theta - i.position_x * sin_theta

            i.position_x = pos_x
            i.position_z = pos_z

    def rotate_Z(self, length : float):

        for i in self.nodes:
            theta = length / distance_3D(ORIGO, i.get_tuple())

            sin_theta = sin(theta)
            cos_theta = cos(theta)

            pos_x = i.position_x * cos_theta - i.position_y * sin_theta
            pos_y = i.position_y * cos_theta + i.position_x * sin_theta
            
            i.position_x = pos_x
            i.position_y = pos_y

    def rotate_3D(self, mouse_prevoius : tuple, mouse : tuple, screen : pygame.Surface, WINDOW_WIDTH : int, WINDOW_HEIGHT : int):

        self.rotate_X(1)
        self.rotate_Y(1)
        self.rotate_Z(1)

        self.draw(screen, WINDOW_WIDTH, WINDOW_HEIGHT)