# Playlist
# Атрибути: списък песни
# Методи: add_song(song), total_duration()
from song import Song

class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        # Добавя песен в плейлиста.
        self.songs.append(song)

    def total_duration(self) -> float:
        # Връща общата продължителност на всички песни.
        return sum(s.duration for s in self.songs)

    def all_songs(self):
        # Връща списък с песни (по желание).
        return list(self.songs)

    def __str__(self):
        return f"Playlist({self.name}, {len(self.songs)} songs, total {self.total_duration()} min)"
