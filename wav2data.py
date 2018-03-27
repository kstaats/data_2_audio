# Converts an audio (wav) file to a 2 dimensional array
# by Kai Staats, MSc AIMS / UCT 2014-15; built from original by Laura

import numpy as np
import matplotlib.pylab as plt
from sys import *
from pylab import *
from scipy.io import wavfile


print ''
# open wav file
filename = raw_input('Open File (sample_data.wav): '); filename = filename or "sample_data.wav"
data = wavfile.read(filename)

# data = np.load(filename)
# data_col = data.shape[0] # images
# data_row = data.shape[1] # channels

hz = float(data[0]) # 1st component of wav file: total number of images
data_col = data[1] # 2nd component of wav file; data
time = np.arange(len(data_col)) / hz # images / hz = time

plt.subplot(211)
plt.plot(time,data_col)
plt.xlabel('time / [s]')
plt.ylabel('wav amplitude')

plt.show()


# generate the FFT
# data_fft = np.fft.fft(data_col)
# freq = np.fft.fftfreq(len(data_col),d=1. / hz)
# f0 = 146.8 # freq of the note "D"
#
# plt.subplot(212)
# plt.plot(freq/f0,abs(data_fft))
# plt.xlabel('freq / f0')
# plt.ylabel('wav fourier components')
