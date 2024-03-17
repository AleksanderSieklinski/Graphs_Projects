import graph_lib as l1
def main():
    sequence = [2,2,2,0]
    if l1.MyGraph.is_graphic_sequence(sequence):
        adjacency_list = l1.MyGraph.construct_graph_from_graphical(sequence)
        if adjacency_list is not None:
            G = l1.MyGraph(adjacency_list, 1)
            G.showGraph()
        else:
            print("The sequence cannot be realized by a simple graph.")
    else:
        print("The sequence is not graphic.")
if __name__ == "__main__":
    main()