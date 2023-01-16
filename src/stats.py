from collections import Counter

from reader import streaming_history


HISTORY = list(streaming_history())


def time_played(year: int = None):
    total = 0

    for item in HISTORY:
        if year is not None:
            if item.playback.timestamp.year != year:
                continue

        total += item.playback.ms_played

    print(f"{total/1000:0.2f} seconds")
    print(f"{total/1000/60:0.2f} minutes")
    print(f"{total/1000/60/60:0.2f} hours")
    print(f"{total/1000/60/60/24:0.2f} days")
    print(f"{total/1000/60/60/24/30:0.2f} months")
    print(f"{total/1000/60/60/24/365:0.2f} years")


def top_artists(year: int = None, count: int = 25):
    artists = []

    for item in HISTORY:
        if year is not None:
            if item.playback.timestamp.year != year:
                continue

        if item.track:
            artists.append(item.track.artist)

    for artist, counter in Counter(artists).most_common(count):
        print(f"{artist} [{counter}]")


def top_songs(year: int = None, count: int = 25):
    tracks = []

    for item in HISTORY:
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

    for (track, artist), counter in Counter(tracks).most_common(count):
        print(f"{track} by {artist} [{counter}]")
