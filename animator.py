# Animation attempt :((
from msvcrt import getch, putwch
from time import sleep
delay = 0.1
string = ""

def clear():
    print("\n" * 1000)

while True:
    keypress = getch()
    if keypress.decode("utf-8") == "\r":
        clear()
    putwch(keypress.decode("utf-8"))

##while True:
##    clear()
##    sleep(delay)
##    print("INPUT CHARACTERS:")
##    print(string)
##    keypress = getch()
##    if keypress == bin(13):
##        print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
##        string = ""
##    else:
##        x = keypress.decode("utf-8")
##        string += x
    
input()
