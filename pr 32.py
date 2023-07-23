
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
