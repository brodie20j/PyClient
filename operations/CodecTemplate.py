__author__ = 'jonathanbrodie'

from hzclient.clientmessage import ClientMessage

class CodecTemplate(object):
    def __init__(self):
        self.requesttype=0
        self.responsetype=0
        self.RETRYABLE=True


    class RequestParameters(object):
        def __init__(self):
            print "foo"
            #initialize vars here
        def calculateDataSize(self):
            return ClientMessage().HEADER_SIZE

    def encodeRequest(self):
        msg=ClientMessage()
        msg.setOperationType(self.requesttype)

        #do anything else here
        return msg

    def decodeRequest(self, clientmessage):
        params=self.RequestParameters()
        return params


    class ResponseParameters(object):
        def __init__(self):
            print "foo"
            #initialize vars here
        def calculateDataSize(self):
            return ClientMessage().HEADER_SIZE

    def encodeResponse(self):
        msg=ClientMessage()
        msg.setOperationType(self.responsetype)

        #do anything else here
        return msg

    def decodeResponse(self, clientmessage):
        params=self.ResponseParameters()
        return params