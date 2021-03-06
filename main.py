#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""
                Ultrasonic sensor
"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""
 For measuring distance between object and itself.
"""""""""""""""""""""""""""""""""""""""""""""""""""
#LIBRARIES
import network
from sensor import distance

#AUTHORINFO
_author_ = "Joel Chapon"
_email_  = "joel.chapon@student.kdg.be"
_status_ = "Finished"
_date_   = "2021-02-24"
wifi_ssid = "telenet-82DF7B9"
wifi_password = "YOUR_WIFI_PASSWORD"
aio_key = "aio_hMXe51B2PmapmKyp2yU1O2xhEMMP"
username = "cj_greencorner"
feed_name = "distance"


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_password)
while not sta_if.isconnected():
    print(".", end = "")

While True:
