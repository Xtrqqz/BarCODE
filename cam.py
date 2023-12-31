from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import mainthread
from kivy.utils import platform

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from camera4kivy import Preview
from PIL import Image

from pyzbar.pyzbar import decode


Builder.load_string("""

<Cam>:
    name:"cam"
    
    BoxLayout:
        padding: dp(20)
        spacing: dp(20)
		orientation: 'vertical'
			
        Button:
            text: "signup"
            on_press:root.switch_to_signup()
""")

class Cam(Screen):

    def switch_to_signup(self):
        self.manager.current = "signup"

