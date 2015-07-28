__author__ = 'jonathanbrodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

'''
PUT
'''
def putEncode():
    msg=ClientMessage()
    msg.optype=0x0101
    util.raiseNotDefined()
def putDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GET
'''
def getEncode():
    msg=ClientMessage()
    msg.optype=0x0102
    util.raiseNotDefined()
def getDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVE
'''
def removeEncode():
    msg=ClientMessage()
    msg.optype=0x0103
    util.raiseNotDefined()
def removeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REPLACE
'''
def replaceEncode():
    msg=ClientMessage()
    msg.optype=0x0104
    util.raiseNotDefined()
def replaceDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REPLACEIFSAME
'''
def replaceifsameEncode():
    msg=ClientMessage()
    msg.optype=0x0105
    util.raiseNotDefined()
def replaceifsameDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUTASYNC
'''
def putasyncEncode():
    msg=ClientMessage()
    msg.optype=0x0106
    util.raiseNotDefined()
def putasyncDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETASYNC
'''
def getasyncEncode():
    msg=ClientMessage()
    msg.optype=0x0107
    util.raiseNotDefined()
def getasyncDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEASYNC
'''
def removeasyncEncode():
    msg=ClientMessage()
    msg.optype=0x0108
    util.raiseNotDefined()
def removeasyncDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CONTAINSKEY
'''
def containskeyEncode():
    msg=ClientMessage()
    msg.optype=0x0109
    util.raiseNotDefined()
def containskeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CONTAINSVALUE
'''
def containsvalueEncode():
    msg=ClientMessage()
    msg.optype=0x010a
    util.raiseNotDefined()
def containsvalueDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEIFSAME
'''
def removeifsameEncode():
    msg=ClientMessage()
    msg.optype=0x010b
    util.raiseNotDefined()
def removeifsameDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
DELETE
'''
def deleteEncode():
    msg=ClientMessage()
    msg.optype=0x010c
    util.raiseNotDefined()
def deleteDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
FLUSH
'''
def flushEncode():
    msg=ClientMessage()
    msg.optype=0x010d
    util.raiseNotDefined()
def flushDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
TRYREMOVE
'''
def tryremoveEncode():
    msg=ClientMessage()
    msg.optype=0x010e
    util.raiseNotDefined()
def tryremoveDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
TRYPUT
'''
def tryputEncode():
    msg=ClientMessage()
    msg.optype=0x010f
    util.raiseNotDefined()
def tryputDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUTTRANSIENT
'''
def puttransientEncode():
    msg=ClientMessage()
    msg.optype=0x0110
    util.raiseNotDefined()
def puttransientDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUTIFABSENT
'''
def putifabsentEncode():
    msg=ClientMessage()
    msg.optype=0x0111
    util.raiseNotDefined()
def putifabsentDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SET
'''
def setEncode():
    msg=ClientMessage()
    msg.optype=0x0112
    util.raiseNotDefined()
def setDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
LOCK
'''
def lockEncode():
    msg=ClientMessage()
    msg.optype=0x0113
    util.raiseNotDefined()
def lockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
TRYLOCK
'''
def trylockEncode():
    msg=ClientMessage()
    msg.optype=0x0114
    util.raiseNotDefined()
def trylockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ISLOCKED
'''
def islockedEncode():
    msg=ClientMessage()
    msg.optype=0x0115
    util.raiseNotDefined()
def islockedDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
UNLOCK
'''
def unlockEncode():
    msg=ClientMessage()
    msg.optype=0x0116
    util.raiseNotDefined()
def unlockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDINTERCEPTOR
'''
def addinterceptorEncode():
    msg=ClientMessage()
    msg.optype=0x0117
    util.raiseNotDefined()
def addinterceptorDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEINTERCEPTOR
'''
def removeinterceptorEncode():
    msg=ClientMessage()
    msg.optype=0x0118
    util.raiseNotDefined()
def removeinterceptorDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENERTOKEYWITHPREDICATE
'''
def addentrylistenertokeywithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x0119
    util.raiseNotDefined()
def addentrylistenertokeywithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENERWITHPREDICATE
'''
def addentrylistenerwithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x011a
    util.raiseNotDefined()
def addentrylistenerwithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENERTOKEY
'''
def addentrylistenertokeyEncode():
    msg=ClientMessage()
    msg.optype=0x011b
    util.raiseNotDefined()
def addentrylistenertokeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENER
'''
def addentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x011c
    util.raiseNotDefined()
def addentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDNEARCACHEENTRYLISTENER
'''
def addnearcacheentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x011d
    util.raiseNotDefined()
def addnearcacheentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEENTRYLISTENER
'''
def removeentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x011e
    util.raiseNotDefined()
def removeentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDPARTITIONLOSTLISTENER
'''
def addpartitionlostlistenerEncode():
    msg=ClientMessage()
    msg.optype=0x011f
    util.raiseNotDefined()
def addpartitionlostlistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEPARTITIONLOSTLISTENER
'''
def removepartitionlostlistenerEncode():
    msg=ClientMessage()
    msg.optype=0x0120
    util.raiseNotDefined()
def removepartitionlostlistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETENTRYVIEW
'''
def getentryviewEncode():
    msg=ClientMessage()
    msg.optype=0x0121
    util.raiseNotDefined()
def getentryviewDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
EVICT
'''
def evictEncode():
    msg=ClientMessage()
    msg.optype=0x0122
    util.raiseNotDefined()
def evictDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
EVICTALL
'''
def evictallEncode():
    msg=ClientMessage()
    msg.optype=0x0123
    util.raiseNotDefined()
def evictallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
LOADALL
'''
def loadallEncode():
    msg=ClientMessage()
    msg.optype=0x0124
    util.raiseNotDefined()
def loadallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
LOADGIVENKEYS
'''
def loadgivenkeysEncode():
    msg=ClientMessage()
    msg.optype=0x0125
    util.raiseNotDefined()
def loadgivenkeysDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
KEYSET
'''
def keysetEncode():
    msg=ClientMessage()
    msg.optype=0x0126
    util.raiseNotDefined()
def keysetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETALL
'''
def getallEncode():
    msg=ClientMessage()
    msg.optype=0x0127
    util.raiseNotDefined()
def getallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUES
'''
def valuesEncode():
    msg=ClientMessage()
    msg.optype=0x0128
    util.raiseNotDefined()
def valuesDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ENTRYSET
'''
def entrysetEncode():
    msg=ClientMessage()
    msg.optype=0x0129
    util.raiseNotDefined()
def entrysetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
KEYSETWITHPREDICATE
'''
def keysetwithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x012a
    util.raiseNotDefined()
def keysetwithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUESWITHPREDICATE
'''
def valueswithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x012b
    util.raiseNotDefined()
def valueswithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ENTRIESWITHPREDICATE
'''
def entrieswithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x012c
    util.raiseNotDefined()
def entrieswithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDINDEX
'''
def addindexEncode():
    msg=ClientMessage()
    msg.optype=0x012d
    util.raiseNotDefined()
def addindexDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIZE
'''
def sizeEncode():
    msg=ClientMessage()
    msg.optype=0x012e
    util.raiseNotDefined()
def sizeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ISEMPTY
'''
def isemptyEncode():
    msg=ClientMessage()
    msg.optype=0x012f
    util.raiseNotDefined()
def isemptyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUTALL
'''
def putallEncode():
    msg=ClientMessage()
    msg.optype=0x0130
    util.raiseNotDefined()
def putallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CLEAR
'''
def clearEncode():
    msg=ClientMessage()
    msg.optype=0x0131
    util.raiseNotDefined()
def clearDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
EXECUTEONKEY
'''
def executeonkeyEncode():
    msg=ClientMessage()
    msg.optype=0x0132
    util.raiseNotDefined()
def executeonkeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SUBMITTOKEY
'''
def submittokeyEncode():
    msg=ClientMessage()
    msg.optype=0x0133
    util.raiseNotDefined()
def submittokeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
EXECUTEONALLKEYS
'''
def executeonallkeysEncode():
    msg=ClientMessage()
    msg.optype=0x0134
    util.raiseNotDefined()
def executeonallkeysDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
EXECUTEWITHPREDICATE
'''
def executewithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x0135
    util.raiseNotDefined()
def executewithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
EXECUTEONKEYS
'''
def executeonkeysEncode():
    msg=ClientMessage()
    msg.optype=0x0136
    util.raiseNotDefined()
def executeonkeysDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
FORCEUNLOCK
'''
def forceunlockEncode():
    msg=ClientMessage()
    msg.optype=0x0137
    util.raiseNotDefined()
def forceunlockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
KEYSETWITHPAGINGPREDICATE
'''
def keysetwithpagingpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x0138
    util.raiseNotDefined()
def keysetwithpagingpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUESWITHPAGINGPREDICATE
'''
def valueswithpagingpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x0139
    util.raiseNotDefined()
def valueswithpagingpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ENTRIESWITHPAGINGPREDICATE
'''
def entrieswithpagingpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x013a
    util.raiseNotDefined()
def entrieswithpagingpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

