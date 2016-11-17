#!/usr/bin/python
import serial
ser = serial.Serial('/dev/tty.usbmodem1412', 38400)
read_byte = ser.read()
line = ''
while read_byte is not None:
    read_byte = ser.read()
    if read_byte == b' ':
        print(line)
        line = ''
    else:
        line += repr(read_byte)
