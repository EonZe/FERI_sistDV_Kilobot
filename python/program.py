import serial
import time as t

ser = serial.Serial()
ser.baudrate = 115200
ser.setPort('/dev/ttyACM1')

ser.open()
print(ser.name)
#ser.write(b"3T\n")
#t.sleep(3)
print("START")
t.sleep(1)
ser.write(b'5P1500 0000\n')
t.sleep(30)
#6309
ser.write(b'5P0000 0000\n')
t.sleep(1)
#7263
ser.write(b'5P0000 2000\n')
t.sleep(30)
#37482
ser.write(b'5P0000 0000\n')
t.sleep(1)
#38535
ser.write(b'5P1400 1400\n')
t.sleep(30)
#48197
ser.write(b'5P0000 0000\n')

ser.close()
print("END")
