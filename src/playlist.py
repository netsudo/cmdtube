from model import Playlist, Song


def save(url, title, playlist="Favourites"):
    playlist, created = Playlist.get_or_create(name=playlist)
    song = Song(url=url, name=title, playlist=playlist.id)
    song.save()


def add_playlist(name):
    playlist = Playlist(playlist=name)
    playlist.save()


def list_songs(playlist=None):
    if playlist is None:
        # Return songs of every playlist
        songs = song_select_format(Song.select())
    else:
        # Return songs belonging to specified playlist
        playlist = Playlist.get(Playlist.name == playlist)
        query = Song.select().where(Song.playlist == playlist.id)
        songs = song_select_format(query)

    return songs


def song_select_format(song_obj):
    songs = {}
    count = 1

    for song in song_obj:
        songs[count] = [song.id, song.name, song.playlist.name]
        count += 1

    return songs
