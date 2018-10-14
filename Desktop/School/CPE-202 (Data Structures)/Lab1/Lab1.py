# Name: Jeffery Ho
# Section: 202 -

# must use iteration not recursion
# Max_list_iter is a int
# tlist is a list of numbers
# List -> int
# Takes a list and returns the max of the list. Will return ValueError if list is empty.
# tlist = [10, 9, 8 ,4, 9]
# tlist2 = []
# tlist3 = [1,2,3,4,5,6,7]
# self.assertEqual(max_list_iter(tlist),10)
# with self.assertRaises(ValueError):
#   max_list_iter(tlist2)
# self.assertEqual(max_list_iter(tlist3),7)
# for i in tlist:
#   if x < i:
#       x = i

def max_list_iter(tlist):
    """ finds the max of a list of numbers and returns it, not the index"""
    if tlist == []:
        raise ValueError
    x = tlist[0]
    for i in tlist:
        if x < i:
            x = i
    return x

# must use recursion
# Reverse_rev is a list
# tempstr is a list of numbers
# List -> List
# Takes in a list and returns the list backwards
# self.assertEqual(reverse_rec("abcd"),"dcba")
# self.assertEqual(reverse_rec([1,2,3,4]), [4,3,2,1])
# self.assertEqual(reverse_rec('1234'), '4321')
# return tempstr[-1:] + reverse_rec(tempstr[:-1]

def reverse_rec(tempstr):   
    """ recursively reverses a list of numbers and returns it """
    if not tempstr:
        return tempstr
    return tempstr[-1:] + reverse_rec(tempstr[:-1])

# Binary Search
# write your recursive binary search code here
# Bin_search is an int
# Target is a number
# low is the lowest index in the list
# high is the highest index in the list
# Int, Int, Int, List -> Int
# Takes in a target, the low index, the high index, and the list and returns the index of the target.
# If the target is not found, will return None. If list is empty, will return None.
# list = []
# self.assertEqual(bin_search(1,0,8,list), None)
# list = [1,2,3,4,5,6,7,8,9]
# self.assertEqual(bin_search(6,0,8,list), 5)
# self.assertEqual(bin_search(1,0,8,list), 0)
# self.assertEqual(bin_search(10,0,8,list), None)
# self.assertEqual(bin_search(9,0,8,list), 8)
# if target == list_val[middle]:
#     return middle
# elif target < list_val[middle]:
#     return bin_search(target, low, middle - 1, list_val)
# else:
#     return bin_search(target, middle + 1, high, list_val)
def bin_search(target, low, high, list_val):
    """ searches for target in list_val[low..high] and returns index if found"""
    if list_val == []:
        return None

    if high >= low:
        middle = low + (high-low)/2
        if target == list_val[middle]:
            return middle
        elif target < list_val[middle]:
            return bin_search(target, low, middle-1, list_val)
        else:
            return bin_search(target, middle+1, high, list_val)
    else:
        return None

