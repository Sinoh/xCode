# Name: Jeffery Ho
# Section: 202 -

# Perm_lex is a list
# A string is a string of characters
# String -> List
# Takes in a string as an input and returns a list of all the permutations in lexicographic order
# self.assertEqual(perm_lex('abc'), [abc, acb, bac, bca, cab, cba])
# If the string contains a single character return a list containing that string
# def perm_lex(string):
# if len(string) = 0:
#       return []
# if len(string) = 1:
#       return [string]
# else:
#   run permutation  by
#   Loop through all character positions of the string containing the characters to be permuted, for each character:
#   Form a simpler string by removing the character
#   Generate all permutations of the simpler string recursively
#   Add the removed character to the front of each permutation of the simpler word, and
#   add the resulting permutation to a list
#   Return all these newly constructed permutations

def perm_lex(string):
    if len(string) == 0:
        return ['']
    if len(string) == 1:
        return [string]
    else:
        result = []

        for i in range(len(string)):
            letter = string[i]
            rst_list = string[:i] + string[i+1:]

            for p in perm_lex(rst_list):
                result.append(letter + p)
        return result
