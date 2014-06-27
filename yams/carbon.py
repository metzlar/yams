import socket


class Carbon(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def create_message(self, client_name, data):
        client_name = client_name.replace('.', '_')
        lines = []
        for k, (v, stamp) in data.iteritems():
            line = 'yams.%s.%s %s %d\n' % (
                client_name,
                k,
                v,
                int(stamp)
            )
            lines.append(line)

        return ''.join(lines)
        
    def send(self, client_name, data):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, int(self.port)))
        
        message = self.create_message(client_name, data)

        s.sendall(message)
        s.shutdown(socket.SHUT_WR)
        while 1:
            data = s.recv(1024)
            if data == "":
                break
        s.close()