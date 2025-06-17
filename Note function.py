from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('note_test.kv')

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Set background color to white
        return MyLayout()
    
if __name__ == '__main__':
    MyApp().run()