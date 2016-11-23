import pygame, sys, time, random
import wave
from pygame.locals import*

# Set up pygame
pygame.init()
Clock = pygame.time.Clock()

# Set up window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Audio')

# Set up sound
sound = wave.open("noise2.wav")



# Set up game loop
while True:
    for event in pygame.event.get():
        pygame.quit()
        sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_s:
            play(sound)

    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()