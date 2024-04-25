import networkx as nx
import matplotlib.pyplot as plt
import graph_lib as gl
import numpy as np

def getNumberOfEdgesFromMatrix(matrix):
	edges = 0
	for i in range(len(matrix)):
		for j in range(i, len(matrix)):
			if matrix[i][j] != 0:
				edges += 1
	return edges

def kruskal_algorithm(graph):
	
	matrix = graph.getWeightMatrix()
	node = len(matrix)
	edges = [] # krawedzie w postaci (v1, v2, waga)
	nodes = {} # para (wierzcholek, kolor)
	color = 0
	matrixSpanningTree = np.zeros_like(matrix) # macierz sasiedztwa (z wagami) dla grafu rozpinajacego
	for i in range(len(matrix)):
		for j in range(i, len(matrix)):
			if matrix[i][j] != 0:
				edges.append([i, j, matrix[i][j]])
				nodes[i] = color # kolor startowy
				nodes[j] = color

	edges.sort(key=lambda x: x[2]) # sortujemy krawedzie po wagach
	print("ilosć wierzchołków: ", node)
	print("macierz: ", matrix)
	print("kolory: ", nodes)
	print("kraw: ", edges)

	#wybieramy pierwszą krawędź
	color += 1
	nodes[edges[0][0]] = color
	nodes[edges[0][1]] = color
	matrixSpanningTree[edges[0][0]][edges[0][1]] = edges[0][2]
	matrixSpanningTree[edges[0][1]][edges[0][0]] = edges[0][2]
	edges.remove(edges[0])

	for edg in edges:
		#jeśli wierzchołek nie ma jeszcze koloru - (0)
		print(edges)
		if getNumberOfEdgesFromMatrix(matrixSpanningTree) == node :# should be node - 1 but check matrixSpanningTree size
			break
		if nodes[edg[0]] == 0 and nodes[edg[1]] == 0:
			color += 1
			nodes[edg[0]] = color
			nodes[edg[1]] = color
			matrixSpanningTree[edg[0]][edg[1]] = edg[2]
			matrixSpanningTree[edg[1]][edg[0]] = edg[2]
		#w innym razie, jeżeli wierzchołki mają różne kolory
		elif nodes[edg[0]] != nodes[edg[1]]:
			# dodajemy krawędź do drzewa rozpinającego
			matrixSpanningTree[edg[0]][edg[1]] = edg[2]
			matrixSpanningTree[edg[1]][edg[0]] = edg[2]
			#wybieramy kolor który nie jest 0
			new_color = 0
			if nodes[edg[0]] == 0:
				new_color = nodes[edg[0]] = nodes[edg[1]]
			elif nodes[edg[1]] == 0:
				new_color = nodes[edg[1]] = nodes[edg[0]]

			#zmieniamy kolory wierzchołków w drzewie
			for node in nodes:
				if nodes[node] == nodes[edg[1]]:
					nodes[node] = new_color
		# w przeciwnym wypadku - odrzucamy krawędź usuwam ją z listy
		else:
			edges.remove(edg)
			
	print(matrixSpanningTree)
	# return grapgSpanningTree
	
if __name__ == '__main__':
	graph = gl.MyGraph([])
	graph.showWeightedGraph('test.png')
	kruskal_algorithm(graph)