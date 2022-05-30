import serial
import time as t

ser = serial.Serial()
ser.baudrate = 115200
ser.setPort('/dev/ttyACM1')

ser.open()
print(ser.name)
ser.write(b"5T\n")
t.sleep(3)
print("START")
ser.write(b'5P0000 0000\n')
t.sleep(0.03)
ser.write(b'5P0000 2000\n')
t.sleep(3)
ser.write(b'5P0000 0000\n')

ser.close()
print("END")
