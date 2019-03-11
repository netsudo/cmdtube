import sys
import pafy
import playlist
from videos import Videos
from player import Player


def selection(videos):
    s = int(input("Select video: "))
    video = pafy.new(videos[s][1])
    best = video.getbestaudio('m4a', True)

    return best.url


def options(stream, music_stream_url, replay=None):
    if replay:
        stream.stop_player()
        stream = Player()
        music_stream_url = replay
        search = input("Search videos: ")
        v = Videos(search)
        v.list_videos()
        music_stream_url = selection(v.videos)
    else:
        music_stream_url = replay
    option = input("\nType (s) to re-search, (r) to replay, (e) to exit\n> ")

    if option == 's':
        stream.stop_player()
        main()

    elif option == 'r':
        stream.stop_player()
        main(music_stream_url)

    elif option == 'p':
        playlists = playlist.list_playlists()
        for i, name in playlists.items():
            print("{}. {}".format(i, name))

        while True:
            option = input("\nType (l) to list songs, (p) to play, (b) to go back\n> ")
            if option == 'l':
                selection = int(input("Select a playlist: "))
                songs = playlists.list_songs(playlists[selection])
                for i, props in songs.items():
                    print("{}. {}".format(i, props[1]))

            elif option == 'p':
                selection = int(input("Select a playlist: "))
                songs = playlists.list_songs(playlists[selection])
                for i, song in songs:
                    music_stream_url = song[2]
                    stream = Player(music_stream_url)
                    stream.start_player()
                    print("Playing: {}".format(song[1]))
                    while stream.is_running:
                        option = input("\nType (n) next, (p) previous, (b) back\n>")
                        if option == 'b':
                            options(stream, music_stream_url)
                        else:
                            pass

            elif option == 'b':
                main()
            else:
                pass

    elif option == 'e':
        sys.exit(1)

    else:
        print("\nType (s) to re-search, (e) to exit\n> ")


def main(replay=None):
    if not replay:
        search = input("Search videos: ")
        v = Videos(search)
        v.list_videos()
        music_stream_url = selection(v.videos)
    else:
        music_stream_url = replay

    stream = Player(music_stream_url)
    stream.start_player()
    options(stream, music_stream_url)


if __name__ == '__main__':
    main()
