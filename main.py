import node
import graph
import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

pygame.init()
resolution =(WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('GRAPH')
screen.fill((255,255,255))
pygame.display.update()

def draw_node(position_x : float, position_y : float, position_z : float):
    if position_z < 0:
        alpha = (graph.RADIUS - (abs(position_z) / 2)) / graph.RADIUS
    if position_z > 0:
        alpha = (graph.RADIUS + (abs(position_z) / 2)) / graph.RADIUS
    if position_z == 0:
        alpha = 1

    pygame.draw.circle(screen, (0,0,0), ((WINDOW_WIDTH / 2 + position_x) , (WINDOW_HEIGHT / 2 + position_y)), 2 * alpha)

def main():

    g = graph.Graph(4000)

    n1 = node.Node((0,0,0))
    n2 = node.Node((1,1,5))

    g.add_node(n1)
    g.add_node(n2)

    print(g.distance(10,11))

    for i in range(len(g.nodes)):
        draw_node(g.nodes[i].position_x, g.nodes[i].position_y, g.nodes[i].position_z)

    exit = False
    while not exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()

    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()
