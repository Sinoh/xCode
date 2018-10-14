# Name: Jeffery Ho
# Section: 202 - 11
# Data Definition

# A HuffmanNode is a class
# a char is a ASCII number
# a freq is a number
# a left is either a HuffmanNode or none
# a right is either a HuffmanNode or none
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # actually the character code
        self.freq = freq
        self.code = None
        self.left = None
        self.right = None

    def __repr__(self):
        return "[%s: %i; (%s, %s)]" % (self.char, self.freq, self.left, self.right)

    def __eq__(self, other):
        if isinstance(other, HuffmanNode):
            return self.char == other.char and self.freq == other.freq and self.code == other.code and self.left == other.left and self.right == other.right
        else:
            return False

   # add any necessary functions you need

# A comes_before is a boolean
# tree tree -> boolean
# Takes in two HuffmanNodes and return true if the first node comes before the second node
# returns true if tree rooted at node a comes before tree rooted at node b
def comes_before (a, b):
    if a.freq == b.freq:
        return a.char < b.char
    return a.freq < b.freq

# A cnt_freq is a list
# string -> list
# Takes in a string that is a file name with the extension '.txt' and returns a list
# That contains the frequencies of all the characters in that file
def cnt_freq(filename):
    in_file = open(filename, 'r')
    output = [0] * 256
    for line in in_file:
        for char in line:
            output[ord(str(char))] += 1
    in_file.close()
    return output

# A sort_min is a list
# list -> list
# Takes a list of huffman nodes and sorts the items from min to max
def sort_min(source_list):
    sorted_list = []
    while source_list:
        minimum = source_list[0]
        for x in source_list:
            if comes_before(x, minimum):
                minimum = x

        sorted_list.append(minimum)
        source_list.remove(minimum)
    return sorted_list

# A create_huff_tree is a HuffmanNode
# list -> Node
# Takes in a list that contains the frequencies of all the characters in a text file
# And returns the correct Huffman Tree with all the characters
def create_huff_tree(char_freq):
    source_list = []
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            source_list.append(HuffmanNode(i, char_freq[i]))
    sorted_list = sort_min(source_list)

    if len(sorted_list) == 0:
        return sorted_list

    if len(sorted_list) == 1:
        temp_node = HuffmanNode(sorted_list[0].char, sorted_list[0].freq)
        del sorted_list[0]
        sorted_list.append(temp_node)

    while len(sorted_list) > 1:
        node_1 = sorted_list[0]
        node_2 = sorted_list[1]

        if node_1.char < node_2.char:
            char = node_1.char
        else:
            char = node_2.char
        temp_node = HuffmanNode(char, node_1.freq + node_2.freq)
        temp_node.left = node_1
        temp_node.right = node_2
        del sorted_list[0]
        del sorted_list[0]
        sorted_list.append(temp_node)
        sorted_list = sort_min(sorted_list)

    return sorted_list[0]

# A create_code is a list
# Node -> list
# Takes in a Huffman Tree and traverses the tree in order to find the code for each character
# And returns a list with all the codes
def create_code (node):
    code_list = [0]*256

    def iterator(tree, path=''):
        if tree.left == tree.right == None:
            code_list[tree.char] = path
        else:

            iterator(tree.left, path + '0')
            iterator(tree.right, path + '1')

    if node != []:
        iterator(node)
    return code_list

# A Huffman_encode is a None
# String String -> None
# Takes in two strings, the first is the name of the input text file, and the second is the output text file
# And writes to the output file the huffman code of the input file
def huffman_encode(in_file, out_file):
    try:
        input = open(in_file, 'r')
    except OSError:
        raise OSError
    output = open(out_file, 'w')

    freq = cnt_freq(in_file)

    huffman_tree = create_huff_tree(freq)
    code_list = create_code(huffman_tree)
    code = ''

    for line in input:
        if line == '':
            break
        for char in line:
            code = code + str(code_list[ord(char)])

    output.write(code)
    input.close()
    output.close()

# A Huffman_encode is a None
# List String String -> None
# Takes in two strings, the first is the name of the input text file, and the second is the output text file and a list of frequencies of the characters
# And writes to the output file the decoded huffman code of the input file
def huffman_decode(freqs, encoded_file, decode_file):
    try:
        input = open(encoded_file, 'r')
    except OSError:
        raise OSError
    output = open(decode_file, 'w')

    huffman_tree = create_huff_tree(freqs)
    decode = ''

    tree = huffman_tree

    for line in input:
        for char in line:

            if char == '0':
                tree = tree.left
            if char == '1':
                tree = tree.right

            if tree.right == tree.left == None:
                decode += str(chr(tree.char))
                tree = huffman_tree

    output.write(decode)
    input.close()
    output.close()

# tree_preord is a string
# tree -> string
# takes in a huffman tree and returns a header for the huffman decode in string format
# Will traverse the tree in pre_order and for every node that is not a leaf, add a '0' to the string
# And if it is a leaf adds a '1' and the character of the leaf to the string
def tree_preord(node, string = ''):

    if node:
        if node.right == node.left == None:
            string += '1' + str(chr(node.char))
            return string

        if node.left != None:
            string = tree_preord(node.left, string + '0')

        if node.right != None:
            string = tree_preord(node.right, string)

    return string