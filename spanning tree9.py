class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def kruskal(edges, n):
    edges.sort(key=lambda edge: edge.weight)  # Sort edges by weight
    parent = list(range(n))  # Parent array for Union-Find

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    mst = []
    for edge in edges:
        root_u, root_v = find(edge.u), find(edge.v)
        if root_u != root_v:  # If not in the same set, add to MST
            mst.append(edge)
            parent[root_u] = root_v  # Union the sets

    return mst

# Input: number of vertices and edges
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []
for _ in range(m):
    u, v, weight = map(int, input("Enter edge (u, v, weight): ").split())
    edges.append(Edge(u, v, weight))

mst = kruskal(edges, n)

# Output the MST edges
print(f"\nNumber of vertices: {n}")
print(f"Number of edges in the MST: {len(mst)}")
for edge in mst:
    print(f"Edge ({edge.u}, {edge.v}) with weight {edge.weight}")
