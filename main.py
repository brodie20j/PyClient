__author__ = 'jonathanbrodie'
import sys
from employee import Employee
from hzclient.hazelclient import HazelcastClient
def main():
    client=HazelcastClient()
    myQueue=client.getQueue("queue")
    myQueue.put("item")
    print myQueue.size()
    sys.exit("Exiting")

if __name__ == '__main__':
    main()

