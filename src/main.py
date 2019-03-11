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


def options(stream, music_stream_url):
    option = input("\nType (s) to re-search, (r) to replay, (e) to exit\n> ")

    if option == 's':
        stream.stop_player()
        main()

    elif option == 'r':
        stream.stop_player()
        main(music_stream_url)

    elif option == 'p':
        print("hello")

    elif option == 'e':
        sys.exit(1)

    else:
        print("\nType (s) to re-search, (e) to exit\n> ")


def main(replay=''):
    if replay == '':
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
