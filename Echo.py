import sys
import wave
import math
import struct
import random


soundFile = wave.open('rubber_biscuit.wav', 'w')


def packfile():

    values = []
    SAMPLE_LENGTH = 44100 * 8
    SAMPLE_RATE = float(44100)
    VOLUME = 1
    BIT_DEPTH = 32767
    CHANNELS = 2
    timer = 0
    FREQUENCY = 560
    FRAMES = []

    for i in range(44100):
        value = math.sin(2.0 * math.pi * FREQUENCY * (i/44100.0)) * (0.5 * (2**15-1))
        pack = struct.pack("<h", value)
        FREQUENCY += 1

        for j in range (0, 1):
            values.append(pack)

def unpackfile():
    wave_packed = soundFile.readframes(1)
    unpack = struct.unpack("<h", wave_packed)
    FRAMES.append(int(unpack[0]))

def echo():
    values = []
    channels = 1
