#chapter 4
#33
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

#34

import networkx as nx
import matplotlib.pyplot as plt

# Load the real-world graph
G_real = nx.read_edgelist("ca-GrQc.txt")

# Compute the shortest path lengths
shortest_path_lengths = nx.shortest_path_length(G_real)

# Count the occurrences of each path length
path_length_counts = {}
for source, paths in shortest_path_lengths:
    for target, length in paths.items():
        if length not in path_length_counts:
            path_length_counts[length] = 0
        path_length_counts[length] += 1

# Convert the counts to a distribution
total_paths = len(G_real.nodes()) * (len(G_real.nodes()) - 1)
path_length_dist = [path_length_counts[length] / total_paths for length in range(1, max(path_length_counts.keys()) + 1)]

# Plot the shortest path length distribution
plt.figure(figsize=(10, 5))
plt.plot(range(1, max(path_length_counts.keys()) + 1), path_length_dist)
plt.xlabel("Shortest Path Length")
plt.ylabel("Distribution")
plt.title("Shortest Path Length Distribution")
plt.show()

#35
import networkx as nx
import matplotlib.pyplot as plt

# Load the real-world graph
G_real = nx.read_edgelist("ca-GrQc.txt")

# Compute the shortest path lengths
shortest_path_lengths = nx.shortest_path_length(G_real)

# Count the occurrences of each path length
path_length_counts = {}
for source, paths in shortest_path_lengths:
    for target, length in paths.items():
        if length not in path_length_counts:
            path_length_counts[length] = 0
        path_length_counts[length] += 1

# Convert the counts to a distribution
total_paths = len(G_real.nodes()) * (len(G_real.nodes()) - 1)
path_length_dist = [path_length_counts[length] / total_paths for length in range(1, max(path_length_counts.keys()) + 1)]

# Plot the shortest path length distribution
plt.figure(figsize=(10, 5))
plt.plot(range(1, max(path_length_counts.keys()) + 1), path_length_dist)
plt.xlabel("Shortest Path Length")
plt.ylabel("Distribution")
plt.title("Shortest Path Length Distribution")
plt.show()

#36
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

