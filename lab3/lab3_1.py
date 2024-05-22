from graph_lib import MyGraph

if __name__ == "__main__":
    #Example of usage
    G = MyGraph()
    B = MyGraph.getRandomConnectedWeightedGraph(5, 4)
    B.showWeightedGraph()
    print(B)
    print(B.weightMatrix)