__author__ = 'jonathanbrodie'


from hzclient.connect import HazelcastConnection
class HazelcastClient(object):
    def __init__(self):
        self.connection=HazelcastConnection()
        self.setupConnection()


    def setupConnection(self):
        while self.connection.initial is False:
            self.connection.connectToCluster()
            self.connection.authenticateConnection()
