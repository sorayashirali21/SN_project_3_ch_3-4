
#37 , 38

import networkx as nx
import matplotlib.pyplot as plt

# Load the real-world graph
G_real = nx.read_edgelist("ca-GrQc.txt")

# Get the weakly connected components
wcc = nx.weakly_connected_components(G_real)

# Compute the size of each weakly connected component
wcc_sizes = [len(component) for component in wcc]

# Count the occurrences of each component size
size_counts = {}
for size in wcc_sizes:
    if size not in size_counts:
        size_counts[size] = 0
    size_counts[size] += 1

# Convert the counts to a distribution
total_components = len(wcc_sizes)
size_dist = [size_counts[size] / total_components for size in sorted(size_counts.keys())]

# Plot the WCC size distribution
plt.figure(figsize=(10, 5))
plt.plot(sorted(size_counts.keys()), size_dist)
plt.xlabel("Component Size")
plt.ylabel("Distribution")
plt.title("WCC Size Distribution")
plt.show()

