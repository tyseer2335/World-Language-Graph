"""CSC111 Final Project 2023:
This is a test file for visulizing graphs
"""
from pyvis.network import Network

net = Network()

unique_id = 0
genus_num = 1
major_lang_num = 3
creole_num = 5

for i in range(1, genus_num + 1):
    print("Generating Genus #" + str(i))
    net.add_node(unique_id,
                 title="Genus " + str(i),
                 color="#62CDFF",
                 size=60,
                 label="Genus " + str(i),
                 labelHighlightBold=True)
    unique_id += 1


for i in range(1, major_lang_num + 1):
    print("Generating Major Language #" + str(i))
    net.add_node(unique_id,
                 title="Major Language " + str(i),
                 color="#95BDFF",
                 size=30,
                 label="Major Language " + str(i),
                 labelHighlightBold=True)
    unique_id += 1


for i in range(1, creole_num + 1):
    print("Generating Creole #" + str(i))
    net.add_node(unique_id,
                 title="Creole " + str(i),
                 color="#C9EEFF",
                 size=15,
                 label="Creole " + str(i),
                 labelHighlightBold=True)
    unique_id += 1

# Add some Rnadom Edges
edge_color = "#2F58CD"
net.add_edge(0, 1, color=edge_color)
net.add_edge(0, 2, color=edge_color)
net.add_edge(0, 3, color=edge_color)
net.add_edge(1, 4, color=edge_color)
net.add_edge(1, 5, color=edge_color)
net.add_edge(2, 6, color=edge_color)
net.add_edge(2, 7, color=edge_color)
net.add_edge(3, 8, color=edge_color)

net.show('test_network.html')
