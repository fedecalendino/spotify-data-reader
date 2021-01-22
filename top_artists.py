from collections import Counter
from reader import streaming_history

YEAR = 2020

artists = []

for item in streaming_history():
    if item.timestamp.year != YEAR:
        continue

    artists.append(item.artist)


for artist, counter in Counter(artists).most_common(10):
    print(f"{artist} [{counter}]")
