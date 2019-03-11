import gi
from threading import Thread
gi.require_version('Gst', '1.0')
from gi.repository import Gst as gst
from gi.repository import GLib


class Player:
    gst.init(None)
    player = gst.ElementFactory.make("playbin", "player")

    def __init__(self, music_stream_url):
        self.music_stream_url = music_stream_url
        self.volume = 0.1
        self.thread = None
        self.loop = GLib.MainLoop()
        self.is_running = False

    def stop_player(self):
        self.player.set_state(gst.State.NULL)
        self.loop.quit()
        self.is_running = False

    def start_player(self):
        self.thread = Thread(target=self.__init_player)
        self.thread.daemon = True
        self.thread.start()
        self.is_running = True

    def __init_player(self):
        def handle_stop(bus, msg):
            self.stop_player()

        # Set the url and volume and start player
        self.player.set_property('volume', self.volume)
        self.player.set_property('uri', self.music_stream_url)
        self.player.set_state(gst.State.PLAYING)

        # Listen for tags on the message bus; tag event might be called more than once
        bus = self.player.get_bus()
        bus.enable_sync_message_emission()
        bus.add_signal_watch()

        bus.connect('message::eos', handle_stop)
        bus.connect('message::error', handle_stop)

        self.loop.run()
