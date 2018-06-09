import midi
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description="Turn a .midi file into a graph")
parser.add_argument('midi_file', help='Path to .midi file to process')

args = parser.parse_args()

song = midi.read_midifile(args.midi_file)
song.make_ticks_abs()
tracks = []
# for track in song:
for i in range(1,len(song)):
    track = song[i]
    notes = [note for note in track if note.name == 'Note On']
    pitch = [note.pitch for note in notes]
    tick = [note.tick for note in notes]
    # tracks += [tick, pitch]
    plt.step(tick,pitch)
plt.show()
