import application, node, globe, sphere, cube

def main():

    origo = (400, 0, 0)
    graph = globe.Globe(origo, 500, 250)

    app = application.Application(graph)
    app.animate()
    
if __name__ == "__main__":
    main()
