import sounddevice
import librosa
import numpy
import json

with open("Intervals.json") as file:
    intervals = json.load(file)

class Player:

    player = None

    def __new__(cls, *args):
        cls.stop()
        cls.player = super().__new__(cls)
        return cls.player

    def __init__(self, process):
        self.note = 0.0
        def detect(input, frames, time, status):
            previous = self.note
            frequencies = librosa.pyin(input.T, fmin=50, fmax=500, sr=44100)[0]
            if numpy.count_nonzero(numpy.isnan(frequencies)) <= 2:
                self.note = numpy.nanmean(frequencies)
            ratio = self.note / previous if previous != 0.0 else 1.0
            distance = lambda interval: abs(numpy.log2(ratio) - numpy.log2(interval[1]))
            name = min(intervals.items(), key=distance)[0]
            process(self.note, ratio, name)
        self.stream = sounddevice.InputStream(callback=detect, samplerate=44100, blocksize=8820)
        self.stream.start()

    @classmethod
    def stop(cls):
        if cls.player is not None:
            cls.player.stream.close()
