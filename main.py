import wave
import struct
import winsound
import math
import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
Clock = pygame.time.Clock()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Audio')
font = pygame.font.SysFont("Courier", 50)
textColour = (0, 0, 0)
window.fill(WHITE)

soundFile = wave.open('puretone.wav', 'w')

# Set up params
soundFile.setparams((2, 2, 44100, 44100*8, 'NONE', 'not compressed'))
FRAMES = soundFile.getnframes()
SAMPLE_LENGTH = 44100*8
FREQUENCY = 220
SAMPLE_RATE = float(44100)
VOLUME = 1
BIT_DEPTH = 32767
CHANNELS = 2
TIMER = 0
params = soundFile.getparams()

'''Unpack wav file'''
for i in range(0, FRAMES):
    waveData = soundFile.readframes(1)
    data = struct.unpack("<h", waveData)
    print(int(data[0]))

'''Generate Pure Tone'''
def puretone():
    for i in range(SAMPLE_LENGTH):
        value = math.sin(2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE)) * (VOLUME * BIT_DEPTH)
        packedValue = struct.pack('h', value)
        soundFile.writeframes(packedValue)

"""Make background red"""
def makered():
    for Y in range(0, WINDOW_HEIGHT):
        for X in range(0, WINDOW_WIDTH):

            RED = window.get_at((X, Y)).r
            GREEN = window.get_at((X, Y)).g
            BLUE = window.get_at((X, Y)).b

            RED = 255
            GREEN = 255 - GREEN
            BLUE = 255 - BLUE

            PXArray[X, Y] = (RED, GREEN, BLUE)

"""Make background green"""
def makegreen():
    for Y in range(0, WINDOW_HEIGHT):
        for X in range(0, WINDOW_WIDTH):

            RED = window.get_at((X, Y)).r
            GREEN = window.get_at((X, Y)).g
            BLUE = window.get_at((X, Y)).b

            RED = 255 - RED
            GREEN = 255
            BLUE = 255 - BLUE

            PXArray[X, Y] = (RED, GREEN, BLUE)

def text():
    x = 50
    y = 100
    label = font.render("Generating Pure Tone...", 1, textColour)
    window.blit(label, (x, y))

def text2():
    x = 50
    y = 100
    label = font.render("Generating White Noise", 1, textColour)
    window.blit(label, (x, y))

while True:
    pressed = pygame.key.get_pressed()
    timer = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if timer == 0:
        print("Generating Pure Tone")
        text()
        PXArray = pygame.PixelArray(window)
        makered()
        pygame.display.update()
        del PXArray
        timer = timer + 1
    if timer == 1:
        puretone()
        winsound.PlaySound("puretone.wav", winsound.SND_FILENAME)
        timer = timer + 1
    if timer == 2:
        window.fill(WHITE)
        winsound.PlaySound("None", 1)
        timer = timer + 1
    if timer == 3:
        text2()
        PXArray = pygame.PixelArray(window)
        makegreen()
        pygame.display.update()
        del PXArray
        timer = timer + 1
    if timer == 4:
        window.fill(WHITE)
        winsound.PlaySound("whitenoise.wav", winsound.SND_FILENAME)
        timer = timer + 1
    if event.type == KEYDOWN and event.key == K_ESCAPE:
        soundFile.close()

    pygame.display.update()
    Clock.tick(500)

winsound.PlaySound(None, winsound.SND_FILENAME)
soundFile.close()