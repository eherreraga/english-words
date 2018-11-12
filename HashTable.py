class HT():
    l = []
    tableSize = -1
    numItems = 0
    
    def __init__(self, size):
        self.l = [None] * size
        self.tableSize = size
    
    #The load factor is going to be the numberOfItems
    #table size
    def getLoadFactor(self):
        return self.numItems / self.tableSize

    #Its going to separate the word into characters and get the number that
    #its represents, then by using folding method we are going to
    #get a number that we are going to get the module by the table size
    def get_position(self, HTNode):
        n = 0
        l = list(HTNode.item)
        for c in l:
            n += ord(c)
        return n % self.tableSize

    #Inserting the word into the hashtable
    def insert(self, word):
        e = HTNode(word)
        pos = self.get_position(e)
        n = self.l[pos]
        if n is not None:
            e.next = n
        self.l[pos] = e
        self.numItems += 1

class HTNode():
    word = ""
    next = ""
    def __init__(self, word, next = None):
        self.word = word
        self.next = next