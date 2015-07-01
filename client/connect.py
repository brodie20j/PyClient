__author__ = 'jonathanbrodie'

'''
Basic connection class that will connect to a Hazelcast Cluster

'''


import socket
from client.clientmessage import ClientMessage
class HazelcastConnection:

    def __init__(self):
        #initialize a default local connection, the user can change these using the below methods
        self.TCP_IP='127.0.0.1'
        self.TCP_PORT=5701
        self.connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.initial=False
        self.connectConstant="CB2"
        self.clientType="PHY" #Python client authorization

    def setIPAddress(self, newIP):
        self.TCP_IP=newIP

    def setPortNumber(self, newPort):
        self.TCP_PORT=newPort

    def connectToCluster(self):
        try:
            self.connection.connect((self.TCP_IP,self.TCP_PORT))
            self.initializeConnection()
        except Exception as e:
            print("There was an error connecting to the server!")
            print(e)

    def initializeConnection(self):
        #only run the six bytes at the beginning during the client-server dialog
        if self.initial:
            return
        else:
            firstpackage=ClientMessage()
            string=(self.connectConstant+self.clientType).encode()
            self.sendPackage(string)
            string="thank god".encode()
            firstpackage.setPayload(string)
            self.sendPackage(firstpackage.getPackageForm())

            print("Trying to receive response")
            data=self.connection.recv(1024)
            print(data)
            self.initial=True


    def sendPackage(self, package):
        #do actual protocol stuff here
        totalsent=0
        while totalsent < len(package):
            print("sending package...")
            sent=self.connection.send(package)
            if sent == 0:
                raise RuntimeError("Connection broken")
            totalsent=totalsent+sent

    def closeConnection(self):
        self.connection.close()


