import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text = "Hello, this is kivy application")



if __name__ == "__main__":
    MyApp().run()