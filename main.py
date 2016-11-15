import pygame, sys, time, random
from pygame.locals import*

# Set up pygame
pygame.init()
Clock = pygame.time.Clock()

# Set up window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Audio')

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up sound
sound = pygame.mixer.Sound('noise2.wav') # For importing sound effect
# pygame.mixer.load('') # For importing background music
# pygame.mixer.music.play(-1, 0.0) # Sets point in sound file to start playing from
musicPlaying = True

# Set up game loop
while True:
    for event in pygame.event.get():
        pygame.quit()
        sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_s:
                play(sound)
        #if event.key == ord('m'):
            #if musicPlaying:
                #pygame.mixer.music.stop()
            #else:
                #pygame.mixer.music.play(-1, 0.0)
           # musicPlaying = not musicPlaying
