import wave
import struct

sheep = wave.open("sheep.wav", "r")
soundFile = wave.open('sheepEcho.wav', 'w')

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

def delay():
    sound1 = sheep
    sound2 = soundFile
    for i in range(0, SAMPLE_LENGTH):
        echo = 0.75
        sound2 += echo
        packedValue = struct.pack("<h", sound2)
        soundFile.writeframes()

def echo(delay, sound):


unpack()
delay()
soundFile.close()