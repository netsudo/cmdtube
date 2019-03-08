from peewee import *

db = SqliteDatabase("../playlists.db")

class Playlist(Model):
    name = CharField()

    class Meta:
        database = db

class Song(Model):
    playlist = ForeignKeyField(Playlist, backref="songs")
    name = CharField()
    url = CharField()

    class Meta:
        database = db
