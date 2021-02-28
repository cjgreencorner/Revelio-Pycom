from network import WLAN
import machine
import pycom
pycom.heartbeat(False)
wlan = WLAN(mode=WLAN.STA)

wlan.connect(ssid='telenet-82DF7B9', auth=(WLAN.WPA2, 'password'))
while not wlan.isconnected():
    machine.idle()
    pycom.rgbled(0xFF0000)

print("WiFi connected succesfully")
print(wlan.ifconfig())
pycom.rgbled(0x00FF00)
