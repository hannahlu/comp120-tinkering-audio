import wave
import struct
import math
import sys
import pygame
from pygame.locals import *


pygame.init()
pygame.mixer.init()
Clock = pygame.time.Clock()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Audio')
window.fill((255, 255, 255))

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
for i in range(SAMPLE_LENGTH):
    value = math.sin(2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE)) * (VOLUME * BIT_DEPTH)
    packedValue = struct.pack('h', value)
    soundFile.writeframes(packedValue)
    soundFile.writeframes(packedValue)

while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_p:
            sound = wave.open("puretone.wav")
            sound.play()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            soundFile.close()

    pygame.display.update()
    Clock.tick(500)


soundFile.close()

