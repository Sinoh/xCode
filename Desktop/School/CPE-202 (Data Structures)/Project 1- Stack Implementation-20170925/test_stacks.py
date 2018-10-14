# Jeffery Ho
# CPE - 202

import unittest
from stacks import *

class TestStack(unittest.TestCase):


    def test_is_empty(self):
        StackArray1 = StackArray(1)
        StackArray2 = StackArray(1)
        StackArray2.push('Hello World')
        self.assertTrue(StackArray1.is_empty())
        self.assertFalse(StackArray2.is_empty())

    def test_is_full(self):
        StackArray1 = StackArray(1)
        StackArray2 = StackArray(1)
        StackArray2.push('Hello World')
        self.assertFalse(StackArray1.is_full())
        self.assertTrue(StackArray2.is_full())

    def test_push(self):
        StackArray1 = StackArray(1)
        StackArray1.push('Hello World')
        self.assertEqual(StackArray1.items, ['Hello World'])
        self.assertRaises(IndexError, lambda: StackArray1.push('Bye'))


    def test_pop(self):
        StackArray1 = StackArray(1)
        StackArray1.push('Hello World')
        StackArray1.pop()
        self.assertEqual(StackArray1.items, [None])
        self.assertRaises(IndexError, lambda: StackArray1.pop())


    def test_peek(self):
        StackArray1 = StackArray(1)
        StackArray1.push('Hello World')
        StackArray2 = StackArray(1)
        self.assertEqual(StackArray1.peek(), 'Hello World')
        self.assertRaises(IndexError, lambda: StackArray2.peek())


    def test_size(self):
        StackArray1 = StackArray(1)
        StackArray1.push('Hello World')
        StackArray2 = StackArray(1)
        self.assertEqual(StackArray1.size(), 1)
        self.assertEqual(StackArray2.size(), 0)

    def test_StackArray(self):
        Stack1 = StackArray(1)
        Stack2 = StackArray(1)
        Stack3 = StackArray(2)
        Stack3.push('Hello World')
        self.assertTrue(Stack1 == Stack2)
        self.assertFalse(Stack1 == None)
        self.assertEqual(repr(Stack3), "['Hello World', None] | Num_items: 1 | Capacity: 2")

    def test_is_empty_linked(self):
        Stack1 = StackLinked()
        Stack2 = StackLinked(Node('Hello'))
        self.assertTrue(Stack1.is_empty())
        self.assertFalse(Stack2.is_empty())

    def test_push_linked(self):
        Stack1 = StackLinked()
        Stack2 = StackLinked(Node('Hello'))
        Stack3 = Stack2
        Stack4 = StackLinked(Node('World', Node('Hello')))
        Stack5 = StackLinked(Node('Bye', Node('World', Node('Hello'))))
        self.assertEqual(Stack1.push('Hello'), Stack2)
        self.assertEqual(Stack3.push('World'), Stack4)
        self.assertEqual(Stack4.push('Bye'), Stack5)

    def test_pop_linked(self):
        Stack1 = StackLinked()
        Stack2 = StackLinked(Node('Hello'))
        Stack3 = Stack2
        Stack4 = StackLinked(Node('World', Node('Hello')))
        self.assertEqual(Stack2.pop(), Stack1)
        self.assertEqual(Stack4.pop(), Stack3)
        self.assertRaises(IndexError, lambda: Stack1.pop())

    def test_peek_linked(self):
        Stack1 = StackLinked()
        Stack2 = StackLinked(Node('Hello'))
        Stack4 = StackLinked(Node('Hello', Node('World')))
        self.assertEqual(Stack2.peek(), 'Hello')
        self.assertEqual(Stack4.peek(), 'Hello')
        self.assertRaises(IndexError, lambda: Stack1.peek())

    def test_size_linked(self):
        Stack1 = StackLinked()
        Stack2 = StackLinked(Node('Hello'))
        Stack4 = StackLinked(Node('Hello', Node('World')))
        self.assertEqual(Stack1.size(), 0)
        self.assertEqual(Stack2.size(), 1)
        self.assertEqual(Stack4.size(), 2)

    def test_Stack_Linked(self):
        Stack1 = StackLinked()
        Stack2 = StackLinked(Node('Hello'))
        self.assertEqual(repr(Stack2), 'Hello, None')
        self.assertTrue(Stack1 == StackLinked())
        self.assertFalse(Stack1 == None)




if __name__ == "__main__":
    unittest.main()
