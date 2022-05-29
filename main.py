import graph
import pygame

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

pygame.init()
resolution =(WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('GRAPH')
screen.fill((255,255,255))
pygame.display.update()

def main():

    g = graph.Graph(500)
    g.draw(screen, WINDOW_WIDTH, WINDOW_HEIGHT)

    #n1 = node.Node((0,0,0))
    #n2 = node.Node((1,1,5))
    #g.add_node(n1)
    #g.add_node(n2)

    #pressed = False
    previous_click = None
    exit = False
    stop = False
    while not exit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit = True

            if pygame.mouse.get_pressed()[0] and previous_click == None:
                previous_click = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0] and previous_click != None:
                #pygame.draw.rect(screen, (255, 255, 255), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
                #g.rotate_3D(previous_click, pygame.mouse.get_pos(), screen, WINDOW_WIDTH, WINDOW_HEIGHT)
                previous_click = pygame.mouse.get_pos()
                stop = not stop

            if not pygame.mouse.get_pressed()[0] and previous_click != None:
                previous_click = None

        if not stop:
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
            g.rotate_3D((0,0,0), (0,0,0), screen, WINDOW_WIDTH, WINDOW_HEIGHT)       
            print("X: " + str(g.nodes[11].position_x) + " Y: " + str(g.nodes[11].position_y) + " Z: " + str(g.nodes[11].position_z) + " R: " + str(graph.distance_3D(g.nodes[11].get_tuple(), graph.ORIGO)) + " O: " + str(g.radius_11) + " " + str(graph.on_sphere(g.nodes[11].get_tuple(), g.radius_11)))
    
        pygame.display.update()

    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()
