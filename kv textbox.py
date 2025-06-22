from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.config import Config
import json

kv = """
<NoteWidget>:
    FloatLayout:
        TextInput:
            id: text_input
            hint_text: "Type your note here..."
            size_hint: 2.0, 4.0
            pos_hint: {"x": 0.5, "y": 1.5}
        Button:
            text: "Save Note"
            size_hint: 0.8, 0.8
            pos_hint: {"x": 0.5, "y": 0.4}
            on_release: root.save_note()
"""

Builder.load_string(kv)

class NoteWidget(Widget):
    def __init__(self, **kwargs):
        super(NoteWidget, self).__init__(**kwargs)
        self.text_input = self.ids.text_input

    def save_note(self):
        note_content = self.text_input.text
        with open('note.json', 'w', encoding="utf-8") as f:
            json.dump({"note": note_content}, f)

    def load_note(self):
        try:
            with open('note.json', 'r') as f:
                data = json.load(f)
                self.text_input.text = data.get("note", "")
        except FileNotFoundError:
            self.text_input.text = ""

class NoteApp(App):
    def build(self):
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '600')
        layout = FloatLayout()
        note_widget = NoteWidget()
        layout.add_widget(note_widget)
        note_widget.load_note()
        return layout

if __name__ == '__main__':
    NoteApp().run()
