import graph
import application
import node

def main():

    gr = graph.Graph("sphere", 3000)

    origo = node.Node((0, 0, 0))
    gr.add_node(origo)

    app = application.Application(gr)
    app.animate()
    
if __name__ == "__main__":
    main()
