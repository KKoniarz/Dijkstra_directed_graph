from Node import Node
from MinHeap import MinHeap


class Graph:

    def __init__(self, file):
        f = open(file, 'r')
        # read first line parameters
        params = f.readline().split(" ")
        self.num_of_nodes = int(params[0])
        self.num_of_edges = int(params[1])
        self.start = int(params[2])
        self.end = int(params[3])

        # create dictionary with nodes
        self.nodes = {}
        for i in range(self.num_of_nodes):
            self.nodes[i] = Node()

        # distribute edges across nodes
        for _ in range(self.num_of_edges):
            edge = f.readline().split(" ")
            from_node = int(edge[0])
            cost = int(edge[1])
            to_node = int(edge[2])
            self.nodes[from_node].add_edge(self.nodes[to_node], cost)

        # set node names
        for i in range(self.num_of_nodes):
            self.nodes[i].name = f.readline().strip()

        # close file
        f.close()
        self.calculate_paths()

    def calculate_paths(self):
        mh = MinHeap(cmp=lambda x: x.get_distance())
        s = self.nodes[self.start]
        s.distance = 0
        s.previous = s
        mh.push(s)

        while len(mh) != 0:
            visit_node = mh.pop()
            for n, c in visit_node.edges.items():
                if n.distance > visit_node.distance + c:
                    n.distance = visit_node.distance + c
                    n.previous = visit_node
                    if n in mh:
                        mh.decrease_key(n)
                    else:
                        mh.push(n)

    def get_path(self):
        current_node = self.nodes[self.end]
        cost = current_node.distance
        route = ""
        while current_node.previous != current_node:
            route = " -> " + current_node.name + route
            current_node = current_node.previous
        route = current_node.name + route
        print("Your route:")
        print(route)
        print("Total distance: " + str(cost))
