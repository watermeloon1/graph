import string, node, pygame, array
from math import sqrt, sin, cos

def distance_3D(node1 : tuple , node2 : tuple):       
    x = pow(node1[0] - node2[0], 2)
    y = pow(node1[1] - node2[1], 2)
    z = pow(node1[2] - node2[2], 2)
    
    return sqrt(x + y + z)

class Graph:
    def __init__(self, origo: tuple, radius: int):
        
        self.nodes: array = []
        self.origo = origo
        self.radius: int = radius

    def check_coordinates(self):
        for i in self.nodes:
            if not -self.radius < i.position_x < self.radius or not -self.radius < i.position_y < self.radius or not -self.radius < i.position_z < self.radius:
                print("ERROR: failed to initalise points!")

    def add_node(self, node : node.Node):
        self.nodes.append(node)

    def distance(self, n1 : int , n2 : int):    
        node1 = (self.nodes[n1].position_x, self.nodes[n1].position_y, self.nodes[n1].position_z)
        node2 = (self.nodes[n2].position_x, self.nodes[n2].position_y, self.nodes[n2].position_z)
        
        return distance_3D(node1, node2)

    def draw(self, screen : pygame.Surface, camera : tuple, WINDOW_WIDTH : int, WINDOW_HEIGHT : int):

        zoom = self.radius / camera.position_z

        for i in self.nodes:

            draw_x = (WINDOW_WIDTH / 2 + self.origo[0]) + (i.position_x * zoom)
            draw_y = (WINDOW_HEIGHT / 2 - self.origo[1]) + (i.position_y * zoom)

            if 0 < draw_x <= WINDOW_WIDTH and 0 < draw_y <= WINDOW_HEIGHT:
                
                #relative_position_z = i.position_z + self.origo[2]

                #TODO: viewdistance

                if i.position_z < self.origo[2]:
                    alpha = (self.radius - (abs(i.position_z) / 2)) / self.radius
                elif i.position_z > self.origo[2]:
                    alpha = (self.radius + (abs(i.position_z) / 2)) / self.radius
                else: alpha = 1

                RGB = (255 - (alpha * (255 / 2)), 255 - (alpha * (255 / 2)), 255 - (alpha * (255 / 2)))
                
                if not pygame.draw.circle(screen, RGB , (draw_x , draw_y), 2 * alpha):
                    print("ERROR: could not draw node " + str(i) + "!")

                if i.position_x == 0 and i.position_y == 0 and i.position_z == 0:
                    pygame.draw.circle(screen, (255, 0, 0) , (draw_x , draw_y), 2)
            
        #TRACE
        #print("X1: " + str(self.nodes[0].position_x) + " Y1: " + str(self.nodes[0].position_y) + " X2: " + str(self.nodes[1].position_x) + str(" Y2: " + str(self.nodes[1].position_y)))
        
        #EDGE
        #pygame.draw.line(screen, (200,200,200) , (WINDOW_WIDTH / 2 + self.nodes[0].position_x, WINDOW_HEIGHT / 2 + self.nodes[0].position_y), (WINDOW_WIDTH / 2 +self.nodes[1].position_x, WINDOW_HEIGHT / 2 +self.nodes[1].position_y) )

    def safe_theta(self, param : float, coordinate : tuple):
        if self.origo == coordinate:
            return 0
        else: return param / distance_3D(self.origo, coordinate)

    def rotate_X(self, param : float, type : string):

        for i in self.nodes:
            
            if type == "cl":
                theta = self.safe_theta(param, i.get_tuple())
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
                theta = self.safe_theta(param, i.get_tuple())
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
                theta = self.safe_theta(param, i.get_tuple())
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
            speed = 0.008
        else: speed = 1
        
        mouse_x = speed * ((WINDOW_WIDTH - previous_click[1]) - (WINDOW_WIDTH - click[1]))
        mouse_y = speed * ((WINDOW_HEIGHT - previous_click[0]) - (WINDOW_HEIGHT - click[0]))

        self.rotate_X(mouse_x, param_type)
        self.rotate_Y(mouse_y, param_type)

    def rotate_3DA(self, param : float, param_type : string):

        if not (param_type == "cl" or param_type == "th"):
            print("ERROR: invalid arguments for rotation!")
            return
        
        self.rotate_X(param, param_type)
        self.rotate_Y(param, param_type)
        self.rotate_Z(param, param_type)