from kivy.app import App
from kivy.lang import Builder

KV = '''
GridLayout:
    display: entry
    rows: 6
    columns: 4
    padding: 10
    spacing: 10

    BoxLayout:
        TextInput:
            id: entry
            font_size: 25

    BoxLayout:
        spacing: 10
        Button:
            text: "ac"
            on_press: entry.text = ""
            background_color: 0.7, 0.2, 0.2, 1
        Button:
            text: "Cancle"
            on_press: entry.text = entry.text[:-1]  # Remove the last character
            background_color: 0.8, 0.5, 0.2, 1
        Button:
            text: "%"
            on_press: entry.text += self.text
            background_color: 0.2, 0.5, 0.9, 1
        Button:
            text: "÷"
            on_press: entry.text += self.text
            background_color: 0.2, 0.7, 0.2, 1

    BoxLayout:
        spacing: 10
        Button:
            text: "7"
            on_press: entry.text += self.text
            background_color: 0.8, 0.8, 0.8, 1
        Button:
            text: "8"
            on_press: entry.text += self.text
            background_color: 0.8, 0.8, 0.8, 1
        Button:
            text: "9"
            on_press: entry.text += self.text
            background_color: 0.8, 0.8, 0.8, 1
        Button:
            text: "×"
            on_press: entry.text += self.text
            background_color: 0.2, 0.7, 0.2, 1

    BoxLayout:
        spacing: 10
        Button:
            text: "4"
            on_press: entry.text += self.text
        Button:
            text: "5"
            on_press: entry.text += self.text
        Button:
            text: "6"
            on_press: entry.text += self.text
        Button:
            text: "-"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        Button:
            text: "1"
            on_press: entry.text += self.text
        Button:
            text: "2"
            on_press: entry.text += self.text
        Button:
            text: "3"
            on_press: entry.text += self.text
        Button:
            text: "+"
            on_press: entry.text += self.text


    BoxLayout:
        spacing: 10
        Button:
            text: "0"
            on_press: entry.text += self.text
            background_color: 0.8, 0.8, 0.8, 1
        Button:
            text: "."
            on_press: entry.text += self.text 
            background_color: 0.8, 0.8, 0.8, 1
        Button:
            text: "="
            on_press: app.calculator(entry.text)
            background_color: 0.2, 0.5, 0.9, 1     
'''

class Myapp(App):

    def build(self):
        return Builder.load_string(KV)

    def calculator(self, form):
        self.root.ids.entry.text = str(eval(form))

Myapp().run()
