#Test Cases for Lab1
from perm_lex import *

import unittest

class TestCase(unittest.TestCase):
    def test_perm_lex(self):
        self.assertEqual(perm_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(perm_lex('a'), ['a'])
        self.assertEqual(perm_lex(''), [''])

# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
