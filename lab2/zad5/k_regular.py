from adjacencyIncidenceMatrixes import MyGraph

# DRAFT

def generate_k_regular_graph(n, k):
    if n <= k:
        print("n must be greater than k")
        return None
    if k % 2 != 0 and n % 2 != 0:
        print("n must be even")
        return None
    
    # ciąg stopni wierzchołków
    degree_sequence = [[i, k] for i in range(n)] # i - wierzchołek, k - stopień wierzchołka
    adj_list = [ [] for i in degree_sequence]

    while True:
        # sprawdzamy czy w degree_sequence stopnie wierzchołków są równe k
        if all(i[1] == 0 for i in degree_sequence):
            break
        for i in range(1, degree_sequence[0][1] + 1):
            degree_sequence[i][1] -= 1
            # dodajemy krawędź między wierzchołkami a i b
            a = degree_sequence[0][0]
            b = degree_sequence[i][0]
            adj_list[a].append(b)    
            adj_list[b].append(a)        

        degree_sequence[0][1] = 0
        
        degree_sequence.sort(reverse=True, key=lambda x: x[1])

    return MyGraph(adj_list, 1)

if __name__ == "__main__":
	n_value = 5  # Ilość wierzchołków
	k_value = 4  # Stopień

	generated_graph = generate_k_regular_graph(n_value, k_value)
	generated_graph.saveFigure("k_regular_graph.png")