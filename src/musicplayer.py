import pyglet

class MusicPlayer:
    player = pyglet.media.Player()
    theme =  pyglet.media.load('./resources/sound/gasgasgas.wav')
    game_is_running = True

    def __init__(self):
        self.player.queue(self.my_playlist())

    def my_playlist(self):
        while self.game_is_running:
            yield self.theme