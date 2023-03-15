import sounddevice
import soundfile
import librosa
import numpy
import json

with open("Tones.json") as file:
    tones = json.load(file)

class Player:

    player = None

    def __new__(cls, *args):
        cls.stop()
        cls.player = super().__new__(cls)
        return cls.player

    def __init__(self, process, duration, fundamental, volume):
        strings, samplerate = soundfile.read("Strings.wav")
        frequency = numpy.nanmean(librosa.pyin(strings.T.sum(0), fmin=50, fmax=1000, sr=samplerate)[0])
        minimum = min(tones.values()) * fundamental
        maximum = max(tones.values()) * fundamental
        window = int(5 * samplerate / minimum)
        self.tone = None
        self.position = 0
        def play(input, output, frames, time, status):
            end = self.position + int(frames * fundamental / frequency)
            samples = numpy.linspace(self.position, end, frames, False).astype(int) % strings.shape[0]
            self.position = end % strings.shape[0]
            output[:] = strings[samples] * volume / 100
            frequencies = librosa.pyin(input.T.sum(0), fmin=minimum, fmax=maximum, sr=samplerate, frame_length=window)[0]
            if numpy.count_nonzero(numpy.isnan(frequencies)) <= 1:
                note = numpy.nanmean(frequencies)
                ratio = note / fundamental
                distance = lambda tone: abs(numpy.log2(ratio) - numpy.log2(tone[1]))
                tone = min(tones.items(), key=distance)[0]
                if tone != self.tone:
                    process(note, tone)
                    self.tone = tone
            else:
                self.tone = None
        self.stream = sounddevice.Stream(callback=play, blocksize=int(duration * samplerate))
        self.stream.start()

    @classmethod
    def stop(cls):
        if cls.player is not None:
            cls.player.stream.close()
