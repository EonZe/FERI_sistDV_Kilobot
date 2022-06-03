from weakref import ref
import serial
import numpy as np
from KilobotData import Math_Utills as mu

class KilobotController:
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.setPort('COM6')#6,7
        #self.ser.setPort('/dev/ttyACM1')

        self.ser.open()

    def sendData(self,data):
        self.ser.write((data+'\n').encode())
    
    def end(self,data):
        msg = ""
        for i in range(0,data.N):
            if i > 9:
                msg+= chr(55+i)+"P0000 0000;"
            else:
                msg+= str(i)+"P0000 0000;"
        
        self.sendData(msg)
        self.ser.close()

    def calcPWM(self,data):
        for i in range(0,len(data.Markerji)):
            marker = data.Markerji[i]

            id = marker.id

            param = data.kb_param[id]
            marker.kot +=param.offset_kota
            if marker.kot > 180:
                marker.kot -= 360
   
            th_m = marker.kot
            p_m = marker.center

            dif = [-(data.ref[id][0]-p_m[0]), -(data.ref[id][1]-p_m[1])]

            th_dif = mu.MarkerKotDeg([1,0], dif)
            d_th=th_dif-th_m
            abs_dth = np.abs(d_th)
            if d_th > 180:
                d_th -= 360

        #"regulacija" položaja
            PWM1 = 0
            PWM2 = 0
            abs_dif=mu.abs(np.array(dif))
            if (abs_dif > 100):
                PWM1 = 2000
                PWM2 = 2000

                if abs_dth > 10:
                    if d_th < 0:
                        PWM1 = 0
                        PWM2 = 2000
                    elif d_th > 0:
                        PWM1 = 2000
                        PWM2 = 0
            elif (abs_dif > 20):
                PWM1 = 1500*param.k_M1*(abs_dif/30)
                PWM2 = 1500*param.k_M2*(abs_dif/30)

                if abs_dth > 10:
                    if d_th < 0:
                        PWM1 = 0
                        PWM2 = 1500*param.k_M2*(abs_dif/20)
                    elif d_th > 0:
                        PWM1 = 1500*param.k_M1*(abs_dif/20)
                        PWM2 = 0
            elif (abs_dif > 15):
                PWM1 = 2000*param.k_M1*(abs_dif/35)
                PWM2 = 2000*param.k_M2*(abs_dif/35)

                if abs_dth > 10:
                    if d_th < 0:
                        PWM1 = 0
                        PWM2 = 2000*param.k_M2*(abs_dif/35)
                    elif d_th > 0:
                        PWM1 = 2000*param.k_M1*(abs_dif/35)
                        PWM2 = 0
            else:
                PWM1 = PWM2 = 0
            if PWM1 > 2000:
                PWM1 = 2000
            elif PWM1 < 0:
                PWM1 = 0
            
            if PWM2 > 2000:
                PWM2 = 2000
            elif PWM2 < 0:
                PWM2 = 0

            
            if id > 9:
                data.SerialData+= chr(55+id)+"P"+str(PWM1).zfill(4)+" "+str(PWM2).zfill(4)+";"
            else:
                data.SerialData+= str(id)+"P"+str(PWM1).zfill(4)+" "+str(PWM2).zfill(4)+";" 
        print("Kilobot: ",marker.getData(),", E: ",dif,", |E|: ",abs_dif,", th_E: ", th_dif,", d_th: ",d_th)
        print("PWM1: ",PWM1,", PWM2: ",PWM2)
        return data
    
    
    def calcRef(self, data):
        for i in range(0,data.N):
            data.ref[i] = [600, 400]
        return data


