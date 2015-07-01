__author__ = 'jonathanbrodie'

from client.connect import HazelcastConnection
def main():
    con=HazelcastConnection()
    con.connectToCluster()
main()
