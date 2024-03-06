import matplotlib.pyplot as plt
import librosa.display
import librosa

audio = 'test_audio/drums_30s.wav'

y, sr = librosa.load(audio, duration=10)
fig, ax = librosa.display.waveshow(y, sr=sr)