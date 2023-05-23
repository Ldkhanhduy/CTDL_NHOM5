import networkx as n

g = n.DiGraph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(4,2)
g.add_edge(3,1)

print("Số đỉnh:", g.number_of_nodes())

#Đếm số cạnh
print("Số cạnh:", g.number_of_edges())

# In ra danh sách các đỉnh trong đồ thị
print("Danh sách các đỉnh trong đồ thị:")
print(g.nodes())

# In ra danh sách các cạnh trong đồ thị
print("Danh sách các cạnh trong đồ thị:")
print(g.edges())

print("Các bậc của các đỉnh:")
print("Đỉnh 1 có bậc:", g.degree(1))
print("Đỉnh 2 có bậc:", g.degree(2))
print("Đỉnh 3 có bậc:", g.degree(3))
print("Đỉnh 4 có bậc:", g.degree(4))

print("Ma trận kề của đồ thị là:")
matran = n.adjacency_matrix(g)
matran = matran.toarray()
print(matran)