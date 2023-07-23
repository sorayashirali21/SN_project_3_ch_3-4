#27
import networkx as nx
import matplotlib.pyplot as plt

'بارگزاری گراف از فایل مربوطه'
G = nx.read_edgelist('ca-AstroPh.txt', comments='#', delimiter='\t')

'محاسبه ی درجه ی توزیع در دنیای واقعی'
degree_seq = [d for n, d in G.degree()]
hist = nx.degree_histogram(G)

'ترسیم نمودار درجه توزیع'
plt.bar(range(len(hist)), hist)
plt.title("Degree distribution of Astro Physics collaboration network")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

#Define the number of nodes and probability for the Erdős-Rényi random graph
num_nodes = 1000
p = 0.01

#Generate the Erdős-Rényi random graph
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
