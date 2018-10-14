# Name: Jeffery Ho
# Section: 202 -

#Test Cases for Lab3
from queue import *

import unittest

class TestCase(unittest.TestCase):
    def test_QueueArray_is_empty(self):
        array1 = QueueArray(10)
        array2 = QueueArray(1)
        array2.enqueue('Hello')
        self.assertTrue(array1.is_empty())
        self.assertFalse(array2.is_empty())

    def test_QueueArray_is_full(self):
        array1 = QueueArray(10)
        array2 = QueueArray(1)
        array2.enqueue('Hello')
        self.assertTrue(array2.is_full())
        self.assertFalse(array1.is_full())

    def test_QueueArray_enqueue(self):
        array1 = QueueArray(2)
        array2 = QueueArray(2)
        array3 = QueueArray(2)
        array2.items = ['Hello', None]
        array2.rear = 1
        array3.items = ['Hello', 'World']
        array1.enqueue('Hello')
        self.assertEqual(array1, array2)
        array1.enqueue('World')
        self.assertEqual(array1, array3)
        self.assertRaises(IndexError, lambda: array1.enqueue('Bye'))
        array2.rear = 0
        self.assertRaises(IndexError, lambda: array2.enqueue('Bye'))

    def test_QueueArray_dequeue(self):
        array1 = QueueArray(2)
        array2 = QueueArray(2)
        array3 = QueueArray(2)
        array2.items = [None, 'World']
        array2.num_items = 1
        array2.front = 1
        array2.rear = 0
        array3.enqueue('Hello')
        array3.enqueue('World')
        array3.dequeue()
        self.assertEqual(array3, array2)
        array3.dequeue()
        self.assertEqual(array3, array1)
        self.assertRaises(IndexError, lambda: array3.dequeue())
        array2.front = 0
        self.assertRaises(IndexError, lambda: array2.dequeue())


    def test_QueueArray_num_in_queue(self):
        array1 = QueueArray(2)
        array2 = QueueArray(2)
        array3 = QueueArray(2)
        array2.enqueue('Hello')
        array3.enqueue('Hello')
        array3.enqueue('World')
        self.assertEqual(array1.num_in_queue(), 0)
        self.assertEqual(array2.num_in_queue(), 1)
        self.assertEqual(array3.num_in_queue(), 2)

    def test_QueueArray(self):
        array1 = QueueArray(2)
        array2 = QueueArray(2)
        array3 = QueueArray(2)
        array2.items = ['Hello', None]
        array2.rear = 1
        array3.items = ['Hello', 'World']
        array1.enqueue('Hello')
        self.assertEqual(repr(array1), "['Hello', None] | Capacity: 2 | Num_items 1 | Front: 0 | Rear: 1" )
        self.assertTrue(array1 == array2)
        self.assertFalse(array1 == None)

    def test_QueueLinked_is_empty(self):
        linked1 = QueueLinked()
        linked2 = QueueLinked(1)
        linked2.enqueue('Hello')
        self.assertTrue(linked1.is_empty())
        self.assertFalse(linked2.is_empty())

    def test_QueueLinked_is_full(self):
        linked1 = QueueLinked(1)
        linked2 = QueueLinked(1)
        linked2.enqueue('Hello')
        self.assertFalse(linked1.is_full())
        self.assertTrue(linked2.is_full())

    def test_QueueLinked_enqueue(self):
        linked1 = QueueLinked(2)
        linked2 = QueueLinked(2)
        linked2.enqueue('Hello')
        linked3 = QueueLinked(2)
        linked3.enqueue('Hello')
        linked3.enqueue('World')
        linked4 = QueueLinked(3)
        linked4.enqueue('Hello')
        linked4.enqueue('World')
        linked4.enqueue("Bye")
        linked1.enqueue('Hello')
        self.assertEqual(linked1, linked2)
        linked1.enqueue('World')
        self.assertEqual(linked1, linked3)
        self.assertRaises(IndexError, lambda: linked1.enqueue('Bye'))

    def test_QueueLinked_dequeue(self):
        linked1 = QueueLinked(2)
        linked2 = QueueLinked(2)
        linked2.enqueue('Hello')
        linked3 = QueueLinked(2)
        linked3.enqueue('Hello')
        linked3.enqueue('World')
        self.assertEqual(QueueLinked.dequeue(linked3), 'Hello')
        self.assertEqual(QueueLinked.dequeue(linked3), 'World')
        self.assertRaises(IndexError, lambda: linked1.dequeue())


    def test_QueueLinked_num_in_queue(self):
        linked1 = QueueLinked(2)
        linked2 = QueueLinked(2)
        linked3 = QueueLinked(2)
        linked2.enqueue('Hello')
        linked3.enqueue('Hello')
        linked3.enqueue('World')
        self.assertEqual(linked1.num_in_queue(), 0)
        self.assertEqual(linked2.num_in_queue(), 1)
        self.assertEqual(linked3.num_in_queue(), 2)

    def test_QueueLinked(self):
        linked1 = QueueLinked(2)
        linked2 = QueueLinked(2)
        linked1.enqueue('Hello')
        linked2.enqueue('Hello')
        self.assertEqual(repr(linked1), '2, 1, Hello, None, Hello, None')
        self.assertTrue(linked1 == linked2)
        self.assertFalse(linked1 == None)

    def test_Node(self):
        node1 = Node('Hello')
        self.assertFalse(node1 == None)

# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
