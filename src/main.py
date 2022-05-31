import graph
import pygame

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

pygame.init()

resolution =(WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(resolution)
screen.fill((255,255,255))

pygame.display.set_caption('GRAPH')
pygame.display.update()

def main():

    g = graph.Graph("cube", 5000)

    previous_click = None
    exit = False
    while not exit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit = True

            if pygame.mouse.get_pressed()[0] and previous_click == None:
                previous_click = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0] and previous_click != None:
                g.rotate_3DM(previous_click, pygame.mouse.get_pos(), "th", WINDOW_WIDTH, WINDOW_HEIGHT)
                previous_click = pygame.mouse.get_pos()

            if not pygame.mouse.get_pressed()[0] and previous_click != None:
                previous_click = None

        pygame.draw.rect(screen, (255, 255, 255), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        g.draw(screen, WINDOW_WIDTH, WINDOW_HEIGHT)

            #DISTANCE
            #print(graph.distance_3D(g.nodes[11].get_tuple(), g.nodes[12].get_tuple()))
           
           #POSITION
            #print("X: " + str(g.nodes[11].position_x) + " Y: " + str(g.nodes[11].position_y) + " Z: " + str(g.nodes[11].position_z) + " R: " + str(graph.distance_3D(g.nodes[11].get_tuple(), graph.ORIGO)) + " O: " + str(g.radius_11) + " " + str(graph.on_sphere(g.nodes[11].get_tuple(), g.radius_11)))

        pygame.display.update()

    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()
