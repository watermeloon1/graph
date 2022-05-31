import graph
import application

def main():

    gr = graph.Graph("cube", 3000)
    app = application.Application(gr)
    app.execute()
    
if __name__ == "__main__":
    main()
