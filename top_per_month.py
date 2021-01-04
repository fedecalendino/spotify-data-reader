from collections import Counter
from reader import streaming_history

YEAR = 2020

counters = {}

for item in streaming_history():
    if item.timestamp.year != YEAR:
        continue

    month = item.timestamp.strftime("%B")

    if month not in counters:
        counters[month] = Counter()

    counters[month].update([(item.artist, item.track)])


for month, counter in counters.items():
    print(f"{month}:")

    for (artist, track), count in counter.most_common(10):
        print(f" * {track} by {artist} ({count})")

    print()
