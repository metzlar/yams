from twisted.internet.protocol import DatagramProtocol

import yams.carbon
import yams.store
import json
import time


YAMS = [{}, time.time()]


class HeartbeatReceiver(DatagramProtocol):

    def __init__(self, key, carbon_host=None, carbon_port=None):
        self.carbon = None
        if (not carbon_host is None) and (not carbon_port is None):
            self.carbon = yams.carbon.Carbon(
                carbon_host, carbon_port)
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

        client_name = '%s' % host

        YAMS[0].update({client_name:data_stamped})
        YAMS[1] = stamp

        yams.store.set(self.key, json.dumps(YAMS))

        self.carbon.send(client_name, data_stamped)
        
        #self.transport.write(data, (host, port))