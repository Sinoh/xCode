class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def OrderedLinked(self):
        self.head = Node()

    def add(self, item, temp = None):
        if self.is_empty():
            newnode = Node(item)
            self.head = newnode
            self.tail = newnode

        if temp == None:
            temp = self.head
        if temp.next == None:
            newnode = Node(item)
            temp.next = newnode
            newnode.prev = temp
            self.tail = newnode
        if temp.item <= item:
            return self.add(item, temp.next)
        if temp.item > item:
            newnode = Node(item)
            newnode.next = temp  # next
            newnode.prev = temp.prev  # prev
            temp.prev.next = newnode  # prev's next
            temp.prev = newnode  # next's prev

    def remove(self, item, temp = None):
        if temp == None:
            temp = self.head
        if temp == None:
            return -1
        if temp.item == item:
            temp.prev.next = temp.next  # prev's next
            temp.next.prev = temp.prev  # next's prev
        else:
            return self.remove(item)

    def search_forward(self, item, temp = None):
        if temp == None:
            temp = self.head

        if temp.is_empty():
            return False
        if item == temp.item:
            return True
        if temp.next == None:
            return False
        else:
            return self.search_forward(item, temp.next)


    def search_backward(self, item, temp = None):
        if temp == None:
            temp = self.tail

        if temp.is_empty():
            return False
        if item == temp.item:
            return True
        if temp.prev == None:
            return False
        else:
            return self.search_backward(item, temp.prev)

    def is_empty(self):
        return self.head == None

    def size(self, count=0, temp = None):
        if temp == None:
            temp = self.head

        if temp == None:
            return count
        else:
            count += 1
            return self.size(count, temp.next)

    def index(self, item, temp = None, index=0):
        if temp == None:
            temp = self.head

        if temp.item == item:
            return index
        else:
            return self.index(item, temp.next, index + 1)

    def pop(self, pos = None, index = 0, temp = None):
        if temp == None:
            temp = self.head

        if pos == None or pos == self.size():
            out = self.tail
            self.tail = self.tail.prev
            return out.item
        else:
            if pos <= self.size()//2:
                if pos == index:
                    out = temp.item
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return out
                if pos != index and pos <= self.size()//2:
                    return self.pop(pos, index+1, temp.next)
                else:
                    return -1

            if pos > self.size()//2:
                index = self.size()
                if pos == index:
                    out = temp.item
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return out
                if pos != index and pos >= self.size()//2:
                    return self.pop(pos, index-1, temp.prev)
