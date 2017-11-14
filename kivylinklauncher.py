from kivy.app import App
# kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition
from kivy.uix.label import Label
from kivy.clock import Clock
import time
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')

class MainScreen(Screen):
    pass

class WebDevScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("SimpleKivy2.kv")

class MainApp(App):
    def build(self):
        return presentation

    def btnrun(self):
        print ("testing")

if __name__ == "__main__":
    MainApp().run()
