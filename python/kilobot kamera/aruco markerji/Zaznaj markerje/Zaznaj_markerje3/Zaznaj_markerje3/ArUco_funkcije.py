#-- -------------------------------------------------------------- --#
#   Ime datoteke : ArUco_funkcije.py      - po potrebi spremeni
#-- -------------------------------------------------------------- --#
#   Funkcije za delovenje programa za detekcijo ArUco markerjev
#       Matej S.     24.3.2020
#-- -------------------------------------------------------------- --#
#   Potrebni instalirani moduli za delovanje funkcij:                 
#       -numpy (1.18)
#       -opencv-contrib-python (4.2.0)
#-- -------------------------------------------------------------- --#

import cv2 as cv
import numpy as np
from cv2 import aruco
import os
import datetime

# klas je tko funkcija, ki ima vec metod(zadeve ki jih klices) - funkcije, lokalne spremenljivke
class NacinDelovanja:
    def __init__(self, CAMERA_VIDEO_OUTPUT_NAME, MARKER_VIDEO_OUTPUT_NAME, VIDEO_INPUT_NAME, SNEMAJ, IZ_DATOTEKE):
        self.CAMERA_VIDEO_OUTPUT_NAME = CAMERA_VIDEO_OUTPUT_NAME
        self.MARKER_VIDEO_OUTPUT_NAME = MARKER_VIDEO_OUTPUT_NAME
        self.VIDEO_INPUT_NAME = VIDEO_INPUT_NAME
        self.SNEMAJ = SNEMAJ
        self.IZ_DATOTEKE = IZ_DATOTEKE

#-- Ustvari objekt Marker
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

cv
def InicializacijaDetekcije(delovanje):
    #-- Ustvari seznam devetih markerjev
    Markerji = []
    for i in range(1,15):
        Markerji.append(Marker([0,0],0,i))

    #-- aruco baza markerjev
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

    #-- vklop kamere/ branja videodatoteke
    if delovanje.IZ_DATOTEKE is True:
        zajem = cv.VideoCapture(delovanje.VIDEO_INPUT_NAME);
        fps = zajem.get(cv.CAP_PROP_FPS)
        frames = int(zajem.get(cv.CAP_PROP_FRAME_COUNT))
    else:
        zajem = cv.VideoCapture(1);
        fps = None
        frames = None

    if delovanje.SNEMAJ:
        # Zbriše prejšnji shranjen posnetek
        if os.path.isfile(delovanje.CAMERA_VIDEO_OUTPUT_NAME):
            os.remove(delovanje.CAMERA_VIDEO_OUTPUT_NAME)

        # Zbriše prejšnji shranjen posnetek
        if os.path.isfile(delovanje.MARKER_VIDEO_OUTPUT_NAME):
            os.remove(delovanje.MARKER_VIDEO_OUTPUT_NAME)

    if zajem.isOpened():
        print("Video zajemanje")
        sirina = zajem.get(cv.CAP_PROP_FRAME_WIDTH)
        visina = zajem.get(cv.CAP_PROP_FRAME_HEIGHT)
        print("Resolucija:"+ str(int(sirina)) + "X" + str(int(visina)))
        print("Za zaprtje okna pritisni tipko q")

        # definiraj kodek za snemanje in ustvari VideoWriter objekta
        if delovanje.SNEMAJ is True:
            fourcc = cv.VideoWriter_fourcc(	'X','V','I','D'	)
            out1 = cv.VideoWriter(delovanje.CAMERA_VIDEO_OUTPUT_NAME,fourcc, 20.0, (int(sirina),int(visina)))
            out2 = cv.VideoWriter(delovanje.MARKER_VIDEO_OUTPUT_NAME,fourcc, 20.0, (int(sirina),int(visina)))
            print("Videoposnetek se bo shranjeval.")
        else:
            out1 = None
            out2 = None
    else:
        print("Napaka pri vklopu kamere ali branju videoposnetka")
    return(Markerji, aruco_dict, zajem, out1, out2, sirina, visina, fps, frames)

def IzvajajDetekcijo(Markerji, aruco_dict, zajem, SNEMAJ, out1, out2, skaliraj):
    Z_cas = datetime.datetime.now()
    if(zajem.isOpened()):
        ret, slika = zajem.read()
        # skaliranje prevelike slike za hitrejšo detekcijo
        width = int(slika.shape[1] * skaliraj / 100)
        height = int(slika.shape[0] * skaliraj / 100)
        dim = (width, height)
        # resize image
        slika_rs = cv.resize(slika, dim, interpolation = cv.INTER_AREA)
        # tresholding in detekcija
        gray = cv.cvtColor(slika_rs, cv.COLOR_BGR2GRAY)
        parameters =  aruco.DetectorParameters_create()
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        frame_markers = aruco.drawDetectedMarkers(slika_rs.copy(), corners, ids)

        #-- če je na sliki kak marker
        if ids is not None:
            for i in range(0,len(ids)):
                #-- določanje pozicije in orientacije markerjev na sliki
                vogali = corners[i]                                 # vogali enega od zaznanih markerjev
                center, kot = ZaznajVogali(vogali,frame_markers, dim, skaliraj)    # določi center in kot markerja (in označi na sliki)
                Markerji[ids[i][0]-1].setData(center, kot)          # zapiši podatke v seznam markerjev
        #-- ------------------------------------------------------------ --#
        # velikost slike za prikaz
        cv.namedWindow("markerji", cv.WINDOW_NORMAL)
        #cv.resizeWindow("markerji", int(1920/2),int(1080/2))  
        
        #-- prikaži sliko z označbami
        cv.imshow("markerji",frame_markers)

        if SNEMAJ:
            #-- shrani video kamere
            out1.write(slika)
            #-- shrani video z marker overlayom
            out2.write(frame_markers)
    else:
        print("Napaka pri detekciji!")
    # vrni čas izvajanja detekcije
    K_cas = datetime.datetime.now()
    delta_cas = K_cas - Z_cas
    delta_cas = int(delta_cas.total_seconds() * 1000)
    return delta_cas

def KonecDetekcije(zajem, SNEMAJ, out1, out2):
    if SNEMAJ:
        out1.release()
        out2.release()
        print("Videoposnetek shranjen.")

    zajem.release()
    cv.destroyAllWindows()



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

def MarkerKotRad(Center, Spredaj):
    pi = np.pi
    kot = np.arctan2(Spredaj[1]-Center[1],Spredaj[0]-Center[0])
    if kot < 0:
        kot = 2*pi + kot
    return kot

def Razdalja2D(T1,T2):
    d = np.sqrt((T1[1]-T2[1])**2 + (T1[0]-T2[0])**2 )
    return d

def Krog(Slika, Center,Spredaj,k):
    radij = int( k *( Razdalja2D(Center,Spredaj) ))
    cv.circle(Slika, (Center[0],Center[1]), radij ,(0,0,255), thickness=1, lineType=8, shift=0)
    return None

def Daljica(Slika,T1,T2):
    cv.line(Slika, (T1[0],T1[1]), (T2[0],T2[1]), (0,0,255), thickness=1, lineType=8, shift=0)
    return None

def clc():
    os.system('cls' if os.name=='nt' else 'clear')
    return None
