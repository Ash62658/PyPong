from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class GameControls(FloatLayout):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game

        self.start_button = Button(text='Start', size_hint=(None, None), size=(150, 75),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(0.2, 0.6, 0.9, 1))
        self.start_button.bind(on_release=self.start_game)
        self.add_widget(self.start_button)

    def start_game(self, instance):
        self.start_button.opacity = 0
        self.game.serve_ball()


class WinnerLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '30sp'
        self.bold = True
        self.color = (1, 0, 0, 1)
        self.opacity = 200