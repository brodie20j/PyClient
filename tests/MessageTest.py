__author__ = 'jonathanbrodie'

import unittest
from client.clientmessage import ClientMessage

class ClientMessageTests(unittest.TestCase):

    def testHeaderNormal(self):
        msg=ClientMessage()
        self.assertEqual(len(msg.getPackageForm()),msg.FRAME_SIZE)

    def testPayload(self):
        msg=ClientMessage()
        #msg.setPayload("sadsaklasdkljjkldas".encode())
        self.assertEqual(len(msg.getPackageForm()),msg.FRAME_SIZE)

    def testAuthorization(self):
        msg=ClientMessage()
        msg.setAuthentication()
        self.assertEqual(len(msg.getPackageForm()),msg.FRAME_SIZE)



if __name__ == '__main__':
    unittest.main()

