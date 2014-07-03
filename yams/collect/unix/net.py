from yams.collect import BaseCollector

import netstat


class NetworkCollector(BaseCollector):

    def __init__(self, *args, **kwargs):
        super(NetworkCollector, self).__init__(*args, **kwargs)

        self.net_lines = netstat.netstat()
        

    def tcp_listening(self, proc, port, property_name = None):
        if type(port) != list:
            port = [port]

        port = [str(p) for p in port]
            
        if property_name is None:
            property_name = '%s_on_%s' % (proc, '_'.join(port))
            
        def _f(pname, pc, pt, lines):
            result = 0
            for line in lines:
                for p in pt:
                    # [tcp_id, uid, l_host, r_host, state, pid, exe]
                    if all([
                        pc in str(line[6]),
                        line[2].endswith(':'+str(p)),
                        line[4] == 'LISTEN',
                    ]):
                        result += 1

            self.write(pname, result)

        self.schedule(_f, property_name, proc, port, self.net_lines)










