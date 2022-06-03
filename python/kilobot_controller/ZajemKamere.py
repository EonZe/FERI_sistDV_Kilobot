from pyueye import ueye
import numpy as np
import cv2 as cv
from cv2 import aruco

from KilobotData import Marker


def get_markers(data):
       
    array = ueye.get_data(data.pcImageMemory, data.width, data.height, data.nBitsPerPixel, data.pitch, copy=False)
    frame = np.reshape(array, (data.height.value, data.width.value, 1))
    
    slika_rs = cv.resize(frame, data.dim, interpolation = cv.INTER_AREA)

    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(slika_rs, data.aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(slika_rs.copy(), corners, ids)
    
    data.Markerji.clear()
    if ids is not None:
        for i in range(0,len(ids)):
            #-- določanje pozicije in orientacije markerjev na sliki
            id=ids[i][0]
            vogali = corners[i]                                 # vogali enega od zaznanih markerjev
            center, kot = ZaznajVogale(vogali, data.dim, data.skaliraj)    # določi center in kot markerja (in označi na sliki)
            data.Markerji.append(Marker(id, center, kot))         # zapiši podatke v seznam markerjev
    
    cv.imshow("Kilobot vodenje", frame_markers)
    return data


def ZaznajVogale(vogali,dim,skaliraj):
    #-- določanje pozicije in orientacije markerjev na sliki¸ra markerja
    Center = MarkerCenterKoord(vogali)      # koordinate centra markerja
    Spredaj = MarkerSpredajKoord(vogali)    # koordinate sredine sprednjega roba
    Center[1] = dim[1]-Center[1]
    Spredaj[1] = dim[1]-Spredaj[1]
    kot = MarkerKotDeg(Center,Spredaj)      # rotacija markerja v stopinjah

    Center = [int(Center[0]*100/skaliraj), int(Center[1]*100/skaliraj)]
    return(Center, kot)

def MarkerCenterKoord(vogali):
    Center = [int((vogali[0][0][0] + vogali[0][2][0]) / 2), int((vogali[0][0][1] + vogali[0][2][1]) / 2)]
    return Center

def MarkerSpredajKoord(vogali):
    Spredaj = [int((vogali[0][0][0] + vogali[0][1][0]) / 2), int((vogali[0][0][1] + vogali[0][1][1]) / 2)]
    return Spredaj

def MarkerKotDeg(Center, Spredaj):
    pi = np.pi
    kot = 180/pi*np.arctan2(Spredaj[1]-Center[1],Spredaj[0]-Center[0])
    if kot < 0:
        kot = 360 + kot
    return int(kot)

