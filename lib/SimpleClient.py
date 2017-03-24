
import socket
from time import time


class ClientDisconnectedException(Exception):
    pass

class SimpleClient(object):
    def __init__(self, host1='localhost', port1=50041):
        self.host = host1
        self.port = port1
        self.lastMessageTimes = list()
        self.warningTime = 0.001
        self.conn = None


    def subscribe(self, connection=None):
        if connection is None and self.conn is None:
            self.conn = socket.socket()
            self.conn.connect((self.host, self.port))
        elif self.conn is None:
            self.conn = connection
        self.conn.send('C')
        while True:
            value1 = self.conn.recv(10)
            self.lastMessageTimes.append(time())
            if(len(self.lastMessageTimes) > 10):
                if(time() - self.lastMessageTimes[0] < self.warningTime):
                    raise ClientDisconnectedException()
                self.lastMessageTimes.pop(0)

            self.useValue(value1)
        self.s.close
            
    def setConnection(self, connection):
        self.conn = connection

    """
        used for test cases
    """
    def getOne(self,connection = None):
        if connection is None:
            self.conn = socket.socket()
            self.conn.connect((self.host, self.port))
        else:
            self.conn = connection
        self.conn.send('C')
        return self.conn.recv(10)

    def useValue(self, value):
        print value

if __name__ == "__main__":
    sc = SimpleClient(host1=socket.gethostname())
    sc.subscribe()
