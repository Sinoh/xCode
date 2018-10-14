# Name: Jeffery Ho
# Section: 202 - 11

import unittest
from sep_chain_ht import *

class TestList(unittest.TestCase):
    def test_insert(self):
        table = MyHashTable()
        table.insert(60, 'dog')
        table.insert(7, 'cat')
        table.insert(5, 'bird')
        result = MyHashTable()
        result.table = [[],[],[],[],[],[(60, 'dog'), (5, 'bird')],[],[(7, 'cat')],[],[],[]]
        result.num_items = 3
        result.num_collisions = 1
        self.assertTrue(table == result)
        table2 = MyHashTable(5)
        table2.insert(1, 'dog')
        table2.insert(6, 'cat')
        table2.insert(11, 'bird')
        table2.insert(16, 'this')
        table2.insert(21, 'is')
        table2.insert(26, 'really')
        table2.insert(31, 'boring')
        table2.insert(37, 'I')
        result2 = MyHashTable()
        result2.table = [[(11, 'bird')], [(1, 'dog')], [], [], [(26, 'really'),(37, 'I')], [(16, 'this')], [(6, 'cat')], [], [], [(31, 'boring')], [(21, 'is')]]
        result2.num_items = 8
        result2.num_collisions = 7
        self.assertTrue(table2 == result2)

    def test_get(self):
        table = MyHashTable()
        table.insert(60, 'dog')
        table.insert(7, 'cat')
        table.insert(5, 'bird')
        self.assertEqual(table.get(60), (60, 'dog'))
        self.assertRaises(LookupError, lambda: table.get(1))

    def test_remove(self):
        table = MyHashTable()
        table.insert(60, 'dog')
        table.insert(7, 'cat')
        table.insert(5, 'bird')
        self.assertEqual(table.remove(5), (5, 'bird'))
        self.assertRaises(LookupError, lambda: table.remove(1))

    def test_size(self):
        table = MyHashTable()
        table.insert(60, 'dog')
        table.insert(7, 'cat')
        table.insert(5, 'bird')
        self.assertEqual(table.size(), 3)
        table.remove(60)
        self.assertEqual(table.size(), 2)

    def test_load_factor(self):
        table = MyHashTable()
        table.insert(60, 'dog')
        table.insert(7, 'cat')
        table.insert(5, 'bird')
        self.assertEqual(table.load_factor(), 0.2727272727272727)
        table.remove(60)
        self.assertEqual(table.load_factor(), 0.18181818181818182)

    def test_collisions(self):
        table = MyHashTable(5)
        table.insert(1, 'dog')
        table.insert(6, 'cat')
        table.insert(11, 'bird')
        self.assertEqual(table.collisions(), 2)
        table.insert(16, 'this')
        table.insert(21, 'is')
        table.insert(26, 'really')
        table.insert(31, 'boring')
        table.insert(37, 'I')
        self.assertEqual(table.collisions(), 7)

if __name__ == '__main__': 
   unittest.main()
