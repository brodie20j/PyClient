__author__ = 'Jonathan Brodie'


from hzclient.connect import HazelcastConnection
from hzclient.proxy import ALongProxy
from hzclient.connectmanager import ConnectionManager
from hzclient.clientmessage import ClientMessage
class HazelcastClient(object):
    def __init__(self):
        self.connection=ConnectionManager()

    def getAtomicLong(self,title):
        mylong=ALongProxy(title,self.connection)
        return mylong

    def step(self):
        print "TO BE IMPLEMENTED"
