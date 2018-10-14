# Name: Jeffery Ho
# Section: 202 - 11

import unittest
from heap_lab import *

class TestList(unittest.TestCase):
    def test_insert(self):
        heap1 = MaxHeap(6)
        heap1.heap = [0,5,4,3,2]
        heap1.size = 4
        heap1.insert(1)
        result1 = MaxHeap(6)
        result1.size = 5
        result1.heap =[0,5,4,3,2,1]
        self.assertEqual(heap1, result1)
        self.assertTrue(heap1.insert(0))
        self.assertFalse(heap1.insert(10))


    def test_find_max(self):
        heap1 = MaxHeap(6)
        heap1.heap = [0,5,4,3,2]
        heap1.size = 4
        heap2 = MaxHeap(6)
        self.assertEqual(heap1.find_max(), 5)
        self.assertFalse(heap2.find_max())

    def test_del_max(self):
        heap1 = MaxHeap(6)
        heap1.heap = [0,5,4,3,2]
        heap1.size = 4
        heap2 = MaxHeap(6)
        heap2.size = 3
        heap2.heap = [0,4,2,3]
        heap3 = MaxHeap(6)
        self.assertEqual(heap1.del_max(), 5)
        self.assertEqual(heap3.del_max(), None)

    def test_heap_contents(self):
        heap1 = MaxHeap(6)
        heap1.heap = [0,5,4,3,2]
        heap1.size = 4
        self.assertEqual(heap1.heap_contents(), [0,5,4,3,2])

    def test_build_heap(self):
        heap1 = MaxHeap(6)
        heap1.heap = [0,5,3,4,2]
        heap1.size = 4
        alist = [2,3,4,5]
        heap2 = MaxHeap(6)
        heap3 = MaxHeap(3)
        self.assertTrue(heap2.build_heap(alist))
        self.assertTrue(heap2 == heap1)
        self.assertFalse(heap3.build_heap(alist))

    def test_is_empty(self):
        heap1 = MaxHeap(6)
        self.assertTrue(heap1.is_empty())
        heap1.insert(1)
        self.assertFalse(heap1.is_empty())

    def test_is_full(self):
        heap1 = MaxHeap(1)
        self.assertFalse(heap1.is_full())
        heap1.insert(1)
        self.assertTrue(heap1.is_full())

    def test_get_heap_cap(self):
        heap1 = MaxHeap(1)
        self.assertEqual(heap1.get_heap_cap(), 1)

    def test_get_heap_size(self):
        heap1 = MaxHeap(1)
        self.assertEqual(heap1.get_heap_size(), 0)

    def test_perc_down(self):
        alist = [2,3,4,5]
        heap1 = MaxHeap(6)
        heap1.build_heap(alist)
        self.assertEqual(heap1.heap, [0,5,3,4,2])

    def test_perc_up(self):
        heap1 = MaxHeap(6)
        heap1.heap = [0,5,2,4,1]
        heap1.size = 4
        heap1.insert(3)
        self.assertEqual(heap1.heap, [0,5,3,4,1,2])

    def test_heap_sort_increase(self):
        heap1 = MaxHeap()
        alist = [1,2,3,4,5,6]
        self.assertEqual(heap1.heap_sort_increase(alist), [0,1,2,3,4,5,6])

if __name__ == '__main__': 
   unittest.main()
