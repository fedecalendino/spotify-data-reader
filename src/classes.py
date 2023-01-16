from datetime import datetime


class Episode:
    def __init__(self, name: str, show: str, uri: str):
        self.name: str = name
        self.show: str = show
        self.uri: str = uri

    def __repr__(self):
        return f"{self.name} ({self.show})"


class Track:
    def __init__(self, name: str, album: str, artist: str, uri: str):
        self.name: str = name
        self.album: str = album
        self.artist: str = artist
        self.uri: str = uri

    def __repr__(self):
        return f"{self.name} by {self.artist} ({self.album})"


class Connection:
    def __init__(
        self,
        username: str,
        platform: str,
        ip: str,
        country: str,
        offline: bool,
        incognito_mode: bool,
    ):
        self.username: str = username
        self.platfrom: str = platform
        self.ip: str = ip
        self.country: str = country
        self.offline: bool = offline
        self.incognito_mode: bool = incognito_mode


class Playback:
    def __init__(
        self,
        ms_played: int,
        reason_start: str,
        reason_end: str,
        shuffle: bool,
        skipped: bool,
        timestamp: datetime,
    ):
        self.ms_played: int = ms_played
        self.reason_start: str = reason_start
        self.reason_end: str = reason_end
        self.shuffle: bool = shuffle
        self.skipped: bool = skipped
        self.timestamp: datetime = timestamp


class Item:
    def __init__(self, **data: dict):
        self.episode: Episode = None
        self.track: Track = None

        if data["spotify_episode_uri"]:
            self.episode = Episode(
                name=data["episode_name"],
                show=data["episode_show_name"],
                uri=data["spotify_episode_uri"],
            )
        elif data["spotify_track_uri"]:
            self.track = Track(
                name=data["master_metadata_track_name"],
                album=data["master_metadata_album_album_name"],
                artist=data["master_metadata_album_artist_name"],
                uri=data["spotify_track_uri"],
            )
        else:
            raise ValueError("Invalid item")

        self.connection = Connection(
            username=data["username"],
            platform=data["platform"],
            ip=data["ip_addr_decrypted"],
            country=data["conn_country"],
            offline=data["offline"],
            incognito_mode=data["incognito_mode"],
        )

        self.playback = Playback(
            ms_played=data["ms_played"],
            reason_start=data["reason_start"],
            reason_end=data["reason_end"],
            shuffle=data["shuffle"],
            skipped=data["skipped"],
            timestamp=datetime.fromisoformat(data["ts"].replace("Z", "+00:00")),
        )

    def __repr__(self):
        if self.episode:
            return str(self.episode)

        if self.track:
            return str(self.track)

        return "unknown"
