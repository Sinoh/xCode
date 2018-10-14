# Name: Jeffery Ho
# Section: 202 - 11

import unittest
from my_graph import *

class TestList(unittest.TestCase):

    def test_Vertex(self):
        Vertex1 = Vertex(1)
        Vertex2 = Vertex(2)
        Vertex3 = Vertex(3)
        Vertex1.addConnection(Vertex2)
        Vertex2.addConnection(Vertex3)
        Vertex4 = Vertex(1)
        Vertex4.connectedTo['2'] = 0
        self.assertTrue(Vertex1 == Vertex4)
        self.assertFalse(Vertex1 == Vertex3)

    def test_return_conections(self):
        Vertex1 = Vertex(1)
        Vertex2 = Vertex(2)
        Vertex3 = Vertex(3)
        Vertex1.addConnection(Vertex2)
        Vertex2.addConnection(Vertex3)
        self.assertEqual(Vertex1.return_connections(), [2])
        self.assertEqual(Vertex2.return_connections(), [1, 3])

    def test_graph(self):
        graph = MyGraph('input1.txt')
        graph2 = MyGraph('input2.txt')
        print(graph.conn_components())
        print(graph2.conn_components())


if __name__ == '__main__': 
   unittest.main()
