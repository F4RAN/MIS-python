import networkx as nx
import numpy as np
# Create random undirected DAG edge list
def create_random_graph():
    alpha = 0.5  # alpha = p (float) – Probability for edge creation.
    G = nx.gnp_random_graph(40, p=alpha)
    DAG = nx.DiGraph([(u, v) for (u, v) in G.edges() if u < v])
    R = DAG.to_undirected()
    # U = nx.to_edgelist(R)

    return mis(R)

def mis(G):
    out = []
    print(list(G.nodes))
    while(len(list(G.nodes)) != 0):
        #Find a vertex of minimum degree v∈V
        degrees = [val for (node, val) in G.degree()]
        np_deg = np.array(degrees)
        min_index = np.where(np_deg == np_deg.min())[0][0]
        node_name = list(G.nodes)[min_index]
        #Find node neighbours
        neighbours = [val for val in G.neighbors(node_name)]
        # Add it to S , Remove it and its neighbours from  V
        G.remove_node(node_name)
        childs = []
        #print(G.nodes, node_name, min_index)
        for n in neighbours:
            childs.append(n)
            G.remove_node(n)

        out.append({'name': node_name, 'childs': childs})
        #print(G.nodes, childs)

    return out
