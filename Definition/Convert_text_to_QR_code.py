#Convert text to QR code (v.1)
import qrcode
from PIL import Image
data = input("Enter the data to be converted: ")
name = input("Enter the name of the file: ")
img = qrcode.make(data)
img.save(name+".jpg")
f = Image.open(name+".jpg").show()