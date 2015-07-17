__author__ = 'jonathanbrodie'

from hzclient.connect import HazelcastConnection
from hzclient.hazelclient import HazelcastClient
def main():
    myClient=HazelcastClient()
    queue=myClient.getQueue("queue")
    print "Initial size of queue is: "+str(queue.size())
    print "Clearing the queue..."
    queue.clear()
    print "Finished clearing queue."
    print "Final size of queue is: "+str(queue.size())
    print "Finished printing size"
main()
