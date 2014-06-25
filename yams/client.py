
from twisted.internet.protocol import DatagramProtocol
from twisted.internet.task import LoopingCall

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

    def sendHeartBeat(self):
        with open(self.file_path, 'r') as f:
            self.transport.write(f.read(), (self.host, self.port))