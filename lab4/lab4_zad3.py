import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def generateRandomStronglyConnectedDigraph(n, K): # n - liczba wierzchołków, k - liczba krawędzi
	if K < n or K > n * (n-1):
		raise ValueError("Invalid number of edges. Must be between n and n*(n-1)")
	
	g = nx.DiGraph()
	g.add_nodes_from(range(n))

	# create basic cycle
	vertices = list(g.nodes)
	np.random.shuffle(vertices)
	for a, b in zip(vertices[:len(vertices)-1], vertices[1:]):
		# add edge from a to b with random weight between -4 and 11
		g.add_edge(a, b, weight=np.random.randint(-4, 12))
	g.add_edge(vertices[-1], vertices[0], weight=np.random.randint(-4, 12))

	# calculate how many edges we still need to add
	K -= g.number_of_edges()

	# add random edges
	while K > 0:
		a = np.random.choice(vertices)
		b = np.random.choice(vertices)
		if a != b and not g.has_edge(a, b):
			g.add_edge(a, b, weight=np.random.randint(-4, 12))
			K -= 1

	return g


def bellmanFord(g, source):
	v = list(g.nodes)
	v = {vi: [np.inf, None] for vi in v}  # (Vertex, Distance, Predecessor)
	edges = list(g.edges(data=True)) # list of edges with weights
	v_mod = len(v) # number of vertices
	v[source][0] = 0 # set distance from source to source to 0

	# Relaxation
	for i in range(v_mod-1):
		for edge in edges:
			u, w, data = edge
			if v[u][0] + data['weight'] < v[w][0]:
				v[w][0] = v[u][0] + data['weight']
				v[w][1] = u
	for edge in edges:
		u, w, data = edge
		if v[u][0] + data['weight'] < v[w][0]:
			# find negative weight cycle
			print("Graph contains a negative weight cycle:")
			visited = [False] * v_mod
			visited[w] = True
			while not visited[u]:
				visited[u] = True
				u = v[u][1]
			ncycle = [u]
			v1 = v[u][1]
			while v1 != u:
				ncycle = [v1] + ncycle
				v1 = v[v1][1]

			print(ncycle)
			return None
	return v

def testGraph():
	g = nx.DiGraph()
	g.add_nodes_from(range(5))
	g.add_edge(0, 1, weight=6)
	g.add_edge(0, 2, weight=7)
	g.add_edge(1, 2, weight=8)
	g.add_edge(1, 3, weight=5)
	g.add_edge(1, 4, weight=-4)
	g.add_edge(2, 3, weight=-3)
	g.add_edge(2, 4, weight=9)
	g.add_edge(3, 1, weight=-2)
	g.add_edge(3, 4, weight=7)

	return g

if __name__ == '__main__':
	g = generateRandomStronglyConnectedDigraph(7, 15)
	# g = testGraph()
	# draw graph with wages, vertices on circle

	pos = nx.circular_layout(g)
	nx.draw(g, pos, with_labels=True)
	edge_labels=dict([((u,v,),d['weight'])
    for u,v,d in g.edges(data=True)])
	nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)
	plt.savefig('lab4_zad3.png')

	source = 0

	bl_dic = bellmanFord(g, source)

	if bl_dic is not None:
		for k, v in bl_dic.items():
			print(f"{source} -> {k}, Distance: {v[0]}, Predecessor: {v[1]}")
