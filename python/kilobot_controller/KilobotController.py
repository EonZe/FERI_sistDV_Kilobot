import serial
import numpy as np
import math
import time
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

    def calcMove(self,data):
        for i in range(0,len(data.Markerji)):
            marker = data.Markerji[i]

            id = marker.id
            if id > data.N-1:
                continue
            param = data.kb_param[id]
            
            th_m = marker.kot+param.offset_kota
            if th_m <0:
                th_m += 360

            p_m = marker.center

            dif = [-(data.ref[id][0]-p_m[0]), -(data.ref[id][1]-p_m[1])]
            abs_dif=mu.abs(np.array(dif))     #Razdalja markerja od vmesne tocke

            difE = [-(data.target[id][0]-p_m[0]), -(data.target[id][1]-p_m[1])] #Odstopanje od koncnega polozaja
            abs_difE=mu.abs(np.array(difE))     #Razdalja markerja od koncne tocke

            th_dif = mu.MarkerKotDeg([1,0], dif)
           

            PWM1  = PWM2 = 0                     #Deklaracija PWM spremenljivk

            ZONE = 15                           #Tolerancno obmocje

            if abs_difE > ZONE:                   #Kontrola, ce je kilobot v obmocju dovoljenega odstopanja od koncne tocke
                self.calcRef(data, marker, difE,abs_dif)
                data.allAtTarget &= False

                PWM1, PWM2 = self.calcPWM(th_m,th_dif,0.1,param,abs_difE)
    
            else:
                data.kb_param[marker.id].endReached = True
                data.allAtTarget &= True
            
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
        print("Kilobot: ",marker.getData(),", R:,",data.ref[id],", E_m: ",dif,", |E_T|: ",abs_difE,", th_m: ", th_m,", th_dif: ",th_dif)
        #print(", E_m: ",dif,", th_m: ", th_m,", th_dif: ",th_dif)
        return data
    
    def calcPWM(self,th_m,th_dif,k,param,abs_dif): #Izracun PWM vrednosti
        
        d_th1 =th_dif-th_m
        if d_th1 > 180:
            d_th1 -=360
        elif d_th1 < -180:
            d_th1+=360
      
        abs_dth1 = np.abs(d_th1)

        print("th1: ",th_dif,", th2: ", th_m)
        print("dth1: ",d_th1,", |dth1|: ", abs_dth1)

        return self.pomik(d_th1, abs_dth1, abs_dif,k,param)

    def pomik(self, d_th,d_th_abs,abs_dif, k,param):
        PWM1 = PWM2 = 0

        if d_th_abs > 5:
            x =1000+1000*math.log(d_th_abs)*k
            if d_th < 0:
                PWM1 = 0
                PWM2 = int(x*param.k_M2)
            else:
                PWM1 = int(x*param.k_M1)
                PWM2 = 0
        else:
            x =1000+1000*math.log(abs_dif)*k
            PWM1 = int(x*param.k_M1)
            PWM2 = int(x*param.k_M2)
        return PWM1, PWM2
    
    def calcRef(self, data, marker, difE,abs_difE):
        if data.kb_param[marker.id].endReached == True:
            return data
        vE=difE
        ref = [0,0]
        if abs_difE > 20:
            vE[0] /= (abs_difE*0.05)
            vE[1] /= (abs_difE*0.05)
        
        ref[0] = int(marker.center[0] - vE[0])
        ref[1] = int(marker.center[1] - vE[1])

    
        #ref = self.collisions_checker(data, marker, ref)
            
        data.ref[marker.id] = ref
        return data
    
    def collisions_checker(self, data, marker, ref):
        unsafe = True
        tries = 0
        while unsafe == True & tries < 5:
            unsafe = False
            tries += 1
            for i in range(0,len(data.Markerji)):
                marker2 = data.Markerji[i]
                if marker2.id == marker.id:
                    continue
                center2 =marker2.center

                us,ref = self.avoidanceCheck(ref,center2)
                unsafe |= us
        if tries == 5:
            ref = marker.center
        return ref
    
    def avoidanceCheck(ref,center2):
        if mu.insideCircle(c=center2,p=ref, rs=10000) == False:
            return False, ref
        else:
            while mu.insideCircle(c=center2,p=ref, rs=10000):
                d_c2_R=[ref[0]-center2[0], ref[1]-center2[1]]
                ref[0] = center2[0]+d_c2_R[0]*1.1
                ref[1] = center2[1]+d_c2_R[1]*1.1
            return True, ref
    
    def calcTarget(self, data):
        if data.allAtTarget == False:
            data.allAtTarget = True
            return data
        if data.seq < data.nPoints-1:
            data.seq += 1
            print("Cycle seq",data.seq)
        else:
            print("Cycle start")
            data.seq = 0
        time.sleep(1)
        for i in range(0,len(data.Markerji)):
            marker = data.Markerji[i]
            data.kb_param[marker.id].endReached = False
            data.target[marker.id] =data.trajectories[marker.id][data.seq]
        return data