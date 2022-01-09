import os
import time

print("Download module to startup") ; os.system('python -m pip install --upgrade pip') ; os.system('pip install colored') ; os.system('cls' if os.name == 'nt' else 'clear')

from colored import *

def check_modules():
    def check_py():
        os.system('python -V')
    def check_pip():
        os.system('pip -V')
    print(fg('light_sky_blue_3b')+"Checking module ..."+attr('reset'))
    print(fg('light_sky_blue_3b')+"Current pip version: "+attr('reset'))
    check_pip()
    print(fg('light_sky_blue_3b')+"Current python version: "+attr('reset'))
    check_py()
    print(fg('light_sky_blue_3b')+"Download the necessary modules: "+attr('reset'))
    os.system('pip install qrcode')
    os.system('pip install pyzbar')
    os.system('pip install distlib')
    os.system('pip install pillow')
    print(fg('green')+"Checking module finish !"+attr('reset'),"\n"); print (fg('green')+"Welcome to my programme !"+ attr('reset'))
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
check_modules()

import qrcode
from PIL import Image
from pip._vendor.distlib.compat import raw_input
from pyzbar.pyzbar import *

def Raw_Input():
    raw_input(fg("green")+"\nPress enter key to exit."+attr('reset'))

def Convert_QR_to_text(): #1
    try:
        print("")
        Input_CQTT = input(fg("green")+"Enter file name: "+attr('reset'))
        Decode = decode(Image.open(Input_CQTT))
        text = Decode[0].data.decode('utf-8')

        print(fg('green')+"Output: "+attr('reset')+text)
    except FileNotFoundError:
        print(fg("red")+"Failed to detect! File not found! (code:AB00001) Enter:'Back::to::Main' to back to main program"+ attr('reset')) ; Convert_QR_to_text()
    # except TypeError:
    #     print(fg("red")+"Type Error! File not found! (code: AB00002)"+attr('reset'))

def Convert_text_to_QR(): #2
    try:
        print("")
        data = input(fg("yellow")+"Enter the data will be converted: "+attr('reset'))
        name = str(input(fg("yellow")+"Enter the name of the file: "+attr('reset')))
        img = qrcode.make(data)
        img.save(name+".jpg")
        print(fg("green")+"File was successfully converted! File name: ",name+".jpg"+attr("reset"))
        show_img = Image.open(name+".jpg").show();Raw_Input()
    except OSError:
        print(fg("red")+"Error! Please, Rename the file (code:AC00001)"+ attr('reset')) ; Convert_text_to_QR()

def main():
    def timesleep():
        time.sleep(0.08)
    def Print():
        for i in range(1,49):
            print(fg('pale_green_1a')+"*"+attr('reset'),end=" ")
        timesleep()
    def Print_star():
        print(fg('pale_green_1a')+"*"+attr('reset'),end=" ")
    def Print_star_no_end():
        print(fg('pale_green_1a')+"*"+attr('reset'))
    Print()
    print("")
    Print_star(); print(fg('green' )+"1. Convert QR code to text                                                                 "+ attr('reset'),end=" "); Print_star_no_end(); timesleep()
    Print_star(); print(fg('yellow')+"2. Convert text to QR code                                                                 "+ attr('reset'),end=" "); Print_star_no_end(); timesleep()
    Print_star(); print(fg('red'   )+"3. Exit                                                                                    "+ attr('reset'),end=" "); Print_star_no_end(); timesleep()
    Print_star(); print(             "                                                                                           "               ,end=" "); Print_star_no_end(); timesleep()
    Print_star(); print(fg('blue'  )+"                                                                         0. View error code"+ attr('reset'),end=" "); Print_star_no_end(); timesleep()
    Print()
    print("")
    def Condition():
        try:
            print("Choose [",fg('blue')+"0"+ attr('reset'),",",end="");print(fg("green")+" 1"+attr('reset'),", ",end="");print(fg('yellow')+"2"+attr('reset'),end="");print(" (",end="");print(fg('red')+"3"+attr('reset'),end="");print(" to exit) ]: ",end="");Input = int(input())
            if Input == 1:
                Convert_QR_to_text()
            elif Input == 2:
                Convert_text_to_QR()
            elif Input == 3:
                os.system('exit')
            elif Input == 0:
                os.startfile("Data\\All_error_code.txt")
                Condition()
            elif Input == "Exit::":
                os.system('exit')
            else:
                print(fg('red')+"Error! (code: AA00001)"+attr('reset')) ; Condition()
        except ValueError:
            print(fg('red')+"Error! (code:AA00002)"+attr('reset')) ; Condition()
        except KeyboardInterrupt:
            print(fg('red')+"Error! (code:AA00003)"+attr('reset'))
    Condition()

if __name__ == "__main__":
    main()






