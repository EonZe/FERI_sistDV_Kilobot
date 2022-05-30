#-- -------------------------------------------------------------- --#
#   Program za detekcijo ArUco markerjev
#       Matej S.     24.4.2020
#-- -------------------------------------------------------------- --#
#   Potrebni instalirani moduli za delovanje funkcij:                 
#       -numpy (1.18)
#       -opencv-contrib-python (4.2.0) 
#-- -------------------------------------------------------------- --#
from ArUco_funkcije import *


#-- ime izhodnih video datotek
#-- ob vsakem shranjevanju se prejšnja verzija izbriše
CAMERA_VIDEO_OUTPUT_NAME = 'kamera.avi'
MARKER_VIDEO_OUTPUT_NAME = 'marker_overlay.avi'
#-- ime vhodne video datoteke
#VIDEO_INPUT_NAME = 'NORM0003.MP4'
VIDEO_INPUT_NAME = 'markerji.avi'
#-- flag za snemanje videoposnetka ( True / False )
#SNEMAJ = True             #-- POSTAVI NA True ČE ŽELIŠ SHRANIT VIDEO
SNEMAJ = False
#-- flag za branje videoposnetka iz datoteke namesto kamere ( True / False )
#IZ_DATOTEKE = True         #-- POSTAVI NA True ČE ŽELIŠ UPORABIT SHRANJEN VIDEOPOSNETEK
IZ_DATOTEKE = False 

#-- -------------------------------------------------------------- --#
#-- Inicializacija izvajanja detekcije markerjev
delovanje = NacinDelovanja(CAMERA_VIDEO_OUTPUT_NAME, MARKER_VIDEO_OUTPUT_NAME, VIDEO_INPUT_NAME, SNEMAJ, IZ_DATOTEKE)
Markerji, aruco_dict, zajem, out1, out2, sirina, visina, fps, frames = InicializacijaDetekcije(delovanje)
count = 1 # števec izvajanja
#-- -------------------------------------------------------------- --#
skaliraj = 100 # odstotek prvotne velikosti slike

# glavni loop
while(True):
    #-- izvajanje detekcije markerjev
    delta_cas = IzvajajDetekcijo(Markerji, aruco_dict, zajem, SNEMAJ, out1, out2, skaliraj)
    
    #-- pobriši command line
    clc()
    #-- izpiši podatke markerjev
    for i in range(len(Markerji)):
        print(Markerji[i].getData())
    #-- izpiši čas izvajanja detekcije markerjev
    print("Čas izvajanja:",delta_cas,"ms")
    #-- ob branju videoposnetka iz datoteke moramo določit pravilno zakasnitev ter konec izvajanja
    if delovanje.IZ_DATOTEKE is True:
        if(1000/fps > delta_cas):
            delay = int(1000/fps - delta_cas)
        else:
            delay = 1
        if count+1 >= frames:
            break
    else:
        delay = 1
    # okno se zapre ob pritisku tipke q 
    if cv.waitKey(delay) & 0xFF == ord('q'):
        break

    #-- prištej števec
    count = count+1
    
#-- konec izvajanja detekcije markerjev
KonecDetekcije(zajem, delovanje.SNEMAJ, out1, out2)   # shranemo posnetek in pobrišemo spremenljivke
