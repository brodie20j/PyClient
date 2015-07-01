__author__ = 'Jonathan Brodie'
'''
Created on 6/24/15
ClientMessage Class, this is meant to duplicate the ClientMessage Java class as best
as I can to best ensure the protocol is followed
'''
import sys,struct,ctypes

class ClientMessage:
    def __init__(self):
        #initialize everything

        VERSION=0
        BEGIN_FLAG=0x80
        END_FLAG=0x40
        BEGIN_END_FLAG=BEGIN_FLAG | END_FLAG

        FRAME_OFFSET=4 #this is trivial but it's in the Java code
        VERSION_OFFSET=1 + FRAME_OFFSET
        FLAG_OFFSET=VERSION_OFFSET + 1
        TYPE_OFFSET=FLAG_OFFSET + 2
        CORRELATION_OFFSET=TYPE_OFFSET + 4
        PARTITION_OFFSET=CORRELATION_OFFSET+4
        self.DATA_OFFSET=PARTITION_OFFSET+2
        self.HEADER_SIZE=self.DATA_OFFSET

        self.FRAME_SIZE=self.HEADER_SIZE
        nativeOrder=sys.byteorder
        littleOrder='little'

        self.version=VERSION
        self.flag=BEGIN_END_FLAG
        self.optype=0
        self.correlation=0
        self.partition=-1
        self.type=0
        self.payload=None
        self.retryable=False


    def setVersion(self, vr):
        self.version=vr
    def getVersion(self):
        return self.version
    def setFlagBegin(self):
        self.flag=self.BEGIN_FLAG
    def setFlagEnd(self):
        self.flag=self.END_FLAG
    def setFlagBoth(self):
        self.flag=self.BEGIN_END_FLAG
    def setOperationType(self, newType):
        self.type=newType
    def getOperationType(self):
        return self.type
    def setPartition(self, newPartition):
        self.partition=newPartition
    def getPartition(self):
        return self.partition
    def setPayload(self,payload):
        self.payload=payload

    def setAuthentication(self):
        self.type=0x2
        self.payload=self.getAuthenticationPayload()

    def getAuthenticationPayload(self):
        myArray=[]
        myArray.append("dev")
        myArray.append("dev-password")
        myArray.append(False)
        myArray.append(False)
        myArray.append(False)

        return myArray



    def fixByteOrder(self, byteConfig):
        if self.nativeOrder != self.littleOrder:
            littleEndian="<"
            #THIS IS BROKEN DON'T TRY IT YET!!! YOU NEED TO SPECIFY THE FORMAT PER DATA TYPE!
            newOrder=struct.unpack(littleEndian,byteConfig)
            byteConfig=newOrder
        return byteConfig

    def getPackageForm(self):

        #since Python only uses ints and longs and does weird memory stuff, we need to wrap them here
        newVersion=ctypes.c_uint8(self.version)
        newFlag=ctypes.c_uint8(self.flag)
        newType=ctypes.c_uint16(self.optype)
        newCorrelation=ctypes.c_uint32(self.correlation)
        newPartition=ctypes.c_int32(self.partition)
        newOffset=ctypes.c_uint16(self.DATA_OFFSET)
        print(self.DATA_OFFSET)

        byteArray=bytearray(newVersion)+bytearray(newFlag)+bytearray(newType)+bytearray(newCorrelation)+bytearray(newPartition)+bytearray(newOffset)

        self.FRAME_SIZE=len(byteArray)+4
        if self.payload is None:
            newSize=ctypes.c_int32(self.FRAME_SIZE)
        else:

            #To-do: convert the payload to bytes properly here. In the meanwhile, the line below converts the payload to raw bytes
            newPayload=self.processPayload(self.payload)
            self.FRAME_SIZE=self.FRAME_SIZE+len(newPayload)
            newSize=ctypes.c_int32(self.FRAME_SIZE)
            print(newPayload)
            byteArray=byteArray+newPayload

        byteArray=bytearray(newSize)+byteArray
        return byteArray


    def processPayload(self,payArray):
        newArray=[]
        for i in payArray:
            print(i)
            if isinstance(i,str):
                i=i.encode("utf-8")
            print(bytearray(i))
            newArray+=bytearray(i)
        return newArray

