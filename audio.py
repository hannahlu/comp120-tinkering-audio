import wave
import math
import struct
import pygame
from pygame import*

pygame.init()

Clock = pygame.time.Clock()

noise_out = wave.open('noise2.wav', 'w')
noise_out.setparams((2, 2, 44100, 44100*10, 'NONE', 'not compressed'))

values = []

SAMPLE_LENGTH = 44100*10
SAMPLE_RATE = 220
SAMPLE_WIDTH = float(44100)
FREQUENCY = 1
VOLUME = 1
BIT_DEPTH = 705
CHANNELS = 2
timer = 0

for i in range(0, SAMPLE_LENGTH):
    timer += 0

    value = math.sin(
        2.0*math.pi*FREQUENCY*(i/SAMPLE_RATE))*(VOLUME*BIT_DEPTH)

    packaged_value = struct.pack("<H", value)

    for j in xrange(0, CHANNELS):
        values.append(packaged_value)

    value_str = ".join(values)"

    noise_out.close()

# Set up game loop
while True:
    for event in pygame.event.get():
        pygame.quit()
        sys.exit()

    pygame.display.update()
    Clock.tick(200)

pygame.quit()
quit()