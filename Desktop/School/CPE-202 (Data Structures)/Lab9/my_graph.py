# Name: Jeffery Ho
# Section: 202 - 11

# MyGraph is a class
# a file is a string
# a vertlist is a dictionary
class MyGraph:
    def __init__(self, filename = None):
        self.file = filename
        self.vertlist = {}

    def __repr__(self):
         return ("Vertlist({!r})".format(self.vertlist))

    def __eq__(self, other):
        if isinstance(other, MyGraph):
            return self.file == other.file and self.vertlist == other.vertlist and self.num_vert == other.num_vert and self.num_edge == other.num_edge
        else:
            return False

    # A add_vertex is a  None
    # Int -> None:
    # Takes in a key as an int and creates a new dictionary entry of a vertex with the key as the id
    def add_vertex(self, key):
        newVertex = Vertex(key)
        self.vertlist[key] = newVertex

    # A con_components is a list
    # None -> List
    # Takes in no paramteres and returns a list of sub_list of all components
    # It will open an input file and create vertexes from the lines of connections
    # Then connected each vertex with other vertex according to the file
    # Then create sub list of all the connections each vertex have
    # Concatenates the lists with at least one duplicated item with both list
    # Delete duplicate list
    # Sorts the list in ascending order
    # Returns list
    def conn_components(self):
        input = open(self.file, 'r')

        result = []
        i = 0
        for line in input:
            if i == 0:
                self.num_vert = line
                for index in range(1,int(line) + 1):
                    self.add_vertex(index)
                i += 1
                print(self.vertlist)
            elif i == 1:
                self.num_edge = line
                i += 1
            else:
                self.vertlist[int(line[0])].addConnection(self.vertlist[int(line[2])])

        for vertex in self.vertlist:
            sub = []
            sub.append(int(vertex))
            print('1', self.vertlist[vertex].return_connections())
            sub += self.vertlist[vertex].return_connections()
            result.append(sub)

        for index in range(len(result)):
            for index in range(len(result)):
                i = index + 1
                while i < len(result):
                    for number in result[index]:
                        if number in result[i]:
                            result[index] += result[i]
                            result[i] = []
                    i += 1

        result = [x for x in result if x != []]

        for index in range(len(result)):
            result[index] = list(set(result[index]))

        for sub_list in result:
            sub_list.sort()

        return result

# A vertex is a class
# A id is a string
# A connctedTo is a dictionary
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def __repr__(self):
         return ('Key: %s' % (self.id))

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.id == other.id and self.connectedTo == other.connectedTo
        else:
            return False

    # A addConnection is a None
    # Class -> None
    # Takes in a vertex class and updates the current vertex's connectedTo and the second vertex's connectedTo
    def addConnection(self,other,weight=0):
        self.connectedTo['%s' % (other.id)] = weight
        other.connectedTo['%s' % (self.id)] = weight


    # A return_connections is a list
    # None -> List
    # Takes in no parameters and returns a list of all the connections this vertex has
    def return_connections(self):
        list = []
        for vertex in self.connectedTo:
            list.append(int(vertex))

        return list






