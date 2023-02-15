import sounddevice
import librosa
import numpy
import json

with open("Intervals.json") as file:
    intervals = json.load(file)

def start(process):
    def detect(input, frames, time, status):
        note = detect.note
        frequencies = librosa.pyin(input.T, fmin=50, fmax=500, sr=44100)[0]
        if numpy.count_nonzero(numpy.isnan(frequencies)) <= 2:
            detect.note = numpy.nanmean(frequencies)
        ratio = detect.note / note if note != 0 else 1
        distance = lambda interval: abs(numpy.log2(ratio) - numpy.log2(interval[1]))
        name = min(intervals.items(), key=distance)[0]
        process(detect.note, ratio, name)
    detect.note = 0
    stream = sounddevice.InputStream(callback=detect, samplerate=44100, blocksize=8820)
    stream.start()
