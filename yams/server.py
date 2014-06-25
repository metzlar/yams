from twisted.internet.protocol import DatagramProtocol

import yams.store
import json


YAMS = {}


class HeartbeatReceiver(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        print "received %r from %s:%d" % (data, host, port)

        try:
            data = json.loads(data)
        except Exception,e:
            print e
        
        YAMS.update({host:data})
        yams.store.set('YAMS', json.dumps(YAMS))
        
        #self.transport.write(data, (host, port))