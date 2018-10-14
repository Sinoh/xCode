# Name: Jeffery Ho
# Section: 202 - 11

import operator
import re

# A HashTableLinPr is a class
# A capacity is a number
# A table is a list
# A num_items is a number
# A table_size is a number
class HashTableLinPr:
    def __init__(self, table_size=251):
        self.table = [[] for i in range(table_size)]
        self.table_size = table_size
        self.num_items = 0

    def __repr__(self):
        return ("HashTable({!r})".format(self.table))

    def __eq__(self, other):
        if isinstance(other, HashTableLinPr):
            return self.table== other.table and self.table_size == other.table_size and self.num_items == other.num_items
        else:
            return False

    # A read_stop is a list
    # string -> list
    # Takes in a string as the file name of a file that contains a list of stop words and creates a hash table of them
    def read_stop(self, filename):
        input = open(filename, 'r')
        for line in input:
            self.insert(line, self.table_size)

        input.close()

    # A read_file is a None
    # String list -> None
    # Takes in a string as a file name that contains sentences and a stop table
    # Creates a hash_table with all the words excluding the ones in the stop_table
    def read_file(self, filename, stop_table):
        input = open(filename, 'r')

        i = 1
        for line in input:
            line = re.sub("[']", '', line)
            line = re.sub("[\d]",' ', line)
            line = re.sub("[\W]",' ', line).split()

            for word in line:
                in_list = False
                for list in stop_table.table:

                    if str(word) in list:
                        in_list = True
                if in_list == False:
                    self.insert(word, self.table_size, i)

            i += 1
        input.close()

    # A get_tablesize is a number
    # None -> int
    # Take in no paramters and returns the number of key-items pairs currently in the table
    def get_tablesize(self):
        return self.num_items

    # A save_concordance is a None
    # String -> None
    # Takes a string as an output name
    # And writes each word and which line it occurs in in the output file
    def save_concordance(self, output_filename):
        output = open(output_filename, 'w')

        table = []
        for list in self.table:
            if list != []:
                table.append(list)

        table.sort(key = operator.itemgetter(0))
        int = 0
        for tuple in table:
            for word in tuple:
                if int != len(table) - 1:
                    output.write('{}:\t{}\r\n'.format(word[0].lower(), word[1]))
                    int += 1
                else:
                    output.write('{}:\t{}'.format(word[0].lower(), word[1]))

        output.close()
    # A get_load_fact is a number
    # None -> int
    # Take in no paramters and returns the load factor of the current table
    def get_load_fact(self):
        return float(self.num_items) / float(self.table_size)

    # A myhash is a nuber
    # string int -> int
    # Takes in a key and the size of the table
    # And returns the hash value
    def myhash(self, key, table_size):
        if len(key) > 8:
            n = 8
        else:
            n = len(key)

        value = 0
        i = 0

        for letter in key:
            value += ord(str(letter)) * (31**(n-1-i))
            i += 1
        return int(value % self.table_size)


    # A insert is a None
    # string int -> None
    # Takes in a string and a table size and inputs it into a hash table
    # Checks if the load factor is greater than .75 and if it is true
    # Doubles the size and add 1
    # Then rehash the table
    def insert(self, line, table_size, occur = None):
        line = line.rstrip('\n\r')
        hash = self.myhash(line, table_size)
        while self.table[hash] != []:
            hash += 1
            if hash == self.table_size:
                hash = 0

        if occur == None:
            self.table[hash].append(line)
        else:
            self.table[hash].append((line , occur))

        self.num_items += 1

        if self.get_load_fact() > .75:
            temp = HashTableLinPr(2 * self.table_size + 1)
            for i in range(self.table_size):
                if self.table[i] != []:
                    if occur == None:
                        remkey = self.table[i][0]
                        temp.insert(remkey, temp.table_size)
                    else:
                        remkey = self.table[i][0][0]
                        remitem = self.table[i][0][1]
                        temp.insert(remkey, remitem, temp.table_size)

            self.table = temp.table
            self.table_size = temp.table_size


