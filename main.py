import wave
import struct
import winsound
import math
import sys
import time
import numpy
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
Clock = pygame.time.Clock()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Audio')
font = pygame.font.SysFont("Courier", 50)
textColour = (255, 255, 255)
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
value = []
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
        packedValue = struct.pack('<h', value)
        soundFile.writeframes(packedValue)

def text():
    x = 50
    y = 100
    label = font.render("Generating Pure Tone...", 1, textColour)
    window.blit(label, (x, y))

def text2():
    x = 50
    y = 100
    label = font.render("Increasing volume...", 1, textColour)
    window.blit(label, (x, y))

while True:
    pressed = pygame.key.get_pressed()
    timer = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if timer == 0:
        window.fill(BLACK)
        text()
        pygame.display.update()
        time.sleep(1)
        timer = timer + 1
    if timer == 1:
        window.fill(RED)
        puretone()
        pygame.display.update()
        winsound.PlaySound("puretone.wav", winsound.SND_FILENAME)
        timer = timer + 1
    if timer == 2:
        window.fill(BLACK)
        pygame.display.update()
        winsound.PlaySound("None", 1)
        timer = timer + 1
    if timer == 3:
        text2()
        pygame.display.update()
        time.sleep(1)
        timer = timer + 1
    if timer == 4:
        window.fill(RED)
    if event.type == KEYDOWN and event.key == K_ESCAPE:
        soundFile.close()
    else:
        sys.exit()

    pygame.display.update()
    Clock.tick(500)

winsound.PlaySound(None, winsound.SND_FILENAME)
soundFile.close()