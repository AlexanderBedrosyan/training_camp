# Playlist
# Атрибути: списък песни
# Методи: add_song(song), total_duration()
from exercises_hard_tasks4.music_platform.song import Song


class Playlist:
    def __init__(self):
        self.playlist: list[Song] = []

    def add_song(self, curr_song:object) -> None:
        self.playlist.append(curr_song)

    def total_duration(self):
        return sum(curr_song.duration for curr_song in self.playlist)

    def long_song(self):
        lg_sg = None
        lg_dr = 0

        for curr_song in self.playlist:
            if curr_song.duration >= lg_dr:
                lg_dr = curr_song.duration
                lg_sg = curr_song
        return lg_sg