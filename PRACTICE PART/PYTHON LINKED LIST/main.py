class node():
    def __init__(self, data):
        self.__data__ = data
        self.__next__ = None
    def getData(self):
        return self.__data__
    def getNext(self):
        return self.__next__
    def setNext(self, next):
        self.__next__ = next

class linkedList():
    def __init__(self):
        self.__head__ = None
    def addNode(self, node):
        if self.__head__ == None:
           self.__head__ = node
        else:
            temp = self.__head__
            while (temp.getNext() != None):
                temp = temp.getNext()
            temp.setNext(node)
    def print(self):
        temp = self.__head__
        while (temp.getNext() != None):
            print(temp.getData())
            temp = temp.getNext()
        print(temp.getData())
    def removeFirst(self):
        self.__head__ = self.__head__.getNext()
        
        
l = linkedList()
l.addNode(node(7))
l.addNode(node(17))
l.addNode(node(47))
l.removeFirst()
l.print()