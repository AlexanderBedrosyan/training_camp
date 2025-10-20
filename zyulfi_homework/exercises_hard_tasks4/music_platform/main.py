from exercises_hard_tasks4.music_platform.playlist import Playlist
from song import Song
from user import User

s1 = Song("Rodino", 54)
s2 = Song("Mayko mila", 30)

pl1 = Playlist()
pl1.add_song(s1)
pl1.add_song(s2)
print(pl1.total_duration())
print(pl1.long_song())

u1 = User("Ivancho")
u1.add_playlist(pl1)
print(u1.favorite_song())
