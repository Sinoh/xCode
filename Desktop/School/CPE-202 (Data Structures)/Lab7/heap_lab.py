# Name: Jeffery Ho
# Section: 202 - 11

# A MaxHeap is a class
# A capacity is a number
# A heap is a list
# A size is a number
class MaxHeap:
    def __init__(self, capacity=50):
        self.heap = [0]
        self.capacity = capacity
        self.size = 0

    def __repr__(self):
        return "%s , Capacity: %i, Size: %i" % (self.heap, self.capacity, self.size)

    def __eq__(self, other):
        if isinstance(other, MaxHeap):
            return self.heap == other.heap and self.capacity == other.capacity and self.size == other.size
        else:
            return False

    # A insert is a boolean
    # int -> boolean
    # Takes in item as a number and inserts it in the correct place of the heap
    # Checks to make sure the property of the heap is correct
    # Returns True if the item is inserted, and False if item cannot be inserted
    def insert(self, item):
        if self.size < self.capacity:
            self.heap.append(item)
            self.size += 1
            self.perc_up(self.size)
            return True
        else:
            return False

    # A find_max is either
    # A number or None
    # None -> int or None
    # Takes in no parameters and return the max value of the heap or None if not found
    def find_max(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return None

    # A del_max is either
    # A number or None
    # None -> int or None
    # Takes in no parameters and returns the deleted max value, if found and successfully deleted
    # And checks the order property
    # Or returns None if unsuccessful
    def del_max(self):
        if self.is_empty():
            return None
        else:
            max = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.size -= 1
            self.heap.pop()
            self.perc_down(1)
            return max

    # A heaps_content is a list
    # None -> list
    # Take in no parameters and returns a list of the heap
    def heap_contents(self):
        return self.heap

    # A build_heap is a boolean
    # List -> Boolean
    # Takes in a list and builds a heap list out of it
    # Returns True if successful and False if unsuccessful
    def build_heap(self, alist):
        if len(alist) > self.capacity:
            return False

        i = len(alist)//2
        self.size = len(alist)
        self.heap = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i -= 1
        return True

    # A is_empty is a boolean
    # None -> boolean
    # Takes in no parameters and returns True if the heap size is 0, otherwise False
    def is_empty(self):
        return self.size == 0

    # A is_full is a boolean
    # None -> boolean
    # Takes in no parameters and returns True if the heap size is at capacity, otherwise False
    def is_full(self):
        return self.size == self.capacity

    # A get_heap_cap is a number
    # None -> int
    # Takes in no parameters and returns the capacity of the heap
    def get_heap_cap(self):
        return self.capacity

    # A get_heap_size is a number
    # None -> int
    # Takes in no parameter and returns the size of the current heap
    def get_heap_size(self):
        return self.size

    # A perc_down is None
    # Int -> None
    # Takes in an int as the size of the heap and returns the heap with the order property checked
    def perc_down(self, i):
        while (i * 2) <= self.size:
            if i * 2 + 1 > self.size:
                mc = i * 2
            else:
                if self.heap[i * 2] > self.heap[i * 2 + 1]:
                    mc = i * 2
                else:
                    mc = i * 2 + 1

            if self.heap[i] < self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    # A perc_up is None
    # Int -> None
    # Takes in an int as the size of the heap and returns the heap with the order property checked
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    # A heap_sort_increase is a list
    # List -> List
    # Takes in an unsorted list and sorts it in increasing order
    def heap_sort_increase(self, alist):
        heap = MaxHeap()
        heap.build_heap(alist)
        length = len(alist)
        sorted = [0] * (length+1)
        for i in range(length):
            val = heap.del_max()
            sorted[length - i] = val
        return sorted
