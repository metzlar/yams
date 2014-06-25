from twisted.internet.protocol import DatagramProtocol

import yams.store
import json
import time


YAMS = [{}, time.time()]


class HeartbeatReceiver(DatagramProtocol):

    def __init__(self, key):
        self.key = key
        yams.store.delete(self.key)
    
    def datagramReceived(self, data, (host, port)):
        stamp = time.time()

        try:
            data = json.loads(data)
        except Exception,e:
            print e

        data_stamped = {}
        for k,v in data.iteritems():
            data_stamped[k] = [v, stamp]

        YAMS[0].update({'%s:%d'%(host, port):data_stamped})
        YAMS[1] = stamp

        yams.store.set(self.key, json.dumps(YAMS))
        
        #self.transport.write(data, (host, port))