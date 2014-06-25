from twisted.internet.protocol import DatagramProtocol
from twisted.internet.task import LoopingCall

import os
import json


class HeartbeatSender(DatagramProtocol):

    def __init__(self, file_path, host, port):
        self.file_path = file_path
        self.host = host
        self.port = port
    
    def startProtocol(self):

        self.transport.connect(self.host, self.port)
        print "Sending to host %s port %d" % (
            self.host, self.port)

        self.loopObj = LoopingCall(self.sendHeartBeat)
        self.loopObj.start(2, now=False)

    def datagramReceived(self, data, (host, port)):
        pass

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print "No one listening"

    def read_file(self, path):
        with open(path, 'r') as f:
            return f.read()
            
    def sendHeartBeat(self):
        files = []
        if os.path.isdir(self.file_path):
            files = os.listdir(self.file_path)

        result = {}
        for k in sorted(files):
            result[k] = self.read_file(os.path.join(self.file_path, k))
        
        self.transport.write(json.dumps(result), (self.host, self.port))