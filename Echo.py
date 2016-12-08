import wave
import struct
import math

soundFile = ('vale.wav', 'w')

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
def echo():
    soundFile = ("vale.wav", "w")
    soundFile2 = ("vale.wav", "w")
    delay = 0.5
    for index in range(delay, len(soundFile)):
        echo = 0.5*soundFile2[index-delay]
        soundFile[index] += echo
        packedValue = struct.pack("<h", soundFile[index])
        soundFile.writeframes(packedValue)

unpack()
echo()
soundFile.close()