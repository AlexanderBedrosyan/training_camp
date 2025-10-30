# User
# Атрибути: name, списък плейлисти
# Методи: add_playlist(pl), favorite_song() (намира най-дългата песен)
from playlist import Playlist

class User:
    def __init__(self, name: str):
        self.name = name
        self.playlists = []

    def add_playlist(self, pl: Playlist):
        # Добавя плейлист към потребителя.
        self.playlists.append(pl)

    def favorite_song(self):

        # Намира най-дългата песен измежду всички плейлисти на потребителя.
        # Ако няма песни, връща None.

        all_songs = [song for pl in self.playlists for song in pl.songs]
        if not all_songs:
            return None
        return max(all_songs, key=lambda s: s.duration)

    def __str__(self):
        return f"User({self.name}, playlists={len(self.playlists)})"
