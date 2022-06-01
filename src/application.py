import pygame
import graph
import camera

class Application:
    
    def __init__(self, graph : graph.Graph):
        pygame.init()

        self.WINDOW_WIDTH = 720
        self.WINDOW_HEIGHT = 720
        self.fps = 60

        self.resolution =(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(self.resolution)
        self.exit = False
        self.previous_click = None

        self.graph = graph
        self.camera = camera.Camera((0, 0, 300))
        self.clock = pygame.time.Clock()

    def animate(self):
        self.screen.fill((255, 255, 255))

        pygame.display.set_caption('GRAPH')
        pygame.display.update()

        while not self.exit:
            for event in pygame.event.get():
                self.check_event(event)

            pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
            self.graph.draw(self.screen, self.camera, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
            pygame.display.update()
            self.clock.tick(self.fps)

        self.terminate()
    
    def check_event(self, event):
        if event.type == pygame.QUIT:
            self.exit = True

        if pygame.key.get_pressed()[pygame.K_MINUS]:
            self.camera.zoom(-5)

        if pygame.key.get_pressed()[pygame.K_PERIOD]:
            self.camera.zoom(+5)

        if pygame.mouse.get_pressed()[0] and self.previous_click == None:
            self.previous_click = pygame.mouse.get_pos()

        elif pygame.mouse.get_pressed()[0] and self.previous_click != None:
            self.graph.rotate_3DM(self.previous_click, pygame.mouse.get_pos(), "th", self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
            self.previous_click = pygame.mouse.get_pos()

        elif not pygame.mouse.get_pressed()[0] and self.previous_click != None:
            self.previous_click = None

    def terminate(self):
        pygame.quit()
        quit()