#chapter 3
# 25
import networkx as nx

# Number of nodes and edges in the real-world graph
num_nodes = 18772
num_edges = 198110

# Generate the Erdős-Rényi random graph
G_er = nx.gnm_random_graph(num_nodes, num_edges)

# Print the number of nodes and edges in the generated graph
print("Number of nodes:", G_er.number_of_nodes())
print("Number of edges:", G_er.number_of_edges())

# 26
import networkx as nx
import urllib.request
import matplotlib.pyplot as plt

# Download the Astro Physics collaboration network dataset
url = "http://snap.stanford.edu/data/ca-AstroPh.txt.gz"
filename = "ca-AstroPh.txt.gz"
urllib.request.urlretrieve(url, filename)

# Load the real-world graph
G_real = nx.read_edgelist(filename)

# Generate the Configuration Model random graph
degrees = [d for (n, d) in G_real.degree()]
G_config = nx.configuration_model(degrees)

# Remove parallel edges and self-loops
G_config = nx.Graph(G_config)

# Print the number of nodes and edges in the real-world graph
print("Real-world graph:")
print("Number of nodes:", G_real.number_of_nodes())
print("Number of edges:", G_real.number_of_edges())

# Print the number of nodes and edges in the Configuration Model random graph
print("\nConfiguration Model random graph:")
print("Number of nodes:", G_config.number_of_nodes())
print("Number of edges:", G_config.number_of_edges())

# Draw the real-world graph
plt.figure(figsize=(8, 6))
nx.draw(G_real, node_size=20)
plt.title("Real-world graph")
plt.show()

# Draw the Configuration Model random graph
plt.figure(figsize=(8, 6))
nx.draw(G_config, node_size=20)
plt.title("Configuration Model random graph")
plt.show()

#27
import networkx as nx
import matplotlib.pyplot as plt

# Load the graph from the file
G = nx.read_edgelist('ca-AstroPh.txt', comments='#', delimiter='\t')

# Compute the degree distribution of the real-world graph
degree_seq = [d for n, d in G.degree()]
hist = nx.degree_histogram(G)
# Plot the degree distribution of the real-world graph
plt.bar(range(len(hist)), hist)
plt.title("Degree distribution of Astro Physics collaboration network")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

# Define the number of nodes and probability for the Erdős-Rényi random graph
num_nodes = 1000
p = 0.01

# Generate the Erdős-Rényi random graph
er_graph = nx.erdos_renyi_graph(num_nodes, p)

# Compute the degree distribution of the Erdős-Rényi random graph
degree_seq = [d for n, d in er_graph.degree()]
hist = nx.degree_histogram(er_graph)

# Plot the degree distribution of the Erdős-Rényi random graph
plt.bar(range(len(hist)), hist)
plt.title("Degree distribution of Erdős-Rényi random graph")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

# Generate an empty graph with the same degree sequence as the real-world graph
CG = nx.configuration_model(G.degree())

# Remove self-loops and parallel edges from the graph
CG = nx.Graph(CG)

# Compute the degree distribution of the Configuration model random graph
degree_seq = [d for n, d in CG.degree()]
hist = nx.degree_histogram(CG)

# Plot the degree distribution of the Configuration model random graph
plt.bar(range(len(hist)), hist)
plt.title("Degree distribution of Configuration model random graph")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

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

#29
import networkx as nx
import matplotlib.pyplot as plt

# Load the real-world graph
G_real = nx.read_edgelist('ca-AstroPh.txt')

# Generate Erdős-Rényi random graph
n = 18772  # Number of nodes
m = 198110  # Number of edges
G_erdos = nx.gnm_random_graph(n, m)

# Generate Configuration model random graph
degree_seq = [G_real.degree(node) for node in G_real.nodes()]
G_config = nx.configuration_model(degree_seq)

# Compute degree distributions
degree_dist_real = nx.degree_histogram(G_real)
degree_dist_erdos = nx.degree_histogram(G_erdos)
degree_dist_config = nx.degree_histogram(G_config)

# Compute shortest path length distributions
shortest_path_lengths_real = nx.shortest_path_length(G_real)
path_lengths_real = [length for lengths in shortest_path_lengths_real.values() for length in lengths.values()]
shortest_path_lengths_erdos = nx.shortest_path_length(G_erdos)
path_lengths_erdos = [length for lengths in shortest_path_lengths_erdos.values() for length in lengths.values()]
shortest_path_lengths_config = nx.shortest_path_length(G_config)
path_lengths_config = [length for lengths in shortest_path_lengths_config.values() for length in lengths.values()]

# Compute clustering coefficient distributions
clustering_coeffs_real = nx.clustering(G_real)
clustering_coeffs_values_real = list(clustering_coeffs_real.values())
clustering_coeffs_erdos = nx.clustering(G_erdos)
clustering_coeffs_values_erdos = list(clustering_coeffs_erdos.values())
clustering_coeffs_config = nx.clustering(G_config)
clustering_coeffs_values_config = list(clustering_coeffs_config.values())

# Plot degree distributions
plt.plot(degree_dist_real, 'bo-', label='Real World Graph')
plt.plot(degree_dist_erdos, 'ro-', label='Erdos-Renyi Graph')
plt.plot(degree_dist_config, 'go-', label='Configuration Model Graph')
plt.xlabel('Degree')
plt.ylabel('Count')
plt.title

#29
import networkx as nx
import matplotlib.pyplot as plt

# Load the real-world graph
G_real = nx.read_edgelist('ca-AstroPh.txt')

# Generate Erdős-Rényi random graph
n = 18772  # Number of nodes
m = 198110  # Number of edges
G_erdos = nx.gnm_random_graph(n, m)

# Generate Configuration model random graph
degree_seq = [G_real.degree(node) for node in G_real.nodes()]
G_config = nx.configuration_model(degree_seq)

# Compute degree distributions
degree_dist_real = nx.degree_histogram(G_real)
degree_dist_erdos = nx.degree_histogram(G_erdos)
degree_dist_config = nx.degree_histogram(G_config)

# Compute shortest path length distributions
shortest_path_lengths_real = nx.shortest_path_length(G_real)
path_lengths_real = [length for lengths in shortest_path_lengths_real.values() for length in lengths.values()]
shortest_path_lengths_erdos = nx.shortest_path_length(G_erdos)
path_lengths_erdos = [length for lengths in shortest_path_lengths_erdos.values() for length in lengths.values()]
shortest_path_lengths_config = nx.shortest_path_length(G_config)
path_lengths_config = [length for lengths in shortest_path_lengths_config.values() for length in lengths.values()]

# Compute clustering coefficient distributions
clustering_coeffs_real = nx.clustering(G_real)
clustering_coeffs_values_real = list(clustering_coeffs_real.values())
clustering_coeffs_erdos = nx.clustering(G_erdos)
clustering_coeffs_values_erdos = list(clustering_coeffs_erdos.values())
clustering_coeffs_config = nx.clustering(G_config)
clustering_coeffs_values_config = list(clustering_coeffs_config.values())

# Plot degree distributions
plt.plot(degree_dist_real, 'bo-', label='Real World Graph')
plt.plot(degree_dist_erdos, 'ro-', label='Erdos-Renyi Graph')
plt.plot(degree_dist_config, 'go-', label='Configuration Model Graph')
plt.xlabel('Degree')
plt.ylabel('Count')
plt.title

#30
import networkx as nx
import matplotlib.pyplot as plt

# Load the real-world graph
G_real = nx.read_edgelist('ca-AstroPh.txt')

# Generate Erdős-Rényi random graph
n = 18772  # Number of nodes
m = 198110  # Number of edges
G_erdos = nx.gnm_random_graph(n, m)

# Generate Configuration model random graph
degree_seq = [G_real.degree(node) for node in G_real.nodes()]
G_config = nx.configuration_model(degree_seq)

# Compute WCC size distributions
wcc_real = nx.weakly_connected_components(G_real)
wcc_sizes_real = [len(wcc) for wcc in wcc_real]
wcc_erdos = nx.weakly_connected_components(G_erdos)
wcc_sizes_erdos = [len(wcc) for wcc in wcc_erdos]
wcc_config = nx.weakly_connected_components(G_config)
wcc_sizes_config = [len(wcc) for wcc in wcc_config]

# Plot WCC size distributions
plt.hist(wcc_sizes_real, bins=range(1, max(wcc_sizes_real) + 2), align='left', rwidth=0.8, label='Real World Graph')
plt.xlabel('WCC Size')
plt.ylabel('Count')
plt.title('WCC Size Distribution - Real World Graph')
plt.legend()
plt.show()

plt.hist(wcc_sizes_erdos, bins=range(1, max(wcc_sizes_erdos) + 2), align='left', rwidth=0.8, label='Erdos-Renyi Graph')
plt.xlabel('WCC Size')
plt.ylabel('Count')
plt.title('WCC Size Distribution - Erdos-Renyi Graph')
plt.legend()
plt.show()

plt.hist(wcc_sizes_config, bins=range(1, max(wcc_sizes_config) + 2), align='left', rwidth=0.8, label='Configuration Model Graph')
plt.xlabel('WCC Size')
plt.ylabel('Count')
plt.title('WCC Size Distribution - Configuration Model Graph')
plt.legend()
plt.show()

#31
import networkx as nx
import numpy as np

# Load the real-world graph
G_real = nx.read_edgelist ('ca-AstroPh.txt')

# Generate Erdős-Rényi random graph
n = 18772  # Number of nodes
m = 198110  # Number of edges
G_erdos = nx.gnm_random_graph (n, m)

# Generate Configuration model random graph
degree_seq = [G_real.degree (node) for node in G_real.nodes ()]
G_config = nx.configuration_model (degree_seq)

# Calculate degree distributions
degree_dist_real = nx.degree_histogram (G_real)
degree_dist_erdos = nx.degree_histogram (G_erdos)
degree_dist_config = nx.degree_histogram (G_config)

# Calculate shortest path length distributions
shortest_paths_real = nx.shortest_path_length (G_real)
path_lengths_real = [length for lengths in shortest_paths_real.values () for length in lengths.values ()]
shortest_paths_erdos = nx.shortest_path_length (G_erdos)
path_lengths_erdos = [length for lengths in shortest_paths_erdos.values () for length in lengths.values ()]
shortest_paths_config = nx.shortest_path_length (G_config)
path_lengths_config = [length for lengths in shortest_paths_config.values () for length in lengths.values ()]

# Calculate clustering coefficient distributions
clustering_coeffs_real = nx.clustering (G_real)
clustering_coeffs_erdos = nx.clustering (G_erdos)
clustering_coeffs_config = nx.clustering (G_config)

# Calculate WCC size distributions
wcc_real = nx.weakly_connected_components (G_real)
wcc_sizes_real = [len (wcc) for wcc in wcc_real]
wcc_erdos = nx.weakly_connected_components (G_erdos)
wcc_sizes_erdos = [len (wcc) for wcc in wcc_erdos]
wcc_config = nx.weakly_connected_components (G_config)
wcc_sizes_config = [len (wcc) for wcc in wcc_config]

# Write results to a file
with open ('graph_properties.txt', 'w') as f:
    f.write ('Degree Distribution\n')
    f.write (f'Real World Graph: {np.array (degree_dist_real)}\n')
    f.write (f'Erdos-Renyi Graph: {np.array (degree_dist_erdos)}\n')
    f.write (f'Configuration Model Graph: {np.array (degree_dist_config)}\n\n')

    f.write ('Shortest Path Length Distribution\n')
    f.write (f'Real World Graph: {np.array (path_lengths_real)}\n')
    f.write (f'Erdos-Renyi Graph: {np.array (path_lengths_erdos)}\n')
    f.write (f'Configuration Model Graph: {np.array (path_lengths_config)}\n\n')

    f.write ('Clustering Coefficient Distribution\n')

# 32
import urllib.request
import gzip
import networkx as nx
import matplotlib.pyplot as plt

# URL of the dataset
url = "https://snap.stanford.edu/data/ca-GrQc.txt.gz"
file_name = "ca-GrQc.txt.gz"

# Download the dataset
urllib.request.urlretrieve(url, file_name)

# Extract the gzipped file
with gzip.open(file_name, 'rb') as gz_file:
    with open("ca-GrQc.txt", 'wb') as output_file:
        output_file.write(gz_file.read())

# Load the real-world graph
G_real = nx.read_edgelist("ca-GrQc.txt")

# Generate a small-world graph
G_small_world = nx.watts_strogatz_graph(len(G_real.nodes()), len(G_real.edges()), 0.1)

# Calculate the degree distributions
degree_dist_real = nx.degree_histogram(G_real)
degree_dist_small_world = nx.degree_histogram(G_small_world)

# Plot the degree distributions
plt.figure(figsize=(10, 5))
plt.plot(degree_dist_real, label="Real World Graph")
plt.plot(degree_dist_small_world, label="Small World Graph")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.title("Degree Distribution")
plt.legend()
plt.show()
