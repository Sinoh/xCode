# Name: Jeffery Ho
# Section: 202 -

# QueueArray is a class
# A capacity is a number
# A items is a list
# A num_items is a number
# A front is a number
# A rear is a number
# Takes in a capacity and sets that as the list's max length
class QueueArray:
    def __init__(self, capacity = 0):
 # the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.front = 0
        self.rear = 0

    def __repr__(self):
        return ("%s | Capacity: %i | Num_items %i | Front: %i | Rear: %i" % (self.items, self.capacity, self. num_items, self.front, self.rear))

    def __eq__(self, other):
        if isinstance(other, QueueArray):
            return self.items == other.items and self.front == other.front and self.rear == other.rear
        else:
            return False

    # is_empty is a boolean
    # Class -> boolean
    # A method that takes no parameters and returns true if the Class has no items otherwise false
    # array1 = QueueArray(10)
    # array2 = QueueArray(1)
    # array2.enqueue('Hello')
    # self.assertTrue(array1.is_empty())
    # self.assertFalse(array2.is_empty())
    # def is_empty(self):
    #   return self.num_items == 0
    def is_empty(self):
        return self.num_items == 0

    # is_full is a boolean
    # Class -> boolean
    # A method that takes no parameters and returns true if the capacity is full otherwise false
    # array1 = QueueArray(10)
    # array2 = QueueArray(1)
    # array2.enqueue('Hello')
    # self.assertTrue(array2.is_full())
    # self.assertFalse(array1.is_full())
    # def is_full(self):
    #     return self.num_items == self.capacity
    def is_full(self):
        return self.num_items== self.capacity

    # enqueue is a mutation
    # Class String -> None
    # A method that takes in an item and mutates the class with the item on top of the class
    # array1 = QueueArray(2)
    # array2 = QueueArray(2)
    # array3 = QueueArray(2)
    # array2.items = ['Hello', None]
    # array2.rear = 1
    # array3.items = ['Hello', 'World']
    # array1.enqueue('Hello')
    # self.assertEqual(array1, array2)
    # array1.enqueue('World')
    # self.assertEqual(array1, array3)
    # self.assertRaises(IndexError, lambda: array1.enqueue('Bye'))
    # array2.rear = 0
    # self.assertRaises(IndexError, lambda: array2.enqueue('Bye'))
    # def enqueue(self, item):
    #     if self.is_full():
    #         ...
    #     else:
    #         self.items[self.rear] = item
    #         ...
    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        if self.items[self.rear] != None:
            raise IndexError
        else:
            self.items[self.rear] = item
            self.rear += 1
            self.num_items += 1
            if self.rear == self.capacity:
                self.rear = 0

    # dequeue is a mutation
    # Class -> None
    # A method that takes no parameters and mutates the class with by removing the top item from the items and returns that item
    # array1 = QueueArray(2)
    # array2 = QueueArray(2)
    # array3 = QueueArray(2)
    # array2.items = [None, 'World']
    # array2.num_items = 1
    # array2.front = 1
    # array2.rear = 0
    # array3.enqueue('Hello')
    # array3.enqueue('World')
    # array3.dequeue()
    # self.assertEqual(array3, array2)
    # array3.dequeue()
    # self.assertEqual(array3, array1)
    # self.assertRaises(IndexError, lambda: array3.dequeue())
    # array2.front = 0
    # self.assertRaises(IndexError, lambda: array2.dequeue())
    # def dequeue(self, item):
    #     if is_empty():
    #         ...
    #     else:
    #         self.items[self.front] = item
    #         ...
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        if self.items[self.front] == None:
            raise IndexError
        else:
            self.items[self.front] = None
            self.front += 1
            self.num_items -= 1
            if self.front == self.capacity:
                self.front = 0

    # num_in_queue is an number
    # Class -> int
    # A method that takes no parameters and returns the size of the stack
    # array1 = QueueArray(2)
    # array2 = QueueArray(2)
    # array3 = QueueArray(2)
    # array2.enqueue('Hello')
    # array3.enqueue('Hello')
    # array3.enqueue('World')
    # self.assertEqual(array1.num_in_queue(), 0)
    # self.assertEqual(array2.num_in_queue(), 1)
    # self.assertEqual(array3.num_in_queue(), 2)
    # def num_items(self):
    #     return self.nums_items
    def num_in_queue(self):
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

# QueueLinked is a class
# A capacity is a number
# A num_items is a number
# A front is a list
# A rear is a list
# Takes in a capacity and sets that as the list's max length
class QueueLinked:
    def __init__(self, capacity = 0):
        # the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.num_items = 0
        self.front = None
        self.rear = None

    def __repr__(self):
        return ('%i, %i, %s, %s' % (self.capacity, self.num_items, self.front, self.rear))

    def __eq__(self, other):
        if isinstance(other, QueueLinked):
            return self.capacity == other.capacity and self.num_items == other.num_items and self.front == other.front and self.rear == other.rear
        else:
            return False

    # is_empty is a boolean
    # Class -> boolean
    # A method that takes no parameters and returns true if the Class has no items otherwise false
    # linked1 = QueueLinked()
    # linked2 = QueueLinked(1)
    # linked2.enqueue('Hello')
    # self.assertTrue(linked1.is_empty())
    # self.assertFalse(linked2.is_empty())
    # def is_empty(self):
    #   return self.num_items == 0
    def is_empty(self):
        return self.num_items == 0

    # is_full is a boolean
    # Class -> boolean
    # A method that takes no parameters and returns true if the capacity is full otherwise false
    # linked1 = QueueLinked(1)
    # linked2 = QueueLinked(1)
    # linked2.enqueue('Hello')
    # self.assertFalse(linked1.is_full())
    # self.assertTrue(linked2.is_full())
    # def is_full(self):
    #     return self.num_items == self.capacity
    def is_full(self):
        return self.num_items == self.capacity

    # enqueue is a mutation
    # Class String -> None
    # # A method that takes in an item and mutates the class with the item on top of the class
    # linked1 = QueueLinked(2)
    # linked2 = QueueLinked(2)
    # linked2.enqueue('Hello')
    # linked3 = QueueLinked(2)
    # linked3.enqueue('Hello')
    # linked3.enqueue('World')
    # linked4 = QueueLinked(3)
    # linked4.enqueue('Hello')
    # linked4.enqueue('World')
    # linked4.enqueue("Bye")
    # linked1.enqueue('Hello')
    # self.assertEqual(linked1, linked2)
    # linked1.enqueue('World')
    # self.assertEqual(linked1, linked3)
    # self.assertRaises(IndexError, lambda: linked1.enqueue('Bye'))
    # def enqueue(self, item):
    #     if self.is_full():
    #         ...
    #     else:
    #         node = Node(item)
    #         ...
    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        if self.front == self.rear:
            if self.is_empty():
                self.rear = Node(item)
                self.front = Node(item)
            else:
                node = Node(item)
                self.front.rest = node
                self.rear = node
        else:
            node = Node(item)
            self.rear.rest = node
            self.rear = node
        self.num_items += 1



    # dequeue is a mutation
    # Class -> None
    # A method that takes no parameters and mutates the class with by removing the top item from the items and returns that item
    # linked1 = QueueLinked(2)
    # linked2 = QueueLinked(2)
    # linked2.enqueue('Hello')
    # linked3 = QueueLinked(2)
    # linked3.enqueue('Hello')
    # linked3.enqueue('World')
    # self.assertEqual(QueueLinked.dequeue(linked3), 'Hello')
    # self.assertEqual(QueueLinked.dequeue(linked3), 'World')
    # self.assertRaises(IndexError, lambda: linked1.dequeue())
    # def dequeue(self, item):
    #     if is_empty():
    #         ...
    #     else:
    #         result = self.front.value
    #         ...
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        if self.front == self.rear:
            result = self.front.value
            self.front = None
            self.rear = None
            self.items = None
        else:
            result = self.front.value
            self.front = self.front.rest
        self.num_items -= 1
        return result

    # num_in_queue is an number
    # Class -> int
    # A method that takes no parameters and returns the size of the stack
    # linked1 = QueueLinked(2)
    # linked2 = QueueLinked(2)
    # linked3 = QueueLinked(2)
    # linked2.enqueue('Hello')
    # linked3.enqueue('Hello')
    # linked3.enqueue('World')
    # self.assertEqual(linked1.num_in_queue(), 0)
    # self.assertEqual(linked2.num_in_queue(), 1)
    # self.assertEqual(linked3.num_in_queue(), 2)
    # def num_items(self):
    #     return self.nums_items
    def num_in_queue(self):
        return self.num_items
