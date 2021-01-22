from collections import Counter
from reader import streaming_history

YEAR = 2020

tracks = []

for item in streaming_history():
    if item.timestamp.year != YEAR:
        continue

    tracks.append((item.track, item.artist))


for (track, artist), counter in Counter(tracks).most_common(20):
    print(f"{track} by {artist} [{counter}]")
