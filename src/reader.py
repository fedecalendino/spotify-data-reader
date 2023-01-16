import json
import os

from classes import Item

PATH = "./data"


def streaming_history(source: str = "./data"):
    for path in os.listdir(source):
        if not path.endswith(".json"):
            continue

        file = open(f"{source}/{path}")

        for item in json.load(file):
            is_episode = item["spotify_episode_uri"]
            is_track = item["spotify_track_uri"]

            if not (is_episode or is_track):
                continue

            yield Item(**item)
