#!/usr/bin/python
import serial
ser = serial.Serial('/dev/ttyACM0', 115200)
read_byte = ser.read()
line = ''
while read_byte is not None:
    read_byte = ser.read()
    if (read_byte == '\n' or read_byte == '\r'):
        print(str(line))
        line = ''
    else:
        # line += repr(read_byte)
        line += read_byte
