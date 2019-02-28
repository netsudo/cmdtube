import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst as gst


class Player:
    gst.init(None)
    player = gst.ElementFactory.make("playbin", "player")

    def __init__(self, music_stream_url):
        self.music_stream_url = music_stream_url
        self.volume = 0.1
        self.__start_player()

    def stop_player(self):
        self.player.set_state(gst.State.NULL)

    def __start_player(self):
        def on_tag(bus, msg):
            taglist = msg.parse_tag()
            print('on_tag:')
            for key in taglist.keys():
                print('\t%s = %s' % (key, taglist[key]))

        # Set the url and volume and start player
        self.player.set_property('volume', self.volume)
        self.player.set_property('uri', self.music_stream_url)
        self.player.set_state(gst.State.PLAYING)

        # Listen for tags on the message bus; tag event might be called more than once
        bus = self.player.get_bus()
        bus.enable_sync_message_emission()
        bus.add_signal_watch()

        bus.connect('message::tag', on_tag)
