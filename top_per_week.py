from collections import Counter
from reader import streaming_history

YEAR = 2020

counters = {w: Counter() for w in range(1, 53)}

for item in streaming_history():
    if item.artist == "Unknown Artist":
        continue

    if item.track == "Unknown Track":
        continue

    if item.timestamp.year != YEAR:
        continue

    week = item.timestamp.isocalendar()[1]
    counters[week].update([(item.artist, item.track)])


for week, counter in counters.items():
    print(f"Week {week}:")

    for (artist, track), count in counter.most_common(3):
        print(f" * {track} by {artist} > played {count} times")

    print()


"""
Output:

Week 1:
 * Submission (feat. Danny Brown & Kelela) by Gorillaz > played 25 times
 * Tranz by Gorillaz > played 21 times
 * Magic City by Gorillaz > played 19 times

Week 2:
 * Submission (feat. Danny Brown & Kelela) by Gorillaz > played 66 times
 * Sleeping Powder by Gorillaz > played 65 times
 * On Melancholy Hill by Gorillaz > played 63 times

Week 3:
 * Sex on Fire by Kings of Leon > played 43 times
 * L'esercito del selfie (feat. Lorenzo Fragola & Arisa) by Takagi & Ketra > played 41 times
 * La Luna e la Gatta (feat. Tommaso Paradiso, Jovanotti, Calcutta) by Takagi & Ketra > played 41 times
 
...
"""