
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
