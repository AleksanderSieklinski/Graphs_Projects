import graph_lib as l1
def main():
    sequence = [4,3,3,2,2,1,1]
    if l1.MyGraph.isGraphicSequence(sequence):
        adjacency_list = l1.MyGraph.constructGraphFromGraphical(sequence)
        if adjacency_list is not None:
            G = l1.MyGraph(adjacency_list, 1)
            G.showGraph()
        else:
            print("The sequence cannot be realized by a simple graph.")
    else:
        print("The sequence is not graphic.")
if __name__ == "__main__":
    main()