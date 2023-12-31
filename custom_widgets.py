from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from styles import Styles
from kivy.graphics import RoundedRectangle, Color

Builder.load_string("""
<CRoundedButton>:
    canvas.before:
        Color:
            rgba: self.bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [20,]
    on_press: root.pressed()
    on_release: root.released()

<CTextInput>:
    
    
    padding: dp(15)
    cursor_width: "3sp"
    multiline: False
    cursor_color: self.cursor_color
    
    
<SignupText>
    color: self.bg_color
    

""")


class CRoundedButton(ButtonBehavior, Label):
    bg_color = Styles.primary_color

    def pressed(self):
        print("Button pressed!")
        self.bg_color = Styles.secondary_color
        self.update_color()

    def released(self):
        print("Button released!")
        self.bg_color = Styles.primary_color
        self.update_color()

    def update_color(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.bg_color)
            RoundedRectangle(size=self.size, pos=self.pos, radius=[20, ])


class CTextInput(TextInput):
    bg_color = Styles.textinput_color
    text_color = Styles.secondary_color
    cursor_color = Styles.primary_color

class SignupText(ButtonBehavior, Label):
    bg_color = Styles.primary_color