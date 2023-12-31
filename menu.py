from camera4kivy import Preview
from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from PIL import Image
from pyzbar.pyzbar import decode


Builder.load_string("""
#: import CRoundedButton custom_widgets
<Menu>:
    name:"menu"
    canvas.before:
        Color:
            rgb: 0.23, 0.23 , 0.23, 1
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: "vertical"
        padding: dp(40)
        
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            size_hint: 1, 0.10
            BoxLayout:
                padding:[dp(20), dp(20), dp(20),dp(50)]
                size_hint_x:None
                width:self.minimum_width
                spacing: dp(5)
                Image:
                    source: "logged_in_guy.png"
                    size_hint: None, None
                    size: dp(20), dp(20)  # Setzen Sie die Größe je nach Bedarf
                    
                Label:
                    text: "User: "
                    size_hint: None, None
                    size: self.texture_size  # Setzen Sie die Breite und Höhe auf die minimale Größe des Textes

                Label:
                    text: "Gjalt Schröder"
                    size_hint: None, None
                    size: self.texture_size  # Setzen Sie die Breite und Höhe auf die minimale Größe des Textes
            
        BoxLayout:
            orientation: "vertical"
            padding:[dp(20), dp(20), dp(20),dp(50)]
            spacing: dp(20)
            size_hint: 1, 0.70
            CRoundedButton:
                text:"Artikel buchen"
                size_hint_y:None
                height:dp(50)
                on_release:root.switch_to_login()
            CRoundedButton:
                text:"Komissionieren"
                size_hint_y:None
                height:dp(50)
                on_release:root.switch_to_signup()
            CRoundedButton:
                text:"Lagerverwaltung"
                size_hint_y:None
                height:dp(50)
                on_press:root.popup_cam_show()
        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'bottom'
            size_hint: 1, 0.20
            
            Image:
                source: "artiware.png"
                size_hint: None, None
                size: dp(60), dp(60)  # Setzen Sie die Größe je nach Bedarf

""")

class Pop_up(Popup):
    def __init__(self, screen_manager, **kwargs):
        super(Pop_up, self).__init__(**kwargs)
        self.screen_manager = screen_manager



    def on_kv_post(self, obj):
        # Ändere die Kamera-ID auf "zwei"
        self.ids.preview.connect_camera(camera_id="0", enable_analyze_pixels=True, default_zoom=0.0)

    @mainthread
    def got_result(self, result):
        string = str(result)
        self.ids.ti.text = string[2:-1]
        signup_screen = self.screen_manager.get_screen("signup")
        signup_screen.ids.qr_code.text = self.ids.ti.text

        # Kamera-Verbindung trennen
        self.ids.preview.disconnect_camera()

        # Popup schließen
        self.dismiss()

    def switch_to_signup(self):
        self.manager.current = "menu"




class ScanAnalyze(Preview):
    extracted_data = ObjectProperty(None)

    def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):
        pimage = Image.frombytes(mode='RGBA', size=image_size, data=pixels)
        list_of_all_barcodes = decode(pimage)

        if list_of_all_barcodes:
            if self.extracted_data:
                self.extracted_data(list_of_all_barcodes[0][0])

            else:
                print("Not found")

class Menu(Screen):
    def switch_to_login(self):
        self.manager.current = "login"
    def switch_to_signup(self):
        self.manager.current = "signup"
    def popup_cam_show(self):
        popup = Pop_up(screen_manager=self.manager)  # Pass the ScreenManager reference
        popup.signup_screen = self
        popup.open()