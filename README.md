# SPOTIFY-DATA-READER

Tiny tool to read Spotify's extended streaming history, you can follow [this guide](https://support.stats.fm/docs/import/spotify-import/) to get yours.


Once you download your streaming history, you are going to see a zip file containing multiple json files.
Put all of them into the `data` folder so the tool can find them.


# json files contents

```json
[
    ...,
    {
        "conn_country": "SI",
        "episode_name": null,
        "episode_show_name": null,
        "incognito_mode": false,
        "ip_addr_decrypted": "1.2.3.4",
        "master_metadata_album_album_name": "Humanz",
        "master_metadata_album_artist_name": "Gorillaz",
        "master_metadata_track_name": "Andromeda (feat. DRAM)",
        "ms_played": 8778,
        "offline": false,
        "offline_timestamp": 1572964071330,
        "platform": "OS X 10.15.1 [x86 8]",
        "reason_end": "endplay",
        "reason_start": "clickrow",
        "shuffle": true,
        "skipped": null,
        "spotify_episode_uri": null,
        "spotify_track_uri": "spotify:track:2C0KFbb4v9CNWR5c9jWcKC",
        "ts": "2019-11-05T14:28:00Z",
        "user_agent_decrypted": "unknown",
        "username": "username"
    },
    ...,
]
```



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
