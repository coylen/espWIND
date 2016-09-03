#main control program

from NasaWind import NASAWind
from time import sleep
import machine

def connect():
    import socket
    s = socket.socket()
    s.connect(('192.168.0.10',10110)) #check address
    return s

def run(test=False):
    nw = NASAWind()
    while True:
        try:
            nw.update()
            s = connect()
            if test:
                print(nw.output)
            s.send(nw.output)
            nw.output = []
        except:
            if nw.fail > 10:
                machine.reset()
            pass
        finally:
            s.close()
        sleep(1)








