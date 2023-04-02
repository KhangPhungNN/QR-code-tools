###     ###
# Imports #
###     ###

import os
import qrcode
import cv2
import webbrowser
import validators
from colored import *
from PIL import Image
from pip._vendor.distlib.compat import raw_input
import pyzbar.pyzbar as pyzbar

# Clear screen
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

# Enter to exit -> Exit
def Raw_Input():
    raw_input(fg("green") + "\n Press enter key to exit." + attr('reset'))



# QR code to text
def Convert_QR_to_text():
    try:
        print("")
        Input_CQTT = input(fg("green") + "Drag file here: " + attr('reset')); print (os.getcwd())
        # Decode the QR code
        Decode = pyzbar.decode(Image.open(Input_CQTT))
        text = Decode[0].data.decode('utf-8')

        print(fg('green') + "Output: " + attr('reset') + text)
        Raw_Input()
    # If file not found
    except FileNotFoundError:
        print(fg("red") + "Failed to detect! File not found!" +  attr('reset')); Convert_QR_to_text()

# Text to QR code
def Convert_text_to_QR():
    try:
        print("")
        data = input(fg("yellow") + "Enter the data will be converted: " + attr('reset')) 
        name = str(input(fg("yellow") + "Enter the name of the file: " + attr('reset'))) 
        img = qrcode.make(data) # Convert QR code
        img.save(name + ".jpg")
        print(fg("green") + "File was successfully converted! File name: ", name + ".jpg" + attr("reset"))
        show_img = Image.open(name + ".jpg").show(); Raw_Input()
    # If file name error
    except OSError:
        print(fg("red") + "Error! Please, Rename the file" + attr('reset')); Convert_text_to_QR()

# Scan QR code with camera
def QR_code_scanner():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            data = obj.data.decode("utf-8")
            # If found the URL on data in QR code
            if validators.url(data):
                print(f"Found URL: {data}")
                choice = input("Do you want to open this URL? (y/n): ")
                if choice.lower() == 'y':
                    webbrowser.open(data)
            else:
                print(data)

        cv2.imshow("QR code scanner", frame)
        key = cv2.waitKey(1)
        # Exit the scanner
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


###      ###
#   Main   #
###      ###

def main():
        
    def MENU():
        clrscr() # Clear the screen
        # Print "-"
        def Print():
            print(fg('pale_green_1a') + "-" * 95 + attr('reset'))
        # Create menu items with colors and elements
        menu_items = [
            ("green", "1. Convert QR code to text"),
            ("yellow", "2. Convert text to QR code"),
            ("cyan", "3. QR code scanner"),
            ("red", "4. Exit"),
            ("", " " * 95),
            ("blue", "0. View error code".rjust(95))
        ]
        # Print menu
        Print()
        for color, item in menu_items:
            if color:
                print(fg(color) + item + attr('reset'))
            else:
                print (item)
        Print()
    
    def Print_Error():
        clrscr() # Clear the screen
        # Print the "-" characters in pale green
        def print_colored_lines():
            print(fg('pale_green_1a') + "-" * 95 + attr('reset'))
        # Create a list of lines of text
        lines = [
        "AA00001: In main program, integers other than the given ones.",
        "AA00002: In main program, string and not integer. (ValueError)",
        "AA00003: In main program, press ctrl + c. (KeyboardInterrupt)"
        ]
        # Print each line of text
        print_colored_lines()
        for line in lines:
            left, right = line.split(":")
            print(fg('red') + left + fg('white') + ":" + right + attr('reset'))
        # Enter key to return to menu
        Raw_Input()
        clrscr() # Clear the screen

    def Condition():
        try:
            # Create a list of color codes for blue, green, yellow, and cyan
            colors = [fg('blue'), fg('green'), fg('yellow'), fg('cyan')]
            # Create a string of options by joining the color codes with their index
            options = ' , '.join(colors[i] + str(i) + attr('reset') for i in range(4))

            Input = int(input(f"Choose [{options} ({fg('red')}4{attr('reset')} to exit)]:"))

            if Input == 1:
                Convert_QR_to_text()
            elif Input == 2:
                Convert_text_to_QR()
            elif Input == 3:
                QR_code_scanner()
            elif Input == 4:
                exit()
            elif Input == 0:
                Print_Error()
                MENU()
                Condition()
            else:
                print(fg('red') + "Error! (code: AA00001)" + attr('reset')); Condition()
        
        # If Error
        except ValueError:
            print(fg('red') + "Error! (code:AA00002)" + attr('reset')); Condition()
        except KeyboardInterrupt:
            print(fg('red') + "Error! (code:AA00003)" + attr('reset'))
    
    clrscr() # Clear the screen
    MENU()
    Condition()


if __name__ == "__main__":
    main()