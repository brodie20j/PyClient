__author__ = 'jonathanbrodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
'''
PUBLISH
'''
def publishEncode():
    msg=ClientMessage()
    msg.optype=0x0401
    util.raiseNotDefined()
def publishDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDMESSAGELISTENER
'''
def addmessagelistenerEncode():
    msg=ClientMessage()
    msg.optype=0x0402
    util.raiseNotDefined()
def addmessagelistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEMESSAGELISTENER
'''
def removemessagelistenerEncode():
    msg=ClientMessage()
    msg.optype=0x0403
    util.raiseNotDefined()
def removemessagelistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

