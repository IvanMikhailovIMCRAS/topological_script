import networkx as nx 
import matplotlib.pyplot as plt
from typing import List, Optional, Tuple
from bonds_parser import bonds_parser
from types_parser import types_parser

def  mol_draw(bonds: List[Tuple[int, int]], types: List[str]) -> None:

    G = nx.Graph()
    G.add_edges_from(bonds)

    colors = ['yellow']
    pos = nx.spring_layout(G) # схема размещения узлов
    options = {
        'node_color': colors,     # color of node
        'node_size': 100,          # size of node
        'width': 1,                 # line width of edges
        'edge_color':'blue',        # edge color
        'font_size' : 10
    }

    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels = True, arrows=False, **options)
    print(G) # так можно посмотреть число вершин и рёбер
    plt.savefig("graph.png")


if __name__ == "__main__":

    S = '(B)2'   #definition of side chain
    script = '(A)1[' + S + ']((A)1[' + S + '])198(A)1' + S #main chain + side chain 
    #script = "(Na)1(C0)1[(O)1]((C)1([(H)1])2)3(O)1(H)1"
    bonds = bonds_parser(script)
    types = types_parser(script)

    mol_draw(bonds, types)