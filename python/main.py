import cv2 as cv
from pyueye import ueye

import datetime

import ZajemKamere
from KilobotData import KilobotData
import KilobotController

d = KilobotData()
c = KilobotController(d)

while(d.nRet == ueye.IS_SUCCESS):

    d.t1= datetime.datetime.now()

    d=ZajemKamere.get_markers(d)    #Pridobitev dejanskih položajev

    if d.ids is not None:
        d = c.calcRef(d)                #Izračun željenih položajev    
        d = c.calcPWM(d)                #Določitev PWM vrednosti
        c.sendData(c.SerialData+'\n')   #Pošiljanje PWM vrednosti


    d.t2 = datetime.datetime.now()
    delta_cas = d.t2 - d.t1
    delta_cas = int(delta_cas.total_seconds() * 1000)
    print("Cas detekcije:", delta_cas, " ms")

    # Pritisk na Q za izhod iz programa
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

c.end()
cv.destroyAllWindows()
    
