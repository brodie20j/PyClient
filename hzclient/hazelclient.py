__author__ = 'jonathanbrodie'


from hzclient.connect import HazelcastConnection
from hzclient.proxy import QueueProxy
from hzclient.proxy import ALongProxy

from hzclient.clientmessage import ClientMessage
from hzclient.clientmessage import QueueMessage
class HazelcastClient(object):
    def __init__(self):
        self.connection=HazelcastConnection()
        self.setupConnection()


    def setupConnection(self):
        while self.connection.initial is False:
            self.connection.connectToCluster()
            self.connection.authenticateConnection()

    def getQueue(self,title):

        myQueue=QueueProxy(title,self.connection)
        return myQueue

    def getAtomicLong(self,title):
        mylong=ALongProxy(title,self.connection)
        return mylong

    def step(self):
        print "TO BE IMPLEMENTED"
