import networkx as n
import matplotlib.pyplot as plt

# Tạo một đối tượng đồ thị vô hướng mới
graph = n.Graph()

# Thêm các cạnh vào đồ thị
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 1)
graph.add_edge(4, 1)
graph.add_edge(2, 4)

#Đếm số đỉnh
print("Số đỉnh:", graph.number_of_nodes())

#Đếm số cạnh
print("Số cạnh:", graph.number_of_edges())

# In ra danh sách các đỉnh trong đồ thị
print("Danh sách các đỉnh trong đồ thị:")
print(graph.nodes())

# In ra danh sách các cạnh trong đồ thị
print("Danh sách các cạnh trong đồ thị:")
print(graph.edges())

print("Các bậc của các đỉnh:")
print("Đỉnh 1 có bậc:", graph.degree(1))
print("Đỉnh 2 có bậc:", graph.degree(2))
print("Đỉnh 3 có bậc:", graph.degree(3))
print("Đỉnh 4 có bậc:", graph.degree(4))