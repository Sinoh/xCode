# Jeffery Ho
# CPE 202


# StackArray is a class
# A capacity is a number
# An item is a string or number
# Num_Items is a number
# Takes in a capacity and sets that as the list's max length
class StackArray:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""
        
    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity		# this is example for list implementation
        self.items = [None]*capacity 		# this is example for list implementation
        self.num_items = 0 			# this is example for list implementation

    def __repr__(self):
        return "%s | Num_items: %i | Capacity: %i" % (self.items, self.num_items, self.capacity)

    def __eq__(self, other):
        if isinstance(other, StackArray):
            return self.items == other.items and self.num_items == other.num_items and self.capacity == other.capacity
        else:
            return False


    # is_empty is a boolean
    # Class -> boolean
    # A method that takes no parameters and returns true if the Class has no items otherwise false
    # StackArray1 = StackArray(1)
    # StackArray2 = StackArray(1)
    # StackArray2.push('Hello World')
    # self.assertTrue(StackArray1.is_empty())
    # self.assertFalse(StackArray2.is_empty())
    # def is_empty(self):
    #   return self.num_items == 0

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return self.num_items == 0

    # is_full is a boolean
    # Class -> boolean
    # A method that takes no parameters and returns true if the capacity is full otherwise false
    # StackArray1 = StackArray(1)
    # StackArray2 = StackArray(1)
    # StackArray2.push('Hello World')
    # self.assertFalse(StackArray1.is_full())
    # self.assertTrue(StackArray2.is_full())
    # def is_full(self):
    #     return self.num_items == self.capacity

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return self.num_items == self.capacity

    # push is a mutation
    # Class String -> None
    # A method that takes in an item and mutates the class with the item on top of the class
    # StackArray1 = StackArray(1)
    # StackArray1.push('Hello World')
    # self.assertEqual(StackArray1.items, ['Hello World'])
    # self.assertRaises(IndexError, lambda: StackArray1.push('Bye'))
    # def push(self, item):
    #     if self.num_items == self.capacity:
    #         ...
    #     else:
    #         self.items[self.num_items] = item
    def push(self, item):
        if self.num_items == self.capacity:
            raise IndexError
        else:
            self.items[self.num_items] = item
            self.num_items += 1

    # pop is a mutation
    # Class -> None
    # A method that takes no parameters and mutates the class with by removing the top item from the list and returns that item
    # StackArray1 = StackArray(1)
    # StackArray1.push('Hello World')
    # StackArray1.pop()
    # self.assertEqual(StackArray1.items, [None])
    # self.assertRaises(IndexError, lambda: StackArray1.pop())
    # def push(self, item):
    #     if self.num_items == 0:
    #         ...
    #     else:
    #         self.items[self.num_items-1] = item
    #         ...
    def pop(self):
        if self.num_items == 0:
            raise IndexError
        else:
            value = self.items[self.num_items-1]
            self.items[self.num_items-1] = None
            self.num_items -= 1
            return value

    # peek is a string
    # Class -> String or number
    # A method that takes no parameters and returns the top item
    # StackArray1 = StackArray(1)
    # StackArray1.push('Hello World')
    # StackArray2 = StackArray(1)
    # self.assertEqual(StackArray1.peek(), 'Hello World')
    # self.assertRaises(IndexError, lambda: StackArray2.peek())
    # def peek(self):
    #     if self.num_items == 0:
    #         ...
    #     return self.items[self.num_items-1]
    def peek(self):
        if self.num_items == 0:
            raise IndexError
        return self.items[self.num_items-1]

    # size is an number
    # Class -> int
    # A method that takes no parameters and returns the size of the stack
    # StackArray1 = StackArray(1)
    # StackArray1.push('Hello World')
    # StackArray2 = StackArray(1)
    # self.assertEqual(StackArray1.size(), 1)
    # self.assertEqual(StackArray2.size(), 0)
    # def size(self):
    #     return self.nums_items
    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items

# Node is a class
# Value is a string or number
# Rest is None or Node
# Takes in a value and rest and links them
class Node:
    def __init__(self, value=None, rest=None):
        self.value = value
        self.rest = rest

    def __repr__(self):
        return "%s, %s" % (self.value, self.rest)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value and self.rest == other.rest
        else:
            return False

# StackLinked is a wrapper class
# node is either None or the Node Class
# A wrapper class for the Node class
class StackLinked:
    def __init__(self, capacity = 0):
        self.capacity = capacity
        self.node = None
        self.num_items = self.size

    def __repr__(self):
        return ('%s' % (self.node))

    def __eq__(self,other):
        if isinstance(other, StackLinked):
            return self.node == other.node
        else:
            return False

    # is_empty is a boolean
    # Class -> boolean
    # A method that takes no parameters and returns true if the Class has no items otherwise false
    # Stack1 = StackLinked()
    # Stack2 = StackLinked(Node('Hello'))
    # self.assertTrue(Stack1.is_empty())
    # self.assertFalse(Stack2.is_empty())
    # def is_empty(self):
    #   return self == StackLinked()
    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return self == StackLinked()


    # is_full is a boolean
    # Class -> boolean
    # A method that takes no parameters and returns true if the Class has no items otherwise false
    # StackArray1 = StackArray(1)
    # StackArray2 = StackArray(1)
    # StackArray2.push('Hello World')
    # self.assertFalse(StackArray1.is_full())
    # self.assertTrue(StackArray2.is_full())
    # def is_full(self):
    #   return self.size() == self.capacity
    def is_full(self):
        return self.size() == self.capacity

    # push is a mutation
    # Class String -> None
    # A method that takes in an item and mutates the class with the item on top of the class
    # Stack1 = StackLinked()
    # Stack2 = StackLinked(Node('Hello'))
    # Stack3 = Stack2
    # Stack4 = StackLinked(Node('World', Node('Hello')))
    # Stack5 = StackLinked(Node('Bye', Node('World', Node('Hello'))))
    # self.assertEqual(Stack1.push('Hello'), Stack2)
    # self.assertEqual(Stack3.push('World'), Stack4)
    # self.assertEqual(Stack4.push('Bye'), Stack5)
    # def push(self, item):
    #     if self.node == None:
    #         ...
    #     else:
    #         return StackLinked(Node(item,self.node))
    def push(self, item):
        if self.is_full():
            raise IndexError
        if self.node == None:
            self.node = Node(item)
        else:
            self.node.rest = Node(self.node.value,self.node.rest)
            self.node = Node(item, self.node.rest)

    # pop is a mutation
    # Class -> None
    # A method that takes no parameters and mutates the class with by removing the top item from the list and returns that item
    # Stack1 = StackLinked()
    # Stack2 = StackLinked(Node('Hello'))
    # Stack3 = Stack2
    # Stack4 = StackLinked(Node('World', Node('Hello')))
    # self.assertEqual(Stack2.pop(), Stack1)
    # self.assertEqual(Stack4.pop(), Stack3)
    # self.assertRaises(IndexError, lambda: Stack1.pop())
    # def push(self, item):
    #     if self.is_empty():
    #         ...
    #     else:
    #         return StackLinked(self.node.rest)
    def pop(self):
        if self.is_empty():
            raise IndexError
        else:
            value = self.node.value
            self.node = self.node.rest
            return value

    # peek is a string
    # Class -> String or number
    # A method that takes no parameters and returns the top item
    # Stack1 = StackLinked()
    # Stack2 = StackLinked(Node('Hello'))
    # Stack4 = StackLinked(Node('Hello', Node('World')))
    # self.assertEqual(Stack2.peek(), 'Hello')
    # self.assertEqual(Stack4.peek(), 'Hello')
    # self.assertRaises(IndexError, lambda: Stack1.peek())
    # def peek(self):
    #     if self.is_empty():
    #         ...
    #     return self.node.value
    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.node.value

    # size is an number
    # Class -> int
    # A method that takes no parameters and returns the size of the stack
    # Stack1 = StackLinked()
    # Stack2 = StackLinked(Node('Hello'))
    # Stack4 = StackLinked(Node('Hello', Node('World')))
    # self.assertEqual(Stack1.size(), 0)
    # self.assertEqual(Stack2.size(), 1)
    # self.assertEqual(Stack4.size(), 2)
    # def size(self):
    #     if self.node == None:
    #         ...
    #     else:
    #         return 1 + self.node.rest.size
    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""

        def length(AnyList):
            if AnyList == None:
                return 0
            else:
                return 1 + length(AnyList.rest)

        return length(self.node)