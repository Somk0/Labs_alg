import csv
import networkx as nx
import matplotlib.pyplot as plt

def minimal_cable_length(a):
    with a as file:
        reader = csv.reader(file)
        matrix = [list(map(int, row)) for row in reader]
    
    n = len(matrix)
    edges = []
    
    for i in range(n):
        for j in range(i + 1, n):  
            if matrix[i][j] > 0:
                edges.append((i, j, matrix[i][j]))
    
   
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    
    uf = UnionFind(n)
    mst_edges = []
    total_length = 0
    
    for u, v, weight in edges_sorted:
        if uf.union(u, v):
            mst_edges.append((u, v))
            total_length += weight
            if len(mst_edges) == n - 1:
                break
    
    
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_weighted_edges_from(edges)
    
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    
    nx.draw_networkx_edges(G, pos, width=1, edge_color='gray', alpha=0.5)
    
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=3, edge_color='red')
    
    
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    
    plt.axis('off')
    plt.show()
    
    return total_length

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False


a1 = open(r'islands.csv')
print("Мінімальна довжина кабелю:", minimal_cable_length(a1))