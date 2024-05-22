from graph_lib import MyGraph
 
nValue = 10 # number of vertices
kValue = 5 # degree

generatedGraph = MyGraph.generateKRegularGraph(nValue, kValue, 0)
if generatedGraph is not None:
    generatedGraph.showGraph("kReg.png")