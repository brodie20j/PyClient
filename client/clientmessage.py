__author__ = 'Jonathan Brodie'


'''
Created on 6/24/15
ClientMessage Class, this is meant to duplicate the ClientMessage Java class as best
as I can to best ensure the protocol is followed
'''
import sys,struct,ctypes,uuid

class ClientMessage(object):
    def __init__(self):
        #initialize everything

        VERSION=0
        self.BEGIN_FLAG=0x80
        self.END_FLAG=0x40
        self.BEGIN_END_FLAG=self.BEGIN_FLAG | self.END_FLAG


        '''
        ***This could be constructed far more efficiently, but left in the form resembling that of ClientMessage.java
        -The first four bytes are the total size of the message
        -The next byte is the version
        -The next byte is the flag
        -The next two bytes are the message type
        -The next four bytes are the Correlation ID - unique to each message type
        -The next four bytes are the partition ID - -1 will put the ID into the default thread pool
        -The next two bytes define the offset from the start of the frame to the payload (Currently it is only 18 because
        the message header extension isn't used yet)
        -The rest of the message is the payload.
        '''

        FRAME_OFFSET=4
        VERSION_OFFSET=1 + FRAME_OFFSET
        FLAG_OFFSET=VERSION_OFFSET + 1
        TYPE_OFFSET=FLAG_OFFSET + 2
        CORRELATION_OFFSET=TYPE_OFFSET + 4
        PARTITION_OFFSET=CORRELATION_OFFSET+4
        self.DATA_OFFSET=PARTITION_OFFSET+2
        self.HEADER_SIZE=self.DATA_OFFSET

        self.FRAME_SIZE=self.HEADER_SIZE
        nativeOrder=sys.byteorder
        self.littleOrder='little'

        self.version=VERSION
        self.flag=self.BEGIN_END_FLAG
        self.optype=0
        self.correlation=213321
        self.partition=-1
        self.payload=None
        self.retryable=False

    '''
    Getters and setters.  Typically not used in Python but used here so a user knows what variables they should and
    shouldn't be messing with
    '''
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
        self.optype=newType
    def getOperationType(self):
        return self.optype
    def setPartition(self, newPartition):
        self.partition=newPartition
    def getPartition(self):
        return self.partition
    def setPayload(self,payload):
        self.payload=payload

    def encodeMessage(self):
        #since Python only uses ints and longs and does weird memory stuff, we need to wrap them here using the C types
        newVersion=ctypes.c_uint8(self.version)
        newFlag=ctypes.c_uint8(self.flag)
        newType=ctypes.c_uint16(self.optype)
        newCorrelation=ctypes.c_uint32(self.correlation)
        newPartition=ctypes.c_int32(self.partition)
        newOffset=ctypes.c_uint16(self.DATA_OFFSET)

        byteArray=bytearray(newVersion)+bytearray(newFlag)+bytearray(newType)+bytearray(newCorrelation)+bytearray(newPartition)+bytearray(newOffset)

        self.FRAME_SIZE=len(byteArray)+4
        if self.payload is None:
            newSize=ctypes.c_int32(self.FRAME_SIZE)
        else:
            #To-do: convert the payload to bytes properly here. In the meanwhile, the line below converts the payload to raw bytes
            newPayload=self.payload
            self.FRAME_SIZE=self.FRAME_SIZE+len(newPayload)
            newSize=ctypes.c_int32(self.FRAME_SIZE)
            byteArray=byteArray+newPayload
        byteArray=bytearray(newSize)+byteArray
        return byteArray

    @classmethod
    def decodeMessage(cls, bytesobject):
        headersize=int.from_bytes(bytesobject[:4],'little')
        bytesobject=bytesobject[4:]
        version=int.from_bytes(bytesobject[:1],'little')
        bytesobject=bytesobject[1:]
        flag=int.from_bytes(bytesobject[:1],'little')
        bytesobject=bytesobject[1:]
        type=int.from_bytes(bytesobject[:2],'little')
        bytesobject=bytesobject[2:]
        correlationID=int.from_bytes(bytesobject[:4],'little')
        bytesobject=bytesobject[4:]
        partitionID=int.from_bytes(bytesobject[:4],'little')
        bytesobject=bytesobject[4:]
        dataOffset=int.from_bytes(bytesobject[:2],'little')
        bytesobject=bytesobject[2:]
        return cls.constructMessageFrom(flag,version,type,correlationID,partitionID,dataOffset,bytesobject)

    @classmethod
    def constructMessageFrom(cls, flag,version,msgtype,corrID,pID,offset,payload):
        myMessage=cls()
        myMessage.flag=flag
        myMessage.version=version
        myMessage.optype=msgtype
        myMessage.correlation=corrID
        myMessage.partition=pID
        myMessage.DATA_OFFSET=offset
        myMessage.payload=payload
        print(myMessage.encodeMessage())
        print(len(myMessage.encodeMessage()))
        return myMessage