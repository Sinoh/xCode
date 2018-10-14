#Test Cases for Lab1
from Lab1 import *

import unittest

class TestCase(unittest.TestCase):
    def test_max_list_iter(self):
        tlist = [10, 9, 8 ,4, 9]
        self.assertEqual(max_list_iter(tlist),10)
        tlist = []
        with self.assertRaises(ValueError):  # magic - uses context manager
            max_list_iter(tlist)
        tlist = [1,2,3,4,5,6,7]
        self.assertEqual(max_list_iter(tlist),7)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec("abcd"),"dcba")
        self.assertEqual(reverse_rec([1,2,3,4]), [4,3,2,1])
        self.assertEqual(reverse_rec('1234'), '4321')

    def test_bin_search(self):
        # Add code here.
        list = []
        self.assertEqual(bin_search(1,0,8,list), None)
        list = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(bin_search(6,0,8,list), 5)
        self.assertEqual(bin_search(1,0,8,list), 0)
        self.assertEqual(bin_search(10,0,8,list), None)
        self.assertEqual(bin_search(9,0,8,list), 8)
        
       
        
# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
