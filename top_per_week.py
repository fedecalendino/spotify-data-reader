from collections import Counter
from reader import streaming_history

YEAR = 2020

counters = {w: Counter() for w in range(1, 54)}

for item in streaming_history():
    if item.timestamp.year != YEAR:
        continue

    week = item.timestamp.isocalendar()[1]
    counters[week].update([(item.artist, item.track)])


for week, counter in counters.items():
    print(f"Week {week}:")

    for (artist, track), count in counter.most_common(2):
        print(f" * {track} by {artist} > ({count})")

    print()
