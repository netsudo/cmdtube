from peewee import Model, SqliteDatabase, CharField, ForeignKeyField

db = SqliteDatabase("../playlists.db")


class BaseModel(Model):
    class Meta:
        database = db


class Playlist(BaseModel):
    name = CharField()


class Song(BaseModel):
    playlist = ForeignKeyField(Playlist, backref="songs")
    name = CharField()
    url = CharField()


db.create_tables([Playlist, Song])
