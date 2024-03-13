import random

import librosa
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import numpy as np

a  = {(93, 11): (16, 180, 0), (94, 9): (16, 181, 0), (93, 12): (17, 179, 0), (94, 10): (16, 180, 0), (94, 12): (17, 179, 0), (92, 10): (15, 181, 0), (95, 10): (17, 179, 0), (92, 9): (15, 181, 0), (93, 10): (17, 179, 0), (95, 9): (16, 180, 0), (93, 9): (16, 181, 0), (95, 11): (17, 179, 0), (92, 11): (15, 181, 0), (94, 11): (16, 181, 0), (95, 12): (17, 179, 0), (92, 12): [(16, 180, 0)]}


print(len(a))

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