from sys import stdout
from time import sleep


def slow_print(string:str, speed:float=0.01):
    for letter in string:
        stdout.write(letter)
        sleep(.1)