# 25
import networkx as nx

'تعداد گره ها و یال ها در دنیای واقعی'
num_nodes = 18772
num_edges = 198110

'Generate the Erdős-Rényi random graph'
G_er = nx.gnm_random_graph(num_nodes, num_edges)

'چاپ تعداد یال ها و گره ها'
print("Number of nodes:", G_er.number_of_nodes())
print("Number of edges:", G_er.number_of_edges())
