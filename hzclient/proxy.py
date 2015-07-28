__author__ = 'jonathanbrodie'
from connect import HazelcastConnection
from hzclient.clientmessage import QueueMessage
from hzclient.clientmessage import ClientMessage
from hzclient.clientmessage import PartitionMessage
from hzclient.codec import alongcodec
from hzclient.codec import queuecodec
from hzclient.codec import proxycodec



class ALongProxy(object):
    def __init__(self,title,conn):
        self.title=title
        self.connection=conn
        firstpack=proxycodec.createProxy(self.title,"hz:impl:atomicLongService")
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

    def getAndIncrement(self):
        pack=alongcodec.getandincrementEncode(self.title)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.getandincrementDecode(response)
        return decoded

    def get(self):
        pack=alongcodec.getEncode(self.title)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.getDecode(response)
        return decoded

    def addAndGet(self,delta):
        pack=alongcodec.addandgetEncode(self.title,delta)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.addandgetDecode(response)
        return decoded

    def compareAndSet(self,expected,updated):
        pack=alongcodec.compareandsetEncode(self.title,expected,updated)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.compareandsetDecode(response)
        return decoded

    def getAndAdd(self,delta):
        pack=alongcodec.getandaddEncode(self.title, delta)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.getandaddDecode(response)
        return decoded

    def getAndSet(self,new):
        pack=alongcodec.getandsetEncode(self.title,new)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.getandsetDecode(response)
        return decoded

    def incrementAndGet(self):
        pack=alongcodec.incrementandgetEncode(self.title)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.incrementandgetDecode(response)
        return decoded

    def set(self,new):
        pack=alongcodec.setEncode(self.title,new)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.setDecode(response)
        return decoded


class QueueProxy(object):
    def __init__(self,title,conn):
        self.title=title
        self.connection=conn
        firstpack=proxycodec.createProxy(self.title,"hz:impl:queueService")
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

    def put(self,item):

        #serialization of item here
        queuemsg=queuecodec.putEncode(self.title,item)
        self.connection.sendPackage(queuemsg.encodeMessage())
        response=self.connection.waitAndGetPackage()


    def size(self):
        '''
        part=PartitionMessage()
        self.connection.sendPackage(part.encodeMessage())
        response=self.connection.waitAndGetPackage()
        print "Size of Partition ID Response: "
        print len(response)
        print "Actual Partition ID Response: " + response
        '''
        pack=queuecodec.sizeEncode(self.title)
        self.connection.sendPackage(pack.encodeMessage())

        response=self.connection.waitAndGetPackage()
        responseMessage=queuecodec.sizeDecode(response)
        size=responseMessage
        return size

    def clear(self):

        queuemsg=QueueMessage()
        queuemsg.clear(self.title)
        self.connection.sendPackage(queuemsg.encodeMessage())
        response=self.connection.waitAndGetPackage()
        print "Size of server's response to clear: "+str(len(response))
        #no return from server

class SetProxy(object):
    def __init__(self,title,conn):
        self.title=title
        self.connection=conn
        firstpack=proxycodec.createProxy(self.title,"hz:impl:setService")
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

class ListProxy(object):
    def __init__(self,title,conn):
        self.title=title
        self.connection=conn
        firstpack=proxycodec.createProxy(self.title,"hz:impl:setService")
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."