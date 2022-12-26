import graphviz
from Graph import Graph


if __name__ == '__main__':
    gr = Graph('Test_Graph.txt')
    gr.get_path()
    dot = graphviz.Digraph('Dijkstra shortest path', comment='Dijkstra shortest path')

    for node in gr.nodes.values():
        dot.node(str(node), node.name)
        for to_node, cost in node.edges.items():
            dot.edge(str(node), str(to_node), label=str(cost))
    current_node = gr.nodes[gr.end]
    while current_node.previous != current_node:
        dot.node(str(current_node), current_node.name, color='green')
        dot.edge(str(current_node.previous), str(current_node), label=str(current_node.previous.edges[current_node]), color='green')
        current_node = current_node.previous
    dot.node(str(current_node), current_node.name, color='green')
    print(dot.source)
    dot.render('Dijkstra_shortest_path.gv', view=True)