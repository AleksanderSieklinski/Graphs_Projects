import networkx as nx
import matplotlib.pyplot as plt
import random

# random.seed(42)

def createFlowNetwork(N):
    sizesOfClusters = [1] # source 

    for _ in range(N):
        sizesOfClusters.append(random.randrange(2,N+1)) #  from 2 to N in each cluster

    sizesOfClusters.append(1) # sink
    
    nodes = [] # list of nodes in each cluster
    nodeIter = 0
    for i in range(len(sizesOfClusters)):
        nodes.append([])
        for _ in range(sizesOfClusters[i]):
            nodes[i].append(nodeIter)
            nodeIter += 1

    G = nx.DiGraph()
    for i in range(len(nodes)):
        for j in nodes[i]:
            G.add_node(j, layer=i)


    for i in range(len(nodes)-1):
        currentClusterSize = len(nodes[i])
        nextClusterSize = len(nodes[i+1])

        j, k = 0, 0 # j - current cluster, k - next cluster

        # creating basic edges between clusters (1st step)
        while True:
            if currentClusterSize <= nextClusterSize:
                G.add_edge(nodes[i][j], nodes[i+1][k], capacity=random.randrange(1,11))
                k += 1
                if j != currentClusterSize-1:
                    j += 1
                if k == nextClusterSize:
                    break
            else:
                G.add_edge(nodes[i][j], nodes[i+1][k], capacity=random.randrange(1,11))
                j += 1
                if k != nextClusterSize-1:
                    k += 1
                if j == currentClusterSize:
                    break  

        edges_to_add = 2*N


    # adding additional random edges (2nd step)
    j = 0
    graph_visualization(G, nodes, 'lab5_zad1_podst_siatka.png')
    while j < edges_to_add:
        #choose random cluster
        choosenCluster1 = random.randrange(1,N + 1)
        choosenCluster2 = None
        while True:
            choosenCluster2 =  choosenCluster1 + random.choice([-1, 0, 1])
            if choosenCluster2 > 0 and choosenCluster2 < N+1:
                break

        #choose random nodes from choosen clusters
        choosenNodeFrom = random.randrange(0,len(nodes[choosenCluster1]))
        choosenNodeTo = random.randrange(0,len(nodes[choosenCluster2]))
        if choosenCluster1 == choosenCluster2:
            if choosenNodeFrom == choosenNodeTo:
                continue
        
        if not G.has_edge(nodes[choosenCluster1][choosenNodeFrom], nodes[choosenCluster2][choosenNodeTo]) and not G.has_edge(nodes[choosenCluster2][choosenNodeTo], nodes[choosenCluster1][choosenNodeFrom]):
            G.add_edge(nodes[choosenCluster1][choosenNodeFrom], nodes[choosenCluster2][choosenNodeTo], capacity=random.randrange(1,11))
            j += 1

    # create matrix of capacities
    matrix = nx.adjacency_matrix(G).todense()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i,j] != 0:
                matrix[i,j] = G[i][j]['capacity']


    return G, matrix, nodes[0], nodes[-1], nodes

def graph_visualization(G, nodes, name):
    positions = {}
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            positions[nodes[i][j]] = (i*2,j*(-2))
    nx.draw_networkx(G, positions)
    labels = nx.get_edge_attributes(G, "capacity")
    nx.draw_networkx_edge_labels(G, positions, labels, label_pos=0.6)
    plt.savefig(name)
    
if __name__ == '__main__':
    N = 3
    G, cappacity_matrix, source, sink, listOfClusters  = createFlowNetwork(N)
    print("Source: ", source)
    print("Sink: ", sink)
    print("Matrix: \n", cappacity_matrix)

    graph_visualization(G, listOfClusters, 'lab5_zad1.png')