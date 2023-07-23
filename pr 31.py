
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
