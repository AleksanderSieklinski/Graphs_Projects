import random
import networkx as nx
import graph_lib as l1
def main():
    G = l1.MyGraph.getRandomGraphNP(6, 0.3)
    G.showGraph()
    G.randomize_graph(1)
    G.showGraph()
if __name__ == "__main__":
    main()