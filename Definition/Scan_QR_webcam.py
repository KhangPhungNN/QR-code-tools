import cv2
camera = cv2.VideoCapture(2)
while True:
    ret,frame = camera.read()
    cv2.imshow("QR",frame)
    k = cv2.waitKey(1)
    if(k==113):
        break
rQR = cv2.QRCodeDetector()
v = rQR.detectAndDecode(frame)
print("Noi dung: ",v[0])
camera.release()
cv2.destroyAllWindows()