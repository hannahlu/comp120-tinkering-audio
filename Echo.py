import wave
import struct
import math
import matlab



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
def unpack():
    for i in range(0, FRAMES):
        waveData = soundFile.readframes(1)
        data = struct.unpack("<h", waveData)
        print(int(data[0]))

'''Generate Echo'''
def echo(delay):
    valeSong  = wave.open("vale.wav", "r")
    soundFile = wave.open('echo.wav', 'w')
    delay = 0.5
    valeSong =
    soundFile =



unpack()
echo()
