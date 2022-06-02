from weakref import ref
import serial
import numpy as np
import time as t

class KilobotController:
    def __init__(self):
        self.t = t.datetime.datetime.now()

        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.setPort('/dev/ttyACM1')

        self.ser.open()
    def sendData(self,data):
        self.ser.write(data+'\n')
    
    def end(self):
        self.ser.close()

    def calcPWM(self,data):
        for i in range(0,len(data.ids)):
            marker = data.Markerji[data.ids[i][0]-1]
            
            id = marker.id
            th_m = marker.kot
            p_m = marker.center

            dif = data.ref[id]-p_m[id]

            th_dif = data.Math_Utills.angle_between(np.array[1,0], np.array(dif))
            d_th=th_dif-th_m

        #"regulacija" položaja
            if (abs(dif) > 10):
                PWM1 = 1400
                PWM2 = 1400

                if np.abs(d_th) < 1:
                    if d_th > 0:
                        PWM1 = 0
                    elif d_th < 0:
                        PWM2 = 0
                if id > 9:
                    data.SerialData+= chr(55+id)+"P"+str(PWM1).zfill(4)+" "+str(PWM2).zfill(4)+";"
                else:
                    data.SerialData+= str(id)+"P"+str(PWM1).zfill(4)+" "+str(PWM2).zfill(4)+";" 
        return data
    
    
    def calcRef(self, data):
        for i in range(0,data.N):
            data.ref[i] = [i*50, 200]
        return data


