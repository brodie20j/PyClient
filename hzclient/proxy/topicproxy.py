__author__ = 'jonathanbrodie'
from hzclient.codec import proxycodec
from hzclient.codec import topiccodec
from hzclient.clientmessage import ClientMessage



class TopicProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title,"hz:impl:topicService")
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

    def publish(self,data):
        msg=topiccodec.TopicPublishCodec.encodeRequest(self.title,data)
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.waitAndGetPackage()
        msg2=ClientMessage.decodeMessage(response)

        return topiccodec.TopicPublishCodec.decodeResponse(msg2)

    def addMessageListener(self):
        msg=topiccodec.TopicAddMessageListenerCodec.encodeRequest(self.title)

        self.connection.sendPackage(msg.encodeMessage())
        #something in here about entry listeners
        response=self.connection.waitAndGetPackage()
        msg2=ClientMessage.decodeMessage(response)

        return topiccodec.TopicAddMessageListenerCodec.decodeResponse(msg2)

    def removeMessageListener(self):
        msg=topiccodec.TopicRemoveMessageListenerCodec.encodeRequest(self.title, registrationId)
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.waitAndGetPackage()
        msg2=ClientMessage.decodeMessage(response)

        return topiccodec.TopicRemoveMessageListenerCodec.decodeResponse(msg2)