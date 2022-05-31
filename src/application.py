import pygame
import graph

class Application:
    
    def __init__(self, graph : graph.Graph):

        self.WINDOW_WIDTH = 720
        self.WINDOW_HEIGHT = 720

        self.resolution =(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(self.resolution)
        self.exit = False
        self.previous_click = None

        self.graph = graph

    def execute(self):
        pygame.init()
        self.screen.fill((255, 255, 255))

        pygame.display.set_caption('GRAPH')
        pygame.display.update()

        while not self.exit:

            for event in pygame.event.get():
                self.check_event(event)

            pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
            self.graph.draw(self.screen, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
            pygame.display.update()

        self.terminate()
    
    def check_event(self, event):
        if event.type == pygame.QUIT:
            self.exit = True

        if pygame.mouse.get_pressed()[0] and self.previous_click == None:
            self.previous_click = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] and self.previous_click != None:
            self.graph.rotate_3DM(self.previous_click, pygame.mouse.get_pos(), "th", self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
            self.previous_click = pygame.mouse.get_pos()

        if not pygame.mouse.get_pressed()[0] and self.previous_click != None:
            self.previous_click = None

        #DISTANCE
        #print(graph.distance_3D(g.nodes[11].get_tuple(), g.nodes[12].get_tuple()))
           
        #POSITION
        #print("X: " + str(g.nodes[11].position_x) + " Y: " + str(g.nodes[11].position_y) + " Z: " + str(g.nodes[11].position_z) + " R: " + str(graph.distance_3D(g.nodes[11].get_tuple(), graph.ORIGO)) + " O: " + str(g.radius_11) + " " + str(graph.on_sphere(g.nodes[11].get_tuple(), g.radius_11)))

    def terminate(self):
        pygame.quit()
        quit()