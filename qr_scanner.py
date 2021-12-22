# link: https://www.youtube.com/watch?v=IOhZqmSrjlE&ab_channel=Pythonenthusiast

import cv2
from pyzbar.pyzbar import decode
import time

######################################
### ovaj kod čita QR kod sa kamere ###
######################################
def scan():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640) #3 - width
    cap.set(4, 480) #4 - height

    id_, rn, slovo, sarza, naziv = 0, 0, 0, 0, 0
    print (id_, rn, slovo, sarza, naziv)

    camera = True # False by default ali kada se prtisne dugme za skenjranje, treba da promeni u True
    while camera == True:
        success, frame = cap.read()
        #print(f"uspešnost: {success}, frejm: {frame}")
        for code in decode(frame):
            # print(code.data.decode("UTF8"))
            txt = code.data.decode("UTF8")
            x = txt.split("-")
            id_, rn, slovo, sarza, naziv = x[0], x[1], x[2], x[3], x[4]
            print(f"{id_=}")
            print(f"{rn=}")
            print(f"{slovo=}")
            print(f"{sarza=}")
            print(f"{naziv=}")
            time.sleep(1)
            if id_ != 0:
                return id_, rn, slovo, sarza, naziv

        cv2.imshow("Testing code scan", frame)
        cv2.waitKey(20)

    def scan_kvar_id():
        cap = cv2.VideoCapture(0)
        cap.set(3, 640) #3 - width
        cap.set(4, 480) #4 - height

        kvar_id, opis_kvara = 0, 0
        print (kvar_id, opis_kvara)

        camera = True # False by default ali kada se prtisne dugme za skenjranje, treba da promeni u True
        while camera == True:
            success, frame = cap.read()
            #print(f"uspešnost: {success}, frejm: {frame}")
            for code in decode(frame):
                # print(code.data.decode("UTF8"))
                txt = code.data.decode("UTF8")
                x = txt.split("-")
                kvar_id, opis_kvara = x[0], x[1]
                print(f"{kvar_id=}")
                print(f"{opis_kvara=}")
                time.sleep(1)
                if kvar_id != 0:
                    return kvar_id, opis_kvara

            cv2.imshow("Testing KVAR ID scan", frame)
            cv2.waitKey(20)
