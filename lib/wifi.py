from network import WLAN
import machine
import pycom


def connect():
    pycom.heartbeat(False)
    wlan = WLAN(mode=WLAN.STA)

    wlan.connect(ssid='telenet-82DF7B9', auth=(WLAN.WPA2, 'Password'))
    while not wlan.isconnected():
        machine.idle()
        pycom.rgbled(0xFF0000)

    print("WiFi connected succesfully")
    print(wlan.ifconfig())