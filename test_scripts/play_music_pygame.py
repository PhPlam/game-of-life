from pygame import mixer
import pygame
import librosa

# Starting the mixer
mixer.init()

# Loading the song
audio = "test_audio/doiwannaknow.mp3"
mixer.music.load(audio)
mixer.music.play()

def detect_onset(audio):
    y, sr = librosa.load(audio)
    o_env = librosa.onset.onset_strength(y=y, sr=sr)
    times = librosa.times_like(o_env, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
    onset_frames = [round(x, 1) for x in times[onset_frames]]
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beats = [round(x, 2 ) for x in times[beats]]
    return beats

onset = detect_onset(audio)
print(onset)
stream_time = 0
i = 0
while True:
    last_stream_time = stream_time
    stream_time = round(pygame.mixer.music.get_pos()/1000, 2)
    if stream_time > last_stream_time and stream_time in onset:
        print('now:', stream_time, ' before:', last_stream_time)
        #print('now', i)
