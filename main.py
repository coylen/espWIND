import webrepl
import windcontroller
import network
from machine import Pin

# check to see if non boot switch is set
p = Pin(14, Pin.IN)
if (p.value() == 0 ):

    #wait until network is connected
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    while (not wlan.isconnected):
        pass

    webrepl.start()
    windcontroller.run(test=True)