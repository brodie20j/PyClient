__author__ = 'jonathanbrodie'
import ctypes
from hzclient.clientmessage import ClientMessage


def putEncode(title,item):
    msg=ClientMessage()
    msg.optype=0x0302
    msg.correlation=101
    msg.partition=1
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle+bytearray(ctypes.c_uint32(len(item)))+item
    msg.setPayload(payload)
    return msg

def putDecode(rawBytes):
    servermsg=ClientMessage.decodeMessage(rawBytes)
    return None
def sizeEncode(title):
    msg=ClientMessage()
    msg.optype=0x0303
    msg.partition=1
    msg.setCorrelation(102)
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_int32(len(newtitle)))+newtitle
    msg.setPayload(payload)
    return msg

def sizeDecode(rawBytes):
    servermsg=ClientMessage.decodeMessage(rawBytes)
    return servermsg.extractIntFromPayload()

def clearEncode(title):
    msg.optype=0x030F
    msg.setCorrelation(122)
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_int32(len(newtitle)))+newtitle
    msg.setPayload(payload)
    return msg

def clearDecode(rawBytes):
    servermsg=ClientMessage.decodeMessage(rawBytes)
    return None #no return from payload