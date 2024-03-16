import graph_lib as l1
def main():
    G = l1.MyGraph.getRandomGraphNP(10, 0.6)
    G.showGraph()
    print("Graph center: ", G.get_graph_center())
    print("Minimax center: ", G.get_minimax_center())
if __name__ == "__main__":
    main()