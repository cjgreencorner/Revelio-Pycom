#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""
      Sending an encrypted float via LoRaWan
"""""""""""""""""""""""""""""""""""""""""""""""""""


#AUTHORINFO
_author_ = "Joel Chapon"
_email_  = "joel.chapon@student.kdg.be"
_status_ = "Finished"
_date_   = "2021-03-06"


#IMPORTS
from network import LoRa
import socket
import time
import ubinascii
import ustruct

# Europe = LoRa.EU868

<<<<<<< HEAD

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
app_eui = ubinascii.unhexlify('70B3D57ED003E4D8')
app_key = ubinascii.unhexlify('92FC14552303B706EABEC67C263E8CE3')
=======
# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('?')
app_key = ubinascii.unhexlify('?')
#uncomment to use LoRaWAN application provided dev_eui
#dev_eui = ubinascii.unhexlify('70B3D549938EA1EE')

# Uncomment for US915 / AU915 & Pygate
# for i in range(0,8):
#     lora.remove_channel(i)
# for i in range(16,65):
#     lora.remove_channel(i)
# for i in range(66,72):
#     lora.remove_channel(i)

# join a network using OTAA (Over the Air Activation)
#uncomment below to use LoRaWAN application provided dev_eui
>>>>>>> 459f8fe9112011ad386238004d9e2553714d02aa
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
print('Joined')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# encode the packet, so that it's in BYTES (TTN friendly)
    # could be extended like this struct.pack('f',lipo_voltage) + struct.pack('c',"example text")

# change the float here
lipo_voltage = 18.89
packet = ustruct.pack('f',lipo_voltage)

# send the prepared packet via LoRa
s.send(packet)

# example of unpacking a payload - unpack returns a sequence of
#immutable objects (a list) and in this case the first object is the only object
print ("Unpacked value is:", ustruct.unpack('f',packet)[0])


# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

# get any data received (if any...)
data = s.recv(64)
print(data)
