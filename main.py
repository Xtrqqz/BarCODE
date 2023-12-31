from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from cam import Cam
from signup import Signup, Pop_up
from login import Login
from menu import Menu, Pop_up



class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cam=Cam()
        signup=Signup()
        login=Login()
        menu=Menu()
        self.add_widget(login)
        self.add_widget(menu)
        self.add_widget(signup)

        self.add_widget(cam)


class BarcodeApp(MDApp):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA, Permission.RECORD_AUDIO])
        return Interface()


if __name__ == '__main__':
    BarcodeApp().run()