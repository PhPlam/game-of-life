import wave
import pyaudio
import numpy as np
import wavio
import time
import sys

#a = np.arange(4).reshape((2,2))
#print(a)
#print(np.max(a[[0,1]]))
#sys.exit()

# open wave in read-only mode
file_name = 'test_audio/drums_30s.wav'
wf = wave.open(file_name, 'rb')

channels = wf.getnchannels()
bytes_per_sample = wf.getsampwidth()
fs = wf.getframerate()

# create pyaudio object
p = pyaudio.PyAudio()


def beat_detect(data):
    audio = wavio._wav2array(channels, bytes_per_sample, data)
    audio_fft = np.abs((np.fft.fft(audio)[0:int(len(audio) / 2)]) / len(audio))
    freqs = fs * np.arange(len(audio) / 2) / len(audio)

    midrange_indices = [idx for idx, val in enumerate(freqs) if 250 <= val <= 2000]
    if midrange_indices:
        midrange = np.max(audio_fft[midrange_indices])
        #print(midrange)

        midrange_max = 10
        midrange_beat = False

        midrange_max = max(midrange_max, midrange)
        #print(midrange_max)

        if midrange >= midrange_max * .9 and not midrange_beat:
            midrange_beat = True
            print("Midrange Beat")
        elif midrange >= midrange_max * .3:
            midrange_beat = False

        #print(midrange_beat)


def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    beat_detect(data)
    return (data, pyaudio.paContinue)


def main():
    stream = p.open(format=p.get_format_from_width(bytes_per_sample),
                    channels=channels,
                    rate=fs,
                    output=True,
                    stream_callback=callback)


    while stream.is_active():
        time.sleep(1) # default 0.1
        sys.exit()

    stream.close()
    p.terminate()


if __name__ == '__main__':
    main()
