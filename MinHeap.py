class MinHeap:

    def __init__(self, cmp=lambda x: x):
        self.heap = []
        self.map = {}
        self.cmp = cmp

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
        if node_index == 0 or self.cmp(self.heap[p_ind]) <= self.cmp(self.heap[node_index]):
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
            c = lc if self.cmp(self.heap[lc]) <= self.cmp(self.heap[rc]) else rc
        # swap id child is smaller than parent
        if self.cmp(self.heap[ind]) > self.cmp(self.heap[c]):
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