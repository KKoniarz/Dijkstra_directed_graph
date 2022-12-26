from sys import maxsize as inf


class Node:

    def __init__(self):
        self.edges = {}
        self.name = ""
        self.distance = inf
        self.previous = None

    def add_edge(self, to_node, cost):
        self.edges[to_node] = cost

    def get_distance(self):
        return self.distance
