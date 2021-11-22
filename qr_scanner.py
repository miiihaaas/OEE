import cv2
from pyzbar.pyzbar import decode
import time

#####################################
### ovaj kod čita QR kod sa fajla ###
#####################################
img = cv2.imread("D:\Mihas\Programming\Python\Projects\OEE\OEE\QR_code.png")
print(decode(img))

for code in decode(img):
    # print(code.type)
    # print(code.data.decode("UTF8"))
    pass

txt = code.data.decode("UTF8")
x = txt.split("-")
id_, rn = x[0], x[1]
print(f"ID gotovog proizvoda je: {id_}")
print(f"Radni nalog gotovog proizvoda je: {rn}")
time.sleep(3)
######################################
### ovaj kod čita QR kod sa kamere ###
######################################
cap = cv2.VideoCapture(0)
cap.set(3, 640) #3 - width
cap.set(4, 480) #4 - height

camera = True
while camera == True:
    success, frame = cap.read()
    print(f"uspešnost: {success}, frejm: {frame}")
    for code in decode(frame):
        print(code.data.decode("UTF8"))
    cv2.imshow("Testing code scan", frame)
    cv2.waitKey(1)
