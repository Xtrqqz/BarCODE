from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string("""
#: import CRoundedButton custom_widgets
#: import CTextInput custom_widgets
#: import SignupText custom_widgets
<Login>:
    name:"login"
    canvas.before:
        Color:
            rgb: 0.23, 0.23 , 0.23, 1
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: "vertical"
        padding: dp(40)
        BoxLayout:
            size_hint: 1, 0.35
            
            Image:
                source: "artiware.png"
        AnchorLayout:
            size_hint: 1, 0.55
            anchor_y:"top"
            padding: [0, dp(60), 0,0]
            BoxLayout:
                orientation: "vertical"
                size_hint_y:None
                height:self.minimum_height
                spacing: dp(10)
                padding: [dp(30), 0, dp(30),0]
                
                BoxLayout:
                    
                    
                    Label:
                        text:"Willkommen bei AritWare:"
                        font_size:'16sp'
                        halign:"left"
                        size_hint_y:None
                        size:self.texture_size
                        text_size:self.size
                    
                CTextInput:
                    size_hint_y:None
                    height:dp(50)
                    hint_text:"Username"
                    
                    
                CTextInput:
                    size_hint_y:None
                    height:dp(50)
                    hint_text:"Passwort"
                    password: True
                BoxLayout:
                    AnchorLayout:
                        anchor_y:"top"
                        
                        BoxLayout:
                            orientation: "vertical"
                            size_hint_y:None
                            height:self.minimum_height
                            padding: [dp(30), dp(35), dp(30),0]
                            spacing: dp(30)        
                            CRoundedButton:
                                text:"Login"
                                size_hint_y:None
                                height:dp(50)
                                on_release:root.switch_to()
                            Label:
                                id:"login_msg"
                                text:""
                                color: 1, 0, 0, 1
                           
                    
        AnchorLayout:
            size_hint: 1, 0.1
            anchor_x: "center"    
            BoxLayout:
                size_hint_x:None
                width:self.minimum_width
                Label:
                    text:"Passwort vergessen? "
                    size_hint_x:None
                    size:self.texture_size
                SignupText:
                    text:"Klicke hier"
                    size_hint_x:None
                    size:self.texture_size
                    
        
""")
class Login(Screen):
    def switch_to(self):
        self.manager.current = "menu"
