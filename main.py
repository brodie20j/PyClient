__author__ = 'Jonathan Brodie'
import sys
from employee import Employee
from hzclient.hazelclient import HazelcastClient
def main():
    client=HazelcastClient()
    along=client.getAtomicLong("along")
    i=along.getAndIncrement()
    print i == along.get()
if __name__ == '__main__':
    main()

