__author__ = 'jonathanbrodie'

class Employee(object):
    def __init__(self,name):
        self.name=name
        self.id=id
    def toBytes(self):
        return bytearray(self.name)