# Converts data in a 2 dimensional array to an audio (wav) file
# by Kai Staats, MSc AIMS / UCT 2014-15

import numpy as np
from sys import *
from pylab import *
from scipy.io.wavfile import write

print ''
# open file and establish parameters
filename = raw_input('Open File (sample_data.npy): '); filename = filename or "sample_data.npy"
data = np.load(filename)
data_col = data.shape[0] # images
data_row = data.shape[1] # channels

print ''
print "There are %d radio channels in this data set." % data_row
chan_start = raw_input('Starting channel (default 0): '); chan_start = chan_start or 0.0; chan_start = float(chan_start)
channels = raw_input('Number of channels (default 1): '); channels = channels or 1.0; channels = float(channels)
chan_stop = chan_start + channels

dur = raw_input('Length of the .wav file? (default 10 second) '); dur = dur or 10.0; dur = float(dur)
hz = raw_input('Output Hertz of audio file? (default 44,100) '); hz = hz or 44100.0; hz = float(hz)
amp = raw_input('By how much would you like to amplify the volume? (default 1 x; decimals ok) '); amp = amp or 1.0; amp = float(amp)
function = raw_input('Do you desire to (a)ppend or (s)tack the channels? (default s) '); function = function or 's'

# If user selects 'append', the channels will follow each other, one after the other for the duration of the .wav
if function == 'a':
	stems = float((hz * dur) / data_col / channels)

# If user selects 'stack', the channels will be layered onto the same duration, creating a compound wave form
else:
	stems = float((hz * dur) / data_col)

chan_count = int(chan_start)
data_total = 0

# loop through all channels
while chan_count < chan_stop:

	# copy all images (columns) of 1 channel (row) to a temp, one-dimensional array
	data_per_chan = data[:,chan_count]
	data_fill = np.repeat(data_per_chan,stems) # rounds down to 44,000, not 44,100 -- NEED TO FIX!

	# (a)ppend or (s)tack the channels (channels)
	if function == 'a':
		data_total = np.append(data_total,data_fill * amp) # Why had I introduced (... * amp - 1) here?

	else:
		data_total = data_total + (data_fill * amp)

	print "Processing channel %d " % chan_count

	# increment the channel
	chan_count = chan_count + 1

# modify the name of the file to be saved
namesplit = filename.split('.')
filename_wav = namesplit[0] + ".wav"

# write the wav file
write(filename_wav, hz, np.abs(data_total))

print ''
print "The wav file %s has been generated." % filename_wav

# plot the graph of the original data, for the given row
plot(np.abs(data_total))
show()
