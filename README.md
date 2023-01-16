# SPOTIFY-DATA-READER

Tiny tool to read Spotify's extended streaming history, you can follow [this guide](https://support.stats.fm/docs/import/spotify-import/) to get yours.


Once you download your streaming history, you are going to see a zip file containing multiple json files.
Put all of them into the `data` folder so the tool can find them.


## usage

```python
from collections import Counter

from reader import streaming_history


def top_songs(year: int = None):
    tracks = []

    for item in streaming_history():
        if year is not None:
            if item.playback.timestamp.year != year:
                continue

        if item.track:
            tracks.append(
                (
                    item.track.name,
                    item.track.artist,
                )
            )

    for (track, artist), counter in Counter(tracks).most_common(5):
        print(f"{track} by {artist} [{counter}]")


top_songs()

# >> Andromeda (feat. DRAM) by Gorillaz [877]
# >> Undercover Martyn by Two Door Cinema Club [682]
# >> Sleeping Powder by Gorillaz [669]
# >> Submission (feat. Danny Brown & Kelela) by Gorillaz [666]
# >> On Melancholy Hill by Gorillaz [606]
```