# Animation attempt :((
from msvcrt import getch, putwch, kbhit
from time import sleep
delay = 0.1
string = ""

animation_frames = [
"ooo\nooo\nooo",
"---\nooo\nooo",
"---\n---\nooo",
"---\n---\n---",
"ooo\n---\n---",
"ooo\nooo\n---"
    ]

current_frame = 0
max_frame = len(animation_frames) - 1


def clear():
    print("\n" * 1000)

while True:
    clear()
    print(animation_frames[current_frame])
    print(string)
    if kbhit():
        key = getch()
        # Backspace : b'\x08' Enter: b'\r'
        if key == b'\r':
            string = ""
        elif key == b'\x08':
            string = string[0:len(string)-1]
        else:
            string += key.decode("utf-8")
    sleep(delay)
    current_frame = current_frame + 1 if not current_frame == max_frame else 0

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
