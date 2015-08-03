__author__ = 'Jonathan Brodie'

class Employee(object):
    def __init__(self,name):
        self.name=name
        self.id=id
    def toBytes(self):
        return bytearray(self.name)