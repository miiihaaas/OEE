import cv2
from pyzbar.pyzbar import decode

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
