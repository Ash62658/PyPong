from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from game import PongGame
from ui import GameControls, WinnerLabel
from kivy.core.audio import SoundLoader


class PongApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        game = PongGame()
        controls = GameControls(game=game)
        winner_label = WinnerLabel()

        root.add_widget(game)
        root.add_widget(controls)
        root.add_widget(winner_label)

        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return root


if __name__ == '__main__':
    music = SoundLoader.load("Bgmg.mp3")
    music.loop = True
    music.play()
    
    PongApp().run()