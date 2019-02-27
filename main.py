import gi
import sys
import pafy
from videos import Videos
gi.require_version('Gst', '1.0')
from gi.repository import Gst as gst


def selection(videos):
    s = int(input("Select video: "))
    video = pafy.new(videos[s][1])
    best = video.getbestaudio('m4a', True)

    return best.url


def play_video(music_stream_uri):
    def on_tag(bus, msg):
        taglist = msg.parse_tag()
        print('on_tag:')
        for key in taglist.keys():
            print('\t%s = %s' % (key, taglist[key]))

    # creates a playbin (plays media from a uri)
    gst.init(None)
    player = gst.ElementFactory.make("playbin", "player")

    # set the uri
    player.set_property('volume', 0.1)
    player.set_property('uri', music_stream_uri)

    # start playing
    player.set_state(gst.State.PLAYING)

    # listen for tags on the message bus; tag event might be called more than once
    bus = player.get_bus()
    bus.enable_sync_message_emission()
    bus.add_signal_watch()

    bus.connect('message::tag', on_tag)


def main():
    search = input("Search videos: ")
    v = Videos(search)
    v.list_videos()

    music_stream_url = selection(v.videos)
    play_video(music_stream_url)

    option = input("\nType (s) to re-search, (e) to exit\n> ")

    if option == 's':
        main()
    elif option == 'e':
        sys.exit(0)
    else:
        print("Stopping....")
        main()


if __name__ == '__main__':
    main()
