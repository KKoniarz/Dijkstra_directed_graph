import unittest
from MinHeap import MinHeap


class MyTestCase(unittest.TestCase):

    def test_push(self):
        h = MinHeap()
        h.push(100)
        h.push(19)
        h.push(25)
        h.push(17)
        h.push(1)
        h.push(3)
        h.push(2)
        h.push(36)
        h.push(7)
        h.push(0)
        print(h.heap)
        print(h.pop())
        print(h.heap)
        print(h.pop())
        print(h.heap)
        print(h.pop())
        print(h.heap)
        print(h.pop())
        print(h.heap)
        print(h.pop())
        print(h.heap)
        print(h.pop())
        print(h.heap)


if __name__ == '__main__':
    unittest.main()
