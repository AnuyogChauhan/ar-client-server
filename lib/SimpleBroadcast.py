
import socket

class SimpleBroadcast(object):
    def __init__(self, host1='localhost', port1=50041):
        self.host = host1
        self.port = port1
        self.conn = None
        
    def broadcast(self,value,connection=None):
        if connection is None and self.conn is None:
            s = socket.socket()
            s.connect((self.host, self.port))
            s.send('P')
            s.send(value)
            s.close
        elif self.conn is not None:
            self.conn.send('P')
            self.conn.send(value)
        elif connection != None:
            self.conn = connection
            self.conn.send('P')
            self.conn.send(value)
            
    def setConnection(self, connection):
        self.conn = connection
        
    def close(self):
        if self.conn is not None:
            self.conn.close
        
        
if __name__ == "__main__":
    sb = SimpleBroadcast(host1=socket.gethostname())
    sb.broadcast('10')
