__author__ = 'jonathanbrodie'
from connect import HazelcastConnection
from hzclient.clientmessage import QueueMessage
from hzclient.clientmessage import ClientMessage
from hzclient.clientmessage import PartitionMessage




class QueueProxy(object):
    def __init__(self,title,conn):
        self.title=title
        self.connection=conn
        queuemsg=QueueMessage()
        queuemsg.getQueue(self.title)
        self.connection.sendPackage(queuemsg.encodeMessage())
        response=self.connection.waitAndGetPackage()
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

    def put(self,item):
        queuemsg=QueueMessage.put(self.title,item)
        self.connection.sendPackage(queuemsg.encodeMessage())

    def size(self):
        '''
        part=PartitionMessage()
        self.connection.sendPackage(part.encodeMessage())
        response=self.connection.waitAndGetPackage()
        print "Size of Partition ID Response: "
        print len(response)
        print "Actual Partition ID Response: " + response
        '''

        queuemsg=QueueMessage()
        queuemsg.size(self.title)
        self.connection.sendPackage(queuemsg.encodeMessage())
        response=self.connection.waitAndGetPackage()
        responseMessage=ClientMessage.decodeMessage(response)
        size=responseMessage.extractIntFromPayload(4)
        return size

    def clear(self):

        queuemsg=QueueMessage()
        queuemsg.clear(self.title)
        self.connection.sendPackage(queuemsg.encodeMessage())
        response=self.connection.waitAndGetPackage()
        print "Size of server's response to clear: "+str(len(response))
        #no return from server

