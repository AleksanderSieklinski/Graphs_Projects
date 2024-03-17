from graph_lib import MyGraph

def generate_k_regular_graph(n, k): # n - ilość wierzchołków, k - stopień
    if n <= k:
        print("n must be greater than k")
        return None
    if k*n % 2 != 0:
        print("k*n must be even")
        return None
    
    # ciąg stopni wierzchołków
    degree_sequence = [[i, k] for i in range(n)] # i - wierzchołek, k - stopień wierzchołka
    adj_list = [ [] for i in degree_sequence]
    print(degree_sequence)
    

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
        print(degree_sequence)
    g = MyGraph(adj_list,1)
    g.saveFigure("k_regular_graph.png")
    g.randomize_graph(100) # tu się psuje
    g.saveFigure("k_regular_graph_random.png")
    return g

if __name__ == "__main__":
	n_value = 4  # Ilość wierzchołków
	k_value = 2  # Stopień
    
	generated_graph = generate_k_regular_graph(n_value, k_value)
	if generated_graph is not None:
		generated_graph.saveFigure("k_regular_graph_random.png")