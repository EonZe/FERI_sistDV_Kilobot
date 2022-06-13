from pyueye import ueye
from cv2 import aruco
import datetime as dt

import numpy as np

class KilobotData:
    def __init__(self):
        #inicializacija kamere

        hCam = ueye.HIDS(0)
        cInfo = ueye.CAMINFO()
        sInfo = ueye.SENSORINFO()
        pcImageMemory = ueye.c_mem_p()
        MemID = ueye.int()
        rectAOI = ueye.IS_RECT()
        pitch = ueye.INT()
        nBitsPerPixel = ueye.INT(8)  # 8 bits per pixel za monochrome (crno belo)
        m_nColorMode = ueye.IS_CM_MONO8  

        height = rectAOI.s32Height
        width = rectAOI.s32Width

        
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

        nRet = ueye.is_AllocImageMem(hCam, width, height, nBitsPerPixel, pcImageMemory, MemID)
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


        self.nRet = nRet
        self.pcImageMemory = pcImageMemory
        self.nBitsPerPixel = nBitsPerPixel


        self.pitch = pitch
        self.width = width
        self.height = height

        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        self.dim = (1280, 960)
        self.skaliraj = 100
        
        self.Markerji = [] #Vrednosti markerjev
        self.ref = []      #Vrednosti vmesnih referencnih vrednosti
        self.target = []   #Vrednosti koncnih referenchih vrednosti
        self.N = 15        #Stevilo kilobotov (15->ID 0-14)
        
        for i in range(0,self.N):
            self.ref.append([0,0])
            self.target.append([0,0])
        self.nPoints = 2
        self.seq = 2
        self.trajectories=[ #p1 =790 300 p2=360 470
         [[400, 400], [600, 400]] ,# 0
         [[400, 400], [600, 400]] ,# 1
         [[400, 400], [600, 400]] ,# 2
         [[400, 400], [600, 400]] ,# 3
         [[400, 400], [600, 400]] ,# 4
         [[400, 400], [600, 400]] ,# 5
         [[400, 400], [600, 400]] ,# 6
         [[400, 400], [600, 400]] ,# 7
         [[400, 400], [600, 400]] ,# 8
         [[400, 400], [600, 400]] ,# 9
         [[400, 400], [600, 400]] ,# 10
         [[400, 400], [600, 400]] ,# 11
         [[400, 400], [600, 400]] ,# 12
         [[400, 400], [600, 400]] ,# 13
         [[400, 400], [600, 400]] ,# 14
        ]

        #Hramba časov
        self.t0 = self.t1 = self.t2 = dt.datetime.now()  #t0 - zacetni cas programa, t1- zacetni cas cikla, t2 - koncni cas cikla

        #Info o dosezenih polozajih
        self.allAtTarget = True        #Vsi roboti so na koncnih polozajih
        #hramba podatkov
        self.SerialData = ""

        #parametri kilobotov
        self.kb_param =[
        KilobotParam(id=0, offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=1, offset_kota=-10,M=1,k_M1=0.7,k_M2=0.8),
        KilobotParam(id=2, offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=3, offset_kota=-232,M=0,k_M1=0.8,k_M2=.8),
        KilobotParam(id=4, offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=5, offset_kota=-51,M=0,k_M1=1,k_M2=1),#50
        KilobotParam(id=6, offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=7, offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=8, offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=9, offset_kota=60,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=10,offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=11,offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=12,offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=13,offset_kota=0,M=0,k_M1=1,k_M2=1),
        KilobotParam(id=14,offset_kota=0,M=0,k_M1=1,k_M2=1)]



class Marker:
    def __init__(self, id, center, kot):
        self.id = id
        self.center = center
        self.kot = kot
    
    def getData(self):
        return(self.id, self.center, self.kot)

    def setKot(self, kot):
        self.kot = kot
    
    def setData(self, center, kot):
        self.center = center
        self.kot = kot
        return None
class KilobotParam:
    def __init__(self, id, offset_kota,M, k_M1, k_M2):
        self.id = id
        self.offset_kota = offset_kota
        self.M = M
        self.k_M1 = k_M1
        self.k_M2 = k_M2
        self.endReached = True
    
  
class Math_Utills:
    def MarkerKotDeg(Center, Spredaj):
        pi = np.pi
        kot = 180/pi*np.arctan2(Spredaj[1]-Center[1],Spredaj[0]-Center[0])
        if kot < 0:
            kot += 360
        return int(kot)

    def abs(v):
        return np.linalg.norm(v)
    def insideCircle(c, p,rs):
        return (p[0]-c[0])**2 + (p[1] - c[1])**2 < rs