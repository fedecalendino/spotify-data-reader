import json
from collections import namedtuple
from datetime import datetime

PATH = "./MyData"


Item = namedtuple("Item", ["artist", "track", "ms_played", "timestamp"])


def streaming_history():
    index = -1

    while True:
        index += 1

        try:
            file = open(f"./MyData/StreamingHistory{index}.json")

            for item in json.load(file):
                yield Item(
                    artist=item.get("artistName"),
                    track=item.get("trackName"),
                    ms_played=item.get("msPlayed", 0),
                    timestamp=datetime.strptime(
                        item["endTime"],
                        "%Y-%m-%d %H:%M"
                    )
                )
        except FileNotFoundError:
            break

