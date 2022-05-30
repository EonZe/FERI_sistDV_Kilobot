 >>> import serial
>>> ser = serial.Serial('/dev/ttyACM1')  # open serial port
>>> print(ser.name)         # check which port was really used
>>> ser.write(b'5T\n')     # write a string
>>> ser.close()
