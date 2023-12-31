from camera4kivy import Preview
from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from PIL import Image
from pyzbar.pyzbar import decode

Builder.load_string("""

<Signup>:
    name:"signup"
    
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            Label:
                id:qr_code
                text:"QR-CODE"
                color:"black"
            Button:
                text:"Scan QR Code"
                on_press:root.popup_cam_show()
        
        
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            Label:
                text: "Signup"
            Button:
                on_press:root.switch_to_login()
            Button:
                text:"save Value"
                on_press:root.safe_value()

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
        self.manager.current = "signup"




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

class Signup(Screen):
    def back_to_cam(self):
        self.manager.current = "cam"
    def switch_to_login(self):
        self.manager.current = "login"
    def popup_cam_show(self):
        popup = Pop_up(screen_manager=self.manager)  # Pass the ScreenManager reference
        popup.signup_screen = self
        popup.open()

    def safe_value(self):
        value = "testCODE"
        if 'qr_code' in self.ids:
            self.ids.qr_code.text = str(value)
        else:
            print("Error: 'qr_code' not found in ids dictionary")