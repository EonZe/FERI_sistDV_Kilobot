#https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
#https://www.geeksforgeeks.org/circle-detection-using-opencv-python/
#https://www.geeksforgeeks.org/connect-your-android-phone-camera-to-opencv-python/
#https://www.fdxlabs.com/calculate-x-y-z-real-world-coordinates-from-a-single-camera-using-opencv/
#https://lindevs.com/detect-and-decode-qr-code-in-image-using-opencv/
#https://techtutorialsx.com/2019/04/13/python-opencv-converting-image-to-black-and-white/
#https://learnopencv.com/edge-detection-using-opencv/

import cv2
import numpy as np
import requests
import imutils

url = "http://192.168.43.1:8080/shot.jpg"

def calculate_XYZ(self,u,v):

        #Solve: From Image Pixels, find World Points

        uv_1=np.array([[u,v,1]], dtype=np.float32)
        uv_1=uv_1.T
        suv_1=self.scalingfactor*uv_1
        xyz_c=self.inverse_newcam_mtx.dot(suv_1)
        xyz_c=xyz_c-self.tvec1
        XYZ=self.inverse_R_mtx.dot(xyz_c)

return XYZ

while(True):
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)
    frame = imutils.resize(frame, width=1000, height=1800)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray,(9,9), sigmaX=0, sigmaY=0)
    edges = cv2.Canny(image=gray_blur, threshold1=100, threshold2=200)


    detected_circles = cv2.HoughCircles(edges,
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                param2 = 30, minRadius = 170, maxRadius = 200)

    detector = cv2.QRCodeDetector()
    data, decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(gray)

    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

    if points is not None:
        # display the image with lines
        # length of bounding box

        for i in range(len(points)):
            pt1 = [int(points[i][0][0]), int(points[i][0][1])]
            pt2 = [int(points[i][1][0]), int(points[i][1][1])]
            pt3 = [int(points[i][2][0]), int(points[i][2][1])]
            pt4 = [int(points[i][3][0]), int(points[i][3][1])]

            cv2.line(frame, pt1, pt2, color=(255, 0, 0), thickness=3)
            cv2.line(frame, pt2, pt3, color=(255, 0, 0), thickness=3)
            cv2.line(frame, pt3, pt4, color=(255, 0, 0), thickness=3)
            cv2.line(frame, pt1, pt4, color=(255, 0, 0), thickness=3)

            if detected_circles is not None:
                for pt in detected_circles[0, :]:
                    a, b, r = pt[0], pt[1], pt[2]
                    if ((pt1[0]+pt3[0])/2 - a)**2 + ((pt1[1]+pt3[1])/2 - b)**2 < r**2:
                        print(f"QRCode data:\n{decoded_info}")
                        print(f"Position:\nX:{a}\nY:{b}\nR:{r}")
                        break

    # Display the resulting framesobelxy
    cv2.imshow('KilobotGUI', frame)
    cv2.imshow('KilobotGUI gray', gray)
    cv2.imshow('KilobotGUI edges', edges)


    # the 'q' button is set as the
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy all the windows
cv2.destroyAllWindows()
