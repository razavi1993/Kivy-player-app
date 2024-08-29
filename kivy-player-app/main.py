from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.window import Window

Window.size= (720,360)

class MainApp(App):
    title = 'My Video'
    def build(self):
        player = VideoPlayer(
            source="myvideo.mp4",
            size_hint=(0.8, 0.8),
            options={'fit_mode': 'contain' }
        )
        player.state = 'play'
        player.options = {'eos': 'loop'}
        player.allow_stretch = True
        return player

if __name__ == '__main__':
    MainApp().run()