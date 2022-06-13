import cv2 as cv
from pyueye import ueye

import datetime
import os

import ZajemKamere
from KilobotData import KilobotData
from KilobotController import KilobotController

d = KilobotData()
c = KilobotController()

while(d.nRet == ueye.IS_SUCCESS):

    d.t1= datetime.datetime.now()

    d=ZajemKamere.get_markers(d)    #Pridobitev dejanskih položajev

    if len(d.Markerji) != 0:
        os.system('cls')
        d = c.calcTarget(d)
        d = c.calcMove(d)                #Izračun željenih položajev
        
        c.sendData(d.SerialData)   #Pošiljanje PWM vrednosti
        d.SerialData = ""

    d.t2 = datetime.datetime.now()
    delta_cas = d.t2 - d.t1
    delta_cas = int(delta_cas.total_seconds() * 1000)
    #print("Cas detekcije:", delta_cas, " ms")

    # Pritisk na Q za izhod iz programa
    if delta_cas <70:
        if cv.waitKey(70-delta_cas) & 0xFF == ord('q'):
            break
    else:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


c.end(d)
cv.destroyAllWindows()
    
