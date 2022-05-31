from math import sqrt, sin, cos, isclose, pi, acos
import string
import node
import random
import pygame

RADIUS = 250
ORIGO = (0, 0, 0)

def random_coordinate_C():    
    size = round((2 * RADIUS) / (sqrt(3) * 2), 0)

    x = random.randrange(-size, size)
    y = random.randrange(-size, size)
    z = random.randrange(-size, size)

    return (x, y, z)

def random_coordinate_S():
    u = random.random()
    v = random.random()
    r = random.random() ** (1./3.)

    theta = u * 2.0 * pi
    phi = acos(2.0 * v - 1.0)
    sin_theta = sin(theta)
    cos_theta = cos(theta)
    sin_phi = sin(phi)
    cos_phi = cos(phi)

    x = r * sin_phi * cos_theta * RADIUS
    y = r * sin_phi * sin_theta * RADIUS
    z = r * cos_phi * RADIUS

    return (x, y, z)

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
    def __init__(self, shape : string, number : int):

        self.nodes = []
        
        if not (shape == "sphere" or shape == "cube"):
            print("ERROR: invalid string argument for graph type!")
            return

        if shape == "sphere":
            for i in range(number):
                coordinate = random_coordinate_S()
                self.nodes.append(node.Node(coordinate))
        else:
            for i in range(number):
                coordinate = random_coordinate_C()
                self.nodes.append(node.Node(coordinate))

        self.radius_11 = distance_3D(ORIGO, self.nodes[11].get_tuple())
    
    def check_coordinates(self):
        for i in self.nodes:
            if not -RADIUS < i.position_x < RADIUS or not -RADIUS < i.position_y < RADIUS or not -RADIUS < i.position_z < RADIUS:
                print("ERROR: failed to initalise points!")

    def add_node(self, node : node.Node):
        self.nodes.append(node)

    def distance(self, n1 : int , n2 : int):    
        node1 = (self.nodes[n1].position_x, self.nodes[n1].position_y, self.nodes[n1].position_z)
        node2 = (self.nodes[n2].position_x, self.nodes[n2].position_y, self.nodes[n2].position_z)
        
        return distance_3D(node1, node2)

    def draw(self, screen : pygame.Surface, WINDOW_WIDTH : int, WINDOW_HEIGHT : int):

        for i in self.nodes: 

            if i.position_z < 0:
                alpha = (RADIUS - (abs(i.position_z) / 2)) / RADIUS
            elif i.position_z > 0:
                alpha = (RADIUS + (abs(i.position_z) / 2)) / RADIUS
            else: alpha = 1

            RGB = (255 - (alpha * (255 / 2)), 255 - (alpha * (255 / 2)), 255 - (alpha * (255 / 2)))

            if i == self.nodes[11] or i == self.nodes[12]:
                pygame.draw.circle(screen, (255,0,0), ((WINDOW_WIDTH / 2 + i.position_x) , (WINDOW_HEIGHT / 2 + i.position_y)), 2 * alpha)
                continue

            if not pygame.draw.circle(screen, RGB , ((WINDOW_WIDTH / 2 + i.position_x) , (WINDOW_HEIGHT / 2 + i.position_y)), 2 * alpha):
                print("ERROR: could not draw node " + str(i) + "!")
            
        #TRACE
        #print("X1: " + str(self.nodes[0].position_x) + " Y1: " + str(self.nodes[0].position_y) + " X2: " + str(self.nodes[1].position_x) + str(" Y2: " + str(self.nodes[1].position_y)))
        
        #EDGE
        #pygame.draw.line(screen, (200,200,200) , (WINDOW_WIDTH / 2 + self.nodes[0].position_x, WINDOW_HEIGHT / 2 + self.nodes[0].position_y), (WINDOW_WIDTH / 2 +self.nodes[1].position_x, WINDOW_HEIGHT / 2 +self.nodes[1].position_y) )

    def rotate_X(self, param : float, type : string):

        for i in self.nodes:
            
            if type == "cl":
                theta = param / distance_3D(ORIGO, i.get_tuple())
            else: theta = param

            sin_theta = sin(theta)
            cos_theta = cos(theta)

            pos_y = i.position_y * cos_theta + i.position_z * sin_theta
            pos_z = i.position_z * cos_theta - i.position_y * sin_theta
            
            i.position_y = pos_y
            i.position_z = pos_z

    def rotate_Y(self, param : float, type : string):

        for i in self.nodes:

            if type == "cl":
                theta = param / distance_3D(ORIGO, i.get_tuple())
            else: theta = param

            sin_theta = sin(theta)
            cos_theta = cos(theta)

            pos_x = i.position_x * cos_theta + i.position_z * sin_theta
            pos_z = i.position_z * cos_theta - i.position_x * sin_theta

            i.position_x = pos_x
            i.position_z = pos_z

    def rotate_Z(self, param : float, type : string):

        for i in self.nodes:
            
            if type == "cl":
                theta = param / distance_3D(ORIGO, i.get_tuple())
            else: theta = param

            sin_theta = sin(theta)
            cos_theta = cos(theta)

            pos_x = i.position_x * cos_theta - i.position_y * sin_theta
            pos_y = i.position_y * cos_theta + i.position_x * sin_theta
            
            i.position_x = pos_x
            i.position_y = pos_y

    def rotate_3DM(self, previous_click : tuple, click : tuple, param_type : string, WINDOW_WIDTH : int, WINDOW_HEIGHT : int):

        if not (param_type == "cl" or param_type == "th"):
            print("ERROR: invalid arguments for rotation!")
            return
        
        if param_type == "th":
            speed = 0.01
        else: speed = 1
        
        mouse_x = speed * ((WINDOW_WIDTH - previous_click[1]) - (WINDOW_WIDTH - click[1]))
        mouse_y = speed * ((WINDOW_HEIGHT - previous_click[0]) - (WINDOW_HEIGHT - click[0]))

        self.rotate_X(mouse_x, param_type)
        self.rotate_Y(mouse_y, param_type)

    def rotate_3DA(self, param : tuple, param_type : string):

        if not (param_type == "cl" or param_type == "th"):
            print("ERROR: invalid arguments for rotation!")
            return
        
        self.rotate_X(param, param_type)
        self.rotate_Y(param, param_type)
        self.rotate_Z(param, param_type)