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
