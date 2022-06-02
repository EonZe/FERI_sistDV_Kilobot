from pyueye import ueye
import numpy as np
import cv2 as cv
from cv2 import aruco
import ctypes
import datetime
import time


class Marker:
    def __init__(self, center, kot, id):
        self.center = center
        self.kot = kot
        self.id = id

    def getData(self):
        return(self.id, self.center, self.kot)

    def setData(self, center, kot):
        self.center = center
        self.kot = kot
        return None
    
def ZaznajVogali(vogali,Slika,dim,skaliraj):
    #-- določanje pozicije in orientacije markerjev na sliki
    Center = MarkerCenterKoord(vogali)      # koordinate centra markerja
    Spredaj = MarkerSpredajKoord(vogali)    # koordinate sredine sprednjega roba
    Center[1] = dim[1]-Center[1]
    Spredaj[1] = dim[1]-Spredaj[1]
    kot = MarkerKotDeg(Center,Spredaj)      # rotacija markerja v stopinjah
    #kot = MarkerKotRad(Center,Spredaj)     # rotacija markerja v radianih

    #Krog(Slika,Center,Spredaj,1.5)          # nariši krog okoli markerja
    #Daljica(Slika,Center,Spredaj)           # nariši daljico med centrom in sprednjim robom
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

Markerji = []
for i in range(1,15):
    Markerji.append(Marker([0,0],0,i))



hCam = ueye.HIDS(0)
cInfo = ueye.CAMINFO()
sInfo = ueye.SENSORINFO()
pcImageMemory = ueye.c_mem_p()
MemID = ueye.int()
rectAOI = ueye.IS_RECT()
pitch = ueye.INT()
nBitsPerPixel = ueye.INT(8)  # 8 bits per pixel za monochrome (crno belo)
bytes_per_pixel = 1 # nBitsPerPixel / 8
channels = 1  # channel 1 za monochrome
m_nColorMode = ueye.IS_CM_MONO8  
img_counter = 0

width = rectAOI.s32Width
height = rectAOI.s32Height

nRet = ueye.is_InitCamera(hCam, None)
if nRet != ueye.IS_SUCCESS:
    print("is_InitCamera ERROR")

nRet = ueye.is_GetCameraInfo(hCam, cInfo)
if nRet != ueye.IS_SUCCESS:
    print("is_GetCameraInfo ERROR")

nRet = ueye.is_GetSensorInfo(hCam, sInfo)
if nRet != ueye.IS_SUCCESS:
    print("is_GetSensorInfo ERROR")

ueye.is_ParameterSet(hCam, ueye.IS_PARAMETERSET_CMD_LOAD_FILE, ueye.c_wchar_p('parametr_test2.ini'), 16)

nRet = ueye.is_AOI(hCam, ueye.IS_AOI_IMAGE_GET_AOI, rectAOI, ueye.sizeof(rectAOI))
if nRet != ueye.IS_SUCCESS:
    print("is_AOI ERROR")

Ret = ueye.is_AllocImageMem(hCam, width, height, nBitsPerPixel, pcImageMemory, MemID)
if nRet != ueye.IS_SUCCESS:
    print("is_AllocImageMem ERROR")

nRet = ueye.is_SetImageMem(hCam, pcImageMemory, MemID)
if nRet != ueye.IS_SUCCESS:
    print("is_SetImageMem ERROR")

ueye.is_SetColorMode(hCam, m_nColorMode)

nRet = ueye.is_CaptureVideo(hCam, ueye.IS_DONT_WAIT)
if nRet != ueye.IS_SUCCESS:
    print("is_CaptureVideo ERROR")

nRet = ueye.is_InquireImageMem(hCam, pcImageMemory, MemID, width, height, nBitsPerPixel, pitch)
if nRet != ueye.IS_SUCCESS:
    print("is_InquireImageMem ERROR")

print(pcImageMemory)
print()
print(width)
print(height)
print()
print(nBitsPerPixel)
print()
print(pitch)
print()
print(cInfo)
print()
print(sInfo)



aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
dim = (1280, 960)
skaliraj = 100


while(nRet == ueye.IS_SUCCESS):
    
    
    Z_cas = datetime.datetime.now()
    
    array = ueye.get_data(pcImageMemory, width, height, nBitsPerPixel, pitch, copy=False)
    frame = np.reshape(array, (height.value, width.value, 1))
    #frame = cv.resize(frame,(0,0),fx=1, fy=1)
    
    slika_rs = cv.resize(frame, dim, interpolation = cv.INTER_AREA)
    
    #gray = cv.cvtColor(slika_rs, cv.COLOR_BGR2GRAY)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(slika_rs, aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(slika_rs.copy(), corners, ids)
    
    if ids is not None:
        for i in range(0,len(ids)):
            #-- določanje pozicije in orientacije markerjev na sliki
            vogali = corners[i]                                 # vogali enega od zaznanih markerjev
            center, kot = ZaznajVogali(vogali,frame_markers, dim, skaliraj)    # določi center in kot markerja (in označi na sliki)
            Markerji[ids[i][0]-1].setData(center, kot)          # zapiši podatke v seznam markerjev
    
    cv.imshow("OpenCV_PyuEye_Test", frame_markers)
    #img_name = "opencv_frame_{}.png".format(img_counter)
    #cv2.imwrite(img_name, frame)
    #print("{} written!".format(img_name))
    #img_counter += 1
    
    for i in range(len(Markerji)):
        print(Markerji[i].getData())

    #time.sleep(0.164)
    #time.sleep(1)
    
    K_cas = datetime.datetime.now()
    delta_cas = K_cas - Z_cas
    delta_cas = int(delta_cas.total_seconds() * 1000)
    print("Cas detekcije:", delta_cas, " ms")

    # Pritisk na Q za izhod iz programa
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    
    


cv.destroyAllWindows()
    
