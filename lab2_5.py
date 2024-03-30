from graph_lib import MyGraph

if __name__ == "__main__":
    nValue = 4  # number of vertices
    kValue = 2  # degree
    
    generatedGraph = MyGraph.generateKRegularGraph(nValue, kValue)
    if generatedGraph is not None:
        generatedGraph.showGraph("kRegularGraphRandom.png")