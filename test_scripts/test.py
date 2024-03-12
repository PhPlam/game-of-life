import random

import librosa
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import numpy as np

set_of_tuples = {(1, 2, 3), (4, 5, 6), (7, 8, 9), (120, 12, 23)}
num = 1
[set_of_tuples.pop() for num in range(num)]
print(set_of_tuples)
# Transpose the set of tuples
#transposed_tuples = zip(*set_of_tuples)

# Calculate the element-wise average
#average_tuple = tuple(sum(column) / len(set_of_tuples) for column in transposed_tuples)

#print("Element-wise average tuple:", average_tuple)

'''
y, sr = librosa.load('test_audio/lofi_no_copyright.mp3')#, duration=5)
o_env = librosa.onset.onset_strength(y=y, sr=sr)
times = librosa.times_like(o_env, sr=sr)
onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
onset_sample = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, units='samples')
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

#print(onset_frames)
#print(times[onset_frames])
#print(onset_sample)
print(times[beats])
print(tempo)
print(round(3.9, 0))

# plot results
fig, ax = plt.subplots(figsize=(12, 5))
plt.plot(times, o_env, label='Onset strength')
plt.vlines(times[onset_frames], 0, o_env.max(), color='r', alpha=0.9, linestyle='--', label='Onsets')
plt.legend()
plt.savefig('analysis_results/analysis_track_1.png')
'''