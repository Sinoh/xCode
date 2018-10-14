import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_cnt_freq(self):
      freqlist	= cnt_freq("file1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 97)
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 97)
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 100)

   def test_create_code(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')

   def test_01_encodefile(self):
      huffman_encode("file1.txt", "output1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))

   def test_comes_before(self):
      a = HuffmanNode(10,10)
      b = HuffmanNode(20,10)
      c = HuffmanNode(10,20)
      self.assertTrue(comes_before(a,b))
      self.assertTrue(comes_before(a,c))

   def test_sort_min(self):
      a = [HuffmanNode(1,10), HuffmanNode(2,3), HuffmanNode(3,1)]
      b = [HuffmanNode(3,1), HuffmanNode(2,3), HuffmanNode(1,10)]
      self.assertEqual(sort_min(a), b)

   def test_tree_preord(self):
      list1 = [0] * 256
      list1[97:104] = [2, 4, 8, 16, 0, 2, 0]
      tree = create_huff_tree(list1)
      result = '00001a1f1b1c1d'
      self.assertEqual(tree_preord(tree), result)
      list2 = [0] * 256
      list2[97:100] = [4, 3, 2, 1]
      list2[32] = 3
      tree2 = create_huff_tree(list2)
      result2 = '001 1b001d1c1a'
      self.assertEqual(tree_preord(tree2), result2)


   def test_01_decodefile(self):
      freqlist = cnt_freq("file1.txt")
      huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))

if __name__ == '__main__': 
   unittest.main()
