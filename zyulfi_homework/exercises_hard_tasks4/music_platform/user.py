# Атрибути: name, списък плейлисти
# Методи: add_playlist(pl), favorite_song() (намира най-дългата песен)
from exercises_hard_tasks4.music_platform.playlist import Playlist
from exercises_hard_tasks4.music_platform.song import Song


class User:
    def __init__(self, name):
        self.name = name
        self.list_of_playlist: list[Playlist] = []

    def add_playlist(self, curr_playlist):
        self.list_of_playlist.append(curr_playlist)

    def favorite_song(self):
        best_song = None
        long_time = 0

        for curr_pl in self.list_of_playlist:
            if curr_pl.long_song().duration >= long_time:
                long_time = curr_pl.long_song().duration
                best_song = curr_pl.long_song()
        return best_song.title
