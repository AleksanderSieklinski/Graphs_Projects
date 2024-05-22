import networkx as nx
import matplotlib.pyplot as plt
import random


# function that creates flow network, with N clusters, each cluster has random number of nodes from 2 to N
# returns: flow network, matrix of capacities, source, sink, list of nodes in each cluster
# sink and source are first and last node in the list of nodes
def createFlowNetwork(N, displayBasicFlowNetwork=False):
    if N < 2 or N > 5:
        raise ValueError("N must be greater than 1 and less than 5.")
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
        # random.shuffle(nodes[i])

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

    j = 0
    if displayBasicFlowNetwork:
        displayFlowNetwork(G, nodes, 'lab5_zad1_podst_siatka.png')
    # adding additional random edges (2nd step)
    while j < edges_to_add:
        #choose random cluster
        # choosenCluster1 = random.randrange(1,N + 1)
        choosenCluster1 = random.randrange(0, N + 1)
        choosenCluster2 = random.randrange(1, N + 2)

        #choose random nodes from choosen clusters
        choosenNodeFrom = random.randrange(0,len(nodes[choosenCluster1]))
        choosenNodeTo = random.randrange(0,len(nodes[choosenCluster2]))
        if choosenCluster1 == choosenCluster2:
            if choosenNodeFrom == choosenNodeTo:
                continue
        
        if not G.has_edge(nodes[choosenCluster1][choosenNodeFrom], nodes[choosenCluster2][choosenNodeTo]) and not G.has_edge(nodes[choosenCluster2][choosenNodeTo], nodes[choosenCluster1][choosenNodeFrom]):
            G.add_edge(nodes[choosenCluster1][choosenNodeFrom], nodes[choosenCluster2][choosenNodeTo], capacity=random.randrange(1,11))
            j += 1
            print("Added edge between: ", nodes[choosenCluster1][choosenNodeFrom], nodes[choosenCluster2][choosenNodeTo])

    # create matrix of capacities (needed for 2nd task)
    matrix = nx.adjacency_matrix(G).todense()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i,j] != 0:
                matrix[i,j] = G[i][j]['capacity']


    return G, matrix, nodes[0], nodes[-1], nodes

def displayFlowNetwork(G, clustersList, name):
    positions = {}
    maxClusterSize = max([len(i) for i in clustersList])
    for i in range(len(clustersList)):
        for j in range(len(clustersList[i])):
            if i % 2 == 0:
                positions[clustersList[i][j]] = (i*2,j*(-2))
            else:
                positions[clustersList[i][j]] = (i*2,j*(-2)+maxClusterSize/3)
    positions[clustersList[0][0]] = (0,-maxClusterSize/2)
    positions[clustersList[-1][-1]] = (len(clustersList)*2,-maxClusterSize/2)

    figsize = (len(clustersList) * 2, len(clustersList)*2)
    plt.figure(figsize=figsize)
    nx.draw_networkx(G, positions)
    labels = nx.get_edge_attributes(G, "capacity")
    nx.draw_networkx_edge_labels(G, positions, labels, label_pos=0.6)
    plt.savefig(name)
    
if __name__ == '__main__':
    N = 2
    G, cappacity_matrix, source, sink, listOfClusters  = createFlowNetwork(N, True)
    print("Source: ", source)
    print("Sink: ", sink)
    print("Matrix: \n", cappacity_matrix)

    displayFlowNetwork(G, listOfClusters, 'lab5_zad1.png')