import graphviz
from Graph import Graph


if __name__ == '__main__':
    gr = Graph('Test_Graph.txt')
    gr.get_path()
    dot = graphviz.Digraph('Dijkstra shortest path', comment='Dijkstra shortest path')

    for node in gr.nodes.values():
        if node.is_on_path:
            dot.node(str(node), node.name, color='green')
        else:
            dot.node(str(node), node.name)
    for edge in gr.edges.values():
        if edge.is_on_path:
            dot.edge(str(edge.from_node), str(edge.to_node), label=str(edge.weight), color='green')
        else:
            dot.edge(str(edge.from_node), str(edge.to_node), label=str(edge.weight))
    print(dot.source)
    dot.render('Dijkstra_shortest_path.gv', view=True)