import cv2 as cv
from pyueye import ueye

import datetime

import ZajemKamere
from KilobotData import KilobotData
from KilobotController import KilobotController

d = KilobotData()
c = KilobotController()

while(d.nRet == ueye.IS_SUCCESS):

    d.t1= datetime.datetime.now()

    d=ZajemKamere.get_markers(d)    #Pridobitev dejanskih položajev

    if len(d.Markerji) != 0:
        d = c.calcRef(d)                #Izračun željenih položajev    
        d = c.calcPWM(d)                #Določitev PWM vrednosti
        
        c.sendData(d.SerialData)   #Pošiljanje PWM vrednosti
        d.SerialData = ""



    d.t2 = datetime.datetime.now()
    delta_cas = d.t2 - d.t1
    delta_cas = int(delta_cas.total_seconds() * 1000)
    print("Cas detekcije:", delta_cas, " ms")

    # Pritisk na Q za izhod iz programa
    if cv.waitKey(70-delta_cas) & 0xFF == ord('q'):
        break

c.end(d)
cv.destroyAllWindows()
    
