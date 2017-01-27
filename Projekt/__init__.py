import unittest
from ShortestPath import BellmanFord
class Test(unittest.TestCase):
    def testPositiveEdges(self):
        fordAlgorithm = BellmanFord()
        adjacencyMatrix = [
            [None, 3, None, None, None,None],
            [None, None, 6, None, None,None],
            [None, None, None, None, 5,2],
            [None, None, 6, None, 4,None],
            [None, None, None, 2, None,None],
            [None, 7, None, None, None, None]
        ]
        source = 0
        expResult = [[-1, 0, 1, 4, 2, 2], [0, 3, 9, 162, 14, 11]]
        result = fordAlgorithm.ShortestPath(adjacencyMatrix, source)
        self.assertEquals(expResult, result)


    def testPositiveEdges2(self):
        fordAlgorithm = BellmanFord()
        adjacencyMatrix = [
            [None, None, 7, 3, None],
            [9, None, None, 6, None],
            [None, None, None, None, 3],
            [None, 2, 1, None, None],
            [None, None, 2, 5, None]
        ]
        source = 0
        expResult = [[-1, 3, 3, 0, 2], [0, 5, 4, 3, 7]]
        result = fordAlgorithm.ShortestPath(adjacencyMatrix, source)
        self.assertEquals(expResult, result)


    def testNegativeEdges(self):
        fordAlgorithm = BellmanFord()
        adjacencyMatrix = [
            [None, 1, 10, None, None],
            [None, None, None, 2, None],
            [None, None, None, -10, None],
            [None, None, None, None, 3],
            [None, None, None, None, None]
        ]
        source = 0
        expResult = [[-1, 0, 0, 2, 3], [0, 1, 10, 0, 3]]
        result = fordAlgorithm.ShortestPath(adjacencyMatrix, source)
        self.assertEquals(expResult, result)

    def testNegativeEdges2(self):
        fordAlgorithm = BellmanFord()
        adjacencyMatrix = [
            [None, 10, -6, None, None],
            [None, None, None, None, 1],
            [None, 12, None, -5, None],
            [None, None, None, None, 2],
            [None, None, 12, None, None]
        ]
        source = 0
        expResult = [[-1, 2, 0, 2, 3], [0, 6, -6, -11, -9]]
        result = fordAlgorithm.ShortestPath(adjacencyMatrix, source)
        self.assertEquals(expResult, result)

    def testNegativeCycle(self):
        fordAlgorithm = BellmanFord()
        adjacencyMatrix = [
            [None, -1, 4, None, None],
            [None, None, 3, 2, 2],
            [None, -6, None, None, None],
            [None, 1, 5, None, None],
            [None, None, None, -3, None]
        ]
        source = 0
        try:
            fordAlgorithm.ShortestPath(adjacencyMatrix, source)
        except:
            pass
        else:
            self.fail("Should have thrown an exception: Negative cycle present")


    def testNegativeCycle2(self):
        fordAlgorithm = BellmanFord()
        adjacencyMatrix = [
            [None, 99, None, None, -99],
            [None, None, 15, None, None],
            [None, -42, None, 10, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]
        source = 0
        try:
            fordAlgorithm.ShortestPath(adjacencyMatrix, source)
        except:
            pass
        else:
            self.fail("Should have thrown an exception: Negative cycle present")