from graph_lib import MyGraph

if __name__ == "__main__":
    #Example of usage
    G = MyGraph()
    B = MyGraph.getRandomGraphNL(10, 7)
    B.showGraph()
    colored, index = B.findBiggestConnectedComponent()
    print(B)
    print(colored)
    print(index)