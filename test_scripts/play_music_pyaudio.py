import wave
import pyaudio
import time
import librosa

# open wave in read-only mode
file_name = 'test_audio/drums_30s.wav'
wf = wave.open(file_name, 'rb')
# create pyaudio object
p = pyaudio.PyAudio()

def detect_onset(audio):
    y, sr = librosa.load(audio)
    o_env = librosa.onset.onset_strength(y=y, sr=sr)
    times = librosa.times_like(o_env, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
    onset_frames = [round(x, 2) for x in times[onset_frames]]
    return onset_frames


def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return data, pyaudio.paContinue


def main():
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    sleep_timer = 0.01

    while stream.is_active():
        time.sleep(sleep_timer)

    stream.close()
    p.terminate()


if __name__ == '__main__':
    main()
