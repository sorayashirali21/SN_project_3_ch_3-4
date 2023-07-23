
#28

import networkx as nx
import matplotlib.pyplot as plt

# Load the graph from the file
G = nx.read_edgelist('ca-AstroPh.txt', comments='#', delimiter='\t')

# Compute the shortest path length distribution of the real-world graph
spl = dict(nx.shortest_path_length(G))
dist = [len([1 for k,v in spl.items() if k!=n and v.get(n) == d]) for n in G.nodes() for d in range(max(spl[n].values())+1)]

# Plot the shortest path length distribution of the real-world graph
plt.bar(range(len(dist)), dist)
plt.title("Shortest path length distribution of Astro Physics collaboration network")
plt.xlabel("Shortest path length")
plt.ylabel("Frequency")
plt.show()

# Define the number of nodes and probability for the Erdős-Rényi random graph
num_nodes = 1000
p = 0.01

# Generate the Erdős-Rényi random graph
er_graph = nx.erdos_renyi_graph(num_nodes, p)

# Compute the shortest path length distribution of the Erdős-Rényi random graph
spl = dict(nx.shortest_path_length(er_graph))
dist = [len([1 for k,v in spl.items() if k!=n and v.get(n) == d]) for n in er_graph.nodes() for d in range(max(spl[n].values())+1)]

# Plot the shortest path length distribution of the Erdős-Rényi random graph
plt.bar(range(len(dist)), dist)
plt.title("Shortest path length distribution of Erdős-Rényi random graph")
plt.xlabel("Shortest path length")
plt.ylabel("Frequency")
plt.show()

# Generate an empty graph with the same degree sequence as the real-world graph
CG = nx.configuration_model(G.degree())

# Remove self-loops and parallel edges from the graph
CG = nx.Graph(CG)

# Compute the shortest path length distribution of the Configuration model random graph
spl = dict(nx.shortest_path_length(CG))
dist = [len([1 for k,v in spl.items() if k!=n and v.get(n) == d]) for n in CG.nodes() for d in range(max(spl[n].values())+1)]

# Plot the shortest path length distribution of the Configuration model random graph
plt.bar(range(len(dist)), dist)
plt.title("Shortest path length distribution of Configuration model random graph")
plt.xlabel("Shortest path length")
plt.ylabel("Frequency")
plt.show()
