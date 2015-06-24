__author__ = 'jonathanbrodie'

'''
Basic connection class that will connect to a Hazelcast client

'''


import socket

class HazelcastConnection:

    def __init__(self):
        #initialize a default local connection, the user can change these using the below methods
        self.TCP_IP='127.0.0.1'
        self.TCP_PORT=5701
        self.connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.initial=False

    def setIPAddress(self, newIP):
        self.TCP_IP=newIP

    def setPortNumber(self, newPort):
        self.TCP_PORT=newPort

    def connectToCluster(self):
        try:
            self.connection.connect((self.TCP_IP,self.TCP_PORT))
            self.authenticateConnection()
        except Exception as e:
            print("There was an error connecting to the server!")
            print(e)

    def authenticateConnection(self):
        #only run the three bytes at the beginning during the client-server dialog
        if self.initial:
            return
        else:
            firstpackage=bytearray([0x43, 0x42, 0x32])
            self.sendPackage(firstpackage)
            self.initial=True


    def sendPackage(self, package):
        #do actual protocol stuff here
        totalsent=0
        while totalsent < len(package):
            sent=self.connection.send(package)
            if sent == 0:
                raise RuntimeError("Connection broken")
            totalsent=totalsent+sent
