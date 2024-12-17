from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty, StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen, FadeTransition

# help manage the design, texts, placements of elements, and setting screen setup
loading_screen_helper = """
<SplashScreen>:
    name: "SplashScreen"
    on_enter: self.ids.progress.start()
    RelativeLayout:
        Image:
            source: "Images/Loading.jpg"
            allow_stretch: True
            keep_ratio: False
            opacity: 1
            pos: self.pos
            size: self.size
             
        CircularProgressBar:
            size_hint: None, None
            size: 118, 118
            pos_hint: {'center_x': 0.5, 'center_y': 0.565}
            value: 100
        
        
<CircularProgressBar>
    canvas.before:
        Color:
            rgba: root.bar_color + [0.3]
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)

    canvas.after:
        Color:
            rgb: root.bar_color
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_value * 3.6)

"""

class SplashScreen(Screen):
    def on_enter(self):
        # Schedule the transition after 10 seconds
        Clock.schedule_once(self.change_screen, 10)
        self.manager.transition = FadeTransition(duration=0.3, clearcolor=(1,1,1,1))
        # Clock.schedule_once(self.play_background_music,5)


    def change_screen(self, *args):
        # Change to MainScreen after 10 seconds
        self.manager.current = "main"
        self.stop_background_music()

    # def play_background_music(self, *args):
    #     # Load and play the audio file (replace with your audio path)
    #     self.sound = SoundLoader.load('Sounds/BG.mp3')
    #     if self.sound:
    #         self.sound.loop = True  # Loop the music
    #         self.sound.play()
    #     else:
    #         print("Failed to load sound")

    def stop_background_music(self):
        if hasattr(self, 'sound') and self.sound:
            self.sound.stop()


class CircularProgressBar(AnchorLayout):
    set_value = NumericProperty(0)
    value = NumericProperty(100)  # The maximum value to reach
    bar_color = ListProperty([1 ,1, 1,])
    bar_width = NumericProperty(5.5)
    text = StringProperty("0%")
    counter = 0
    duration = NumericProperty(3)  # Total duration for the progress to complete

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 5)

    def animate(self, *args):
        interval = self.duration / self.value
        Clock.schedule_interval(self.percent_counter, interval)

    def percent_counter(self, *args):
        if self.counter < self.value:
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:
            Clock.unschedule(self.percent_counter)