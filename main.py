#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""
                Ultrasonic sensor
"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""
 For measuring distance between object and itself.
"""""""""""""""""""""""""""""""""""""""""""""""""""


#AUTHORINFO
_author_ = "Joel Chapon"
_email_  = "joel.chapon@student.kdg.be"
_status_ = "Finished"
_date_   = "2021-02-24"

#LIBRARIES
from machine import UART

#CONFIGURATIONS
uart = UART(1)
uart.init(bits=8, baudrate=9600, parity=None, stop=1, timeout_chars=100, pins('P3', 'P4'))
DATA_1 = int(uart.read(1)[0])
DATA_2 = int(uart.read(1)[0])
SUM = int(uart.read(1)[0])

#CODE
while True:
    header_bytes = uart.read(1)
    while header_bytes != b'\xff'):
        header_bytes = uart.read(1)

    if DATA_1 + DATA_2 == SUM
        distance = (DATA_1*256)+ DATA_2
        print(distance)