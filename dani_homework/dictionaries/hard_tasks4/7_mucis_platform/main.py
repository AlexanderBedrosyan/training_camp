from song import Song
from playlist import Playlist
from user import User

# Песни
s1 = Song("Bohemian Rhapsody", 5.9)
s2 = Song("Imagine", 3.1)
s3 = Song("Stairway to Heaven", 8.0)
s4 = Song("Yesterday", 2.5)

# Плейлисти
pl1 = Playlist("Rock Classics")
pl1.add_song(s1)
pl1.add_song(s3)

pl2 = Playlist("Chill Vibes")
pl2.add_song(s2)
pl2.add_song(s4)

# Потребител
u = User("Alice")
u.add_playlist(pl1)
u.add_playlist(pl2)

# Демонстрация
print(pl1)
print(pl2)
print("Обща продължителност на Rock Classics:", pl1.total_duration(), "min")
print("Любима песен (най-дълга):", u.favorite_song())
