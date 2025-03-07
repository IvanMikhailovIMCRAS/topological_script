import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Optional, Tuple
from bonds_parser import bonds_parser
from types_parser import types_parser


def mol_draw(bonds: List[Tuple[int, int]], types: List[str]) -> None:
    G: nx.classes.graph.Graph = nx.Graph()
    # G.add_nodes_from(types)
    G.add_edges_from(bonds)

    colors = ["yellow" if t == "B" else "red" for t in types]
    # print(colors)
    print(type(G))
    pos = nx.kamada_kawai_layout(G)  # схема размещения узлов
    options = {
        "node_color": colors,  # color of node
        "node_size": 100,  # size of node
        "edge_color": "black",
        "width": 1,  # line width of edges
        "edge_color": "blue",  # edge color
        "font_size": 10,
    }

    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=False, arrows=False, **options)
    ax = plt.gca()
    ax.collections[0].set_edgecolor("#000000")  # рисуем черную обводку у каждого узла
    print(G)  # так можно посмотреть число вершин и рёбер
    plt.savefig("graph.png")


if __name__ == "__main__":
    S = "(B)2"  # definition of side chain
    script = (
        "(A)1{1}[" + S + "]((A)1[" + S + "])198(A)1{1}" + S
    )  # main chain + side chain
    # script = "(Na)1(C0)1[(O)1]((C)1([(H)1])2)3(O)1(H)1"
    bonds = bonds_parser(script)
    types = types_parser(script)
    print(len(bonds) - 1)
    print(len(types))
    mol_draw(bonds, types)
