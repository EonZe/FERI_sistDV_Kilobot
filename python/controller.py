from weakref import ref
import serial
import numpy as np
import time as t
from Zajem_detekcija import Marker as m

class KilobotController:
    def __init__(self, N):
        self.N = N
        self.t = t.datetime.datetime.now()

        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.setPort('/dev/ttyACM1')

        for i in range(0,N+1):
            self.ref.append([0, 0])

        self.ser.open()
    def sendData(self,data):
        self.ser.write(data+'\n')
    
    def end(self):
        self.ser.close()
    def cycle(self):
        for i in range(0, self.N):
            self.calcPWM(Zaj)
        self.sendData(self.SerialData+'\n')

    def calcPWM(self,marker):
        id = marker.id
        th_m = marker.kot
        p_m = marker.center

        dif = self.ref[id]-p_m[id]
        self.pos[id] = p_m

        th_dif = Math_Utills.angle_between(np.array[1,0], np.array(dif))
        d_th=th_dif-th_m

        if (abs(dif) > 10):
            PWM1 = 1400
            PWM2 = 1400

            if np.abs(d_th) < 10:
                if d_th > 0:
                    PWM1 = 0
                elif d_th < 0:
                    PWM2 = 0
            if id > 9:
                self.SerialData+= chr(55+id)+"P"+str(PWM1).zfill(4)+" "+str(PWM2).zfill(4)+";"
            else:
               self.SerialData+= str(id)+"P"+str(PWM1).zfill(4)+" "+str(PWM2).zfill(4)+";" 

    def calcRef(self):
        for i in range(0,self.N+1):
            ref[i] = [i*100, 200]

class Math_Utills:

    def angle_between(v1, v2):
        """ Returns the angle in radians between vectors 'v1' and 'v2'::

                >>> angle_between((1, 0, 0), (0, 1, 0))
                1.5707963267948966
                >>> angle_between((1, 0, 0), (1, 0, 0))
                0.0
                >>> angle_between((1, 0, 0), (-1, 0, 0))
                3.141592653589793
        """
        v1_u = v1 / np.linalg.norm(v1)
        v2_u = v2 / np.linalg.norm(v2)
        fi= np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
        return np.degrees(fi)

