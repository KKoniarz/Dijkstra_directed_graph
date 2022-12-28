from sys import maxsize as inf

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
            self.nodes[i] = Node(f.readline().strip())
        # create dictionary withh edges
        self.edges = {}

        # distribute edges across nodes
        for i in range(self.num_of_edges):
            edge_params = f.readline().split(" ")
            from_node = int(edge_params[0])
            weight = int(edge_params[1])
            to_node = int(edge_params[2])
            edge = Edge(self.nodes.get(from_node), self.nodes.get(to_node), weight)
            self.nodes.get(from_node).edges.append(edge)
            self.edges[i] = edge

        # close file
        f.close()
        self.calculate_paths()
        self.__traverse_path()

    def calculate_paths(self):
        mh = MinHeap()
        s = self.nodes[self.start]
        s.distance = 0
        s.previous = s
        mh.push(s)

        while len(mh) != 0:
            visit_node = mh.pop()
            for edge in visit_node.edges:
                if edge.to_node.distance > visit_node.distance + edge.weight:
                    edge.to_node.distance = visit_node.distance + edge.weight
                    edge.to_node.previous = visit_node
                    if edge.to_node in mh:
                        mh.decrease_key(edge.to_node)
                    else:
                        mh.push(edge.to_node)

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

    def __traverse_path(self):
        current_node = self.nodes[self.end]
        while current_node.previous != current_node:
            current_node.is_on_path = True
            previous = current_node.previous
            for edge in previous.edges:
                if edge.to_node == current_node:
                    edge.is_on_path = True
            current_node = previous
        current_node.is_on_path = True

class Node:

    def __init__(self, name):
        self.edges = []
        self.name = name
        self.distance = inf
        self.previous = None
        self.is_on_path = False

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_distance(self):
        return self.distance


class Edge:

    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
        self.is_on_path = False


class MinHeap:

    def __init__(self):
        self.heap = []
        self.map = {}

    def clear(self):
        self.heap = []
        self.map = {}

    def push(self, item):
        self.heap.append(item)  # add new item at the end of array
        self.map[item] = len(self.heap) - 1  # save index of new item
        self.__move_node_up(len(self.heap) - 1)  # correct heap

    def pop(self):
        # if heap is empty raise error
        if len(self.heap) == 0:
            raise IndexError
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.map.pop(self.heap[0])  # save root node to return and delete it from map
        self.heap[0] = self.heap.pop()  # move last element to root
        self.map[self.heap[0]] = 0  # save new root index
        self.__move_node_down(0)
        return root

    def decrease_key(self, item):
        item_ind = self.map[item]  # get item index
        self.map.pop(item)  # remove item from map
        self.__move_node_up(item_ind)

    def __move_node_up(self, node_index):
        p_ind = node_index // 2  # get parent index
        # if reached root or parent is smaller than moved node end
        if node_index == 0 or self.heap[p_ind].distance <= self.heap[node_index].distance:
            return
        else:
            # swap child with parent
            self.__swap(node_index, p_ind)
            # move to the parent node
            self.__move_node_up(p_ind)

    def __move_node_down(self, ind):
        lc = ind * 2 + 1
        rc = ind * 2 + 2
        # has no children (no left child means no right child)
        if lc >= len(self.heap):
            return  # end
        # only has left child, child to swap check is left child
        elif rc >= len(self.heap):
            c = lc
        # has both children, child to swap check is smaller one
        else:
            c = lc if self.heap[lc].distance <= self.heap[rc].distance else rc
        # swap id child is smaller than parent
        if self.heap[ind].distance > self.heap[c].distance:
            self.heap[ind], self.heap[c] = self.heap[c], self.heap[ind]
            self.__move_node_down(c)

    def __swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]
        self.map[self.heap[first]] = first
        self.map[self.heap[second]] = second

    def __contains__(self, item):
        return item in self.heap

    def __len__(self):
        return len(self.heap)