


import cv2 as cv
import numpy as np
from cv2 import aruco
import os
import datetime
import requests
import imutils



url = "http://192.168.43.1:8080/shot.jpg"

clear = lambda: os.system('clear')

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters =  aruco.DetectorParameters_create()

ref=[]
pos=[]
rot=[]



ref[3] = ref[3]+[100, 100]

print("START")


while(True):
    t1 = datetime.datetime.now()
    
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv.imdecode(img_arr, -1)
    frame = imutils.resize(frame, width=1000, height=1800)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict, parameters=parameters, cameraMatrix=matrix_coefficients, distCoeff=distortion_coefficients)
    ids=[]

    if ids is not None:
        for i in range(0,len(ids)):
            #rvec, tvec, markerPoints = aruco.estimatePoseSingleMarkers(corners[i], 0.03, matrix_coefficients, distortion_coefficients)

            #(rvec - tvec).any()  # get rid of that nasty numpy value array error
            #aruco.drawDetectedMarkers(frame, corners)  # Draw A square around the markers
            #aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)  # Draw Axis
           


    t2 = datetime.datetime.now()
    dt=t2-t1;

    if cv.waitKey(70-dt) & 0xFF == ord('q'):
        break
    
#-- konec izvajanja detekcije markerjev


ser.close()
print("END")
