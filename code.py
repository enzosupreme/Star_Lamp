import board
import time
import neopixel
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer
from colorpallette import colors
import random


a = DigitalInOut(board.A3)
a.direction = Direction.INPUT
a.pull = Pull.UP

numpix = 8
pixpin = board.A2

ORDER = neopixel.GRB

col =[
    colors.CYBER,
    colors.MINT,
    colors.GREEN,
    colors.BLUE,
    colors.NEON,
    colors.MAGENTA,
    colors.CYAN,
    colors.PEACH,
    colors.ORANGE,
    colors.RORANGE,
    colors.WHITE,

]
pixels = neopixel.NeoPixel(pixpin, numpix, brightness=1, auto_write=False,pixel_order = ORDER)

def rando_fill():
    l = len(pixels)
    c = len(col)
    r = random.randint(0,(c-1))

    for i in range(l):
        r2 = random.randint(0,(c-1))
        pixels[i] = col[r]
        pixels.show()
        time.sleep(0.08)

def eraser():
    l = len(pixels)
    for i in range (l):
        pixels[i] = 0
        pixels.show()
        time.sleep(0.08)

def demo(number):
    if number is 0:
        l = len(pixels)
        c = len(col)
        r = random.randint(0,(c-1))
        for i in range(l):
            r2 = random.randint(0,(c-1))
            pixels[i] = col[r]
            pixels.show()
            time.sleep(0.08)
    elif number is 1:
        l = len(pixels)
        for i in range (l):
            pixels[i] = 0
            pixels.show()
            time.sleep(0.08)
status = False

while True:
    old_status = status
    if old_status is False:
        if not a.value:
            rando_fill()
            time.sleep(0.2)
            status = True
    if old_status is True:
        if not a.value:
            eraser()
            time.sleep(0.2)
            status = False
    while not a.value:
        rando_fill()

    """rando_fill()

    time.sleep(2)
    eraser()"""
    old_status = status
    time.sleep(0.2)




# Write your code here :-)
