from pyzbar.pyzbar import decode
from PIL import Image
from colored import *

Input = input(fg("green")+"Enter file name: "+attr('reset'))
Decode = decode(Image.open(Input))
text = Decode[0].data.decode('utf-8')

print(fg('green')+"Output: "+attr('reset')+text)
