from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label

class MainApp(App):
    def build(self):
       # return Button(text='Hello World')
        return Label()

MainApp().run()
