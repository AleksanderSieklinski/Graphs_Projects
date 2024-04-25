import graph_lib as l1

if __name__ == "__main__":
    n=6
    graph = l1.MyGraph.getRandomConnectedWeightedGraph(n, 7)

    paths = l1.MyGraph.dijkstra(graph, 0)

    for target, path, length in paths:
        print(f"Do wierzchołka {target}: Ścieżka {path}, Długość:  {int(length)}")
    print()

    distance_matrix = graph.all_pairs_shortest_path(n)
    for row in distance_matrix:
        for element in row:
            print(f"{element[2]}\t", end=" ")
        print()
    graph.showWeightedGraph()
    


