import matplotlib.pyplot as plt
import networkx as nx
import random
class MyGraph:
    def __init__(self, directed=False):
        self.graph = nx.DiGraph() if directed else nx.Graph()
    def add_edge(self, u, v, weight, directed=False):
        if not self.graph.has_edge(u, v):
            self.graph.add_edge(u, v, weight=weight)
    def generate_random_directed_edges(self, n, p):
        for u in range(n):
            for v in range(n):
                if u != v and random.random() < p:
                    yield u, v
    def generate_random_weighted_graph(self, n, p, directed=False, weight_range=(1, 10)):
        while True:
            self.graph = nx.DiGraph() if directed else nx.Graph()
            all_possible_edges = [(u, v) for u in range(n) for v in range(n) if u != v]
            num_edges = int(p * len(all_possible_edges))
            random_edges = random.sample(all_possible_edges, num_edges)
            for u, v in random_edges:
                weight = random.randint(*weight_range)
                self.add_edge(u, v, weight, directed=directed)
                if directed and random.random() < p:
                    weight = random.randint(*weight_range)
                    self.add_edge(v, u, weight, directed=directed)
            if (nx.is_strongly_connected(self.graph) if directed else nx.is_connected(self.graph)):
                break
    def get_graph_center(self):
        dist_sum = [sum(nx.shortest_path_length(self.graph, source=n, weight='weight').values()) for n in self.graph.nodes()]
        return dist_sum.index(min(dist_sum))
    def get_minimax_center(self):
        dist_max = [max(nx.shortest_path_length(self.graph, source=n, weight='weight').values()) for n in self.graph.nodes()]
        return dist_max.index(min(dist_max))
    def print_graph(self):
        pos = nx.spring_layout(self.graph)
        labels = {n: str(n) for n in self.graph.nodes()}
        nx.draw(self.graph, pos, labels=labels, with_labels=True)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()
    def johnson(self):
        self.graph.add_node('s')
        for node in self.graph.nodes():
            if node != 's':
                self.graph.add_edge('s', node, weight=0)
        try:
            _, h = nx.bellman_ford_predecessor_and_distance(self.graph, source='s', weight='weight')
        except nx.NetworkXUnbounded:
            print("Graph contains a negative weight cycle")
            return None
        for u, v, data in self.graph.edges(data=True):
            data['weight'] = data['weight'] + h[u] - h[v]
        D = {}
        for u in self.graph.nodes():
            if u != 's':
                D[u] = nx.single_source_dijkstra_path_length(self.graph, source=u, weight='weight')
        for u in D:
            for v in D[u]:
                D[u][v] = D[u][v] - h[u] + h[v]
        self.graph.remove_node('s')
        return D

def main():
    directed = False # Change to True to generate a directed graph and test Johnson's algorithm or False to generate an undirected graph and test graph center and minimax center
    G = MyGraph()
    G.generate_random_weighted_graph(4, 0.5, directed=directed)
    if directed:
        print("Directed graph")
        print("Johnson's algorithm result:")
        johnson_result = G.johnson()
        print("Node:\t",end="")
        print(sorted(johnson_result.keys()))
        for key in sorted(johnson_result.keys()):
            print(key, ":\t\t", [dist for node, dist in sorted(johnson_result[key].items())],sep="")
    else:
        print("Undirected graph")
        print("Graph center is:")
        print(G.get_graph_center())
        print("Minimax center is:")
        print(G.get_minimax_center())
    G.print_graph()

if __name__ == '__main__':
    main()