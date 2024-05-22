import graph_lib as l1

from itertools import permutations

if __name__ == "__main__":
    G = l1.MyGraph.getRandomGraphNP(6, 0.7)

    
    cycle = l1.MyGraph.find_hamiltonian_cycle(G)

    if cycle:
        print("Znaleziono cykl hamiltonowski:", cycle)
    else:
        print("Graf nie jest hamiltonowski.")
        
    G.showGraph()
   