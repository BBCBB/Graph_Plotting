
import networkx as nx
import matplotlib.pyplot as plt
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])       # nodes [x , y]

f = open(r"C:\\Users\data_file","r")   # reading the coordinates of the nodes from a text file
input_data = ''.join(f.readlines())
lines = input_data.split('\n')

nodeCount = int(lines[0])

points = []
for i in range(1, nodeCount+1):
    line = lines[i]
    parts = line.split()
    points.append(Point(float(parts[0]), float(parts[1])))


G=nx.DiGraph()                 #defining a directed graph (empty)... Eliminate "Di" to create a simple graph
G.add_edges_from([(0,1),(1,2),(1,3),(0,3),(1,4),(3,2)])         # adding edges
nodes=range(nodeCount)

G.add_nodes_from(nodes)                                          # add nodes
pos = {}                  # assigning the coordinates of the nodes to each one
for i in range(len(nodes)):
    pos[i]=[]
for i in range(len(nodes)):
    pos[i].append(points[i][0])
    pos[i].append(points[i][1])


fig, ax = plt.subplots()
nx.draw_networkx_nodes(G,pos,node_size=55,node_color='yellow')
nx.draw_networkx_edges(G,pos, width=0.4,edge_color='black')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
nx.draw_networkx_labels(G,pos,font_size=8)
plt.savefig('result.png', dpi=300)                 # saving the resulting graph


