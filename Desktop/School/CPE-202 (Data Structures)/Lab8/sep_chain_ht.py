# Name: Jeffery Ho
# Section: 202 - 11

# A MyHashTable is a class
# A capacity is a number
# A table is a list
# A num_items is a number
# A num_collisions is a number
class MyHashTable:
    def __init__(self, table_size=11):
        self.table = [[] for i in range(table_size)]
        self.capacity = table_size
        self.num_items = 0
        self.num_collisions = 0

    def __repr__(self):
        return ("HashTable({!r})".format(self.table))

    def __eq__(self, other):
        if isinstance(other, MyHashTable):
            return self.table== other.table and self.capacity == other.capacity and self.num_items == other.num_items and self.num_collisions == other.num_collisions
        else:
            return False

    # A insert is a None
    # int object -> None
    # Takes in a key and and item and inputs it into a list as a tuple
    # Will take the key and create a hash by modding the key by the table size
    # Then insert the tuple into the position of the hash
    # If there are duplicate keys, the old key-item pair will be replaced by the new key-item pair
    # If the load factor is greater than 1.5, the table capacity will be increased two times plus one
    # And all the items will then be inserted into the new has table
    def insert(self, key, item):
        hash_value = key % self.capacity
        if self.table[hash_value] != []:
            self.num_collisions += 1
            for keys in self.table[hash_value]:
                if keys[0] == key:
                    self.remove(key)
        self.table[hash_value].append((key,item))
        self.num_items += 1

        if self.load_factor() > 1.5:
            temp = MyHashTable(2 * self.capacity + 1)
            temp.num_collisions = self.num_collisions
            for i in range(self.capacity):
                if self.table[i] != []:
                    for k in range(len(self.table[i])):
                        remkey = self.table[i][k][0]
                        remitem = self.table[i][k][1]
                        temp.insert(remkey, remitem)

            self.table = temp.table
            self.capacity = temp.capacity
            self.num_collisions = temp.num_collisions

    # A get is a tuple or Error
    # int object -> tuple
    # Takes in a key and and item and returns a tuple if key was found in table
    # Else return LookupError
    def get(self, key):
        hash_value = key % self.capacity
        for keys in self.table[hash_value]:
            if keys[0] == key:
                return keys
        raise LookupError


    # A remove is a tuple or Error
    # int -> tuple
    # Takes in a key and returns a tuple if key was found in table
    # Also deletes the tuple found
    # Else return LookupError
    def remove(self, key):
        hash_value = key % self.capacity
        for index in range(len(self.table[hash_value])):
            if self.table[hash_value][index][0] == key:
                keys = self.table[hash_value][index]
                self.table[hash_value].remove((key, keys[1]))
                self.num_items -= 1
                return keys
        raise LookupError

    # A size is a number
    # None -> int
    # Take in no paramters and returns the number of key-items pairs currently in the table
    def size(self):
        return self.num_items

    # A load_factor is a number
    # None -> int
    # Take in no paramters and returns the load factor of the current table
    def load_factor(self):
        return float(self.num_items) / float(self.capacity)

    # A size is a number
    # None -> int
    # Take in no paramters and returns the number the number of collisions that has occurred in this table
    def collisions(self):
        return self.num_collisions
