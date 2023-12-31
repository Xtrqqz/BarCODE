

from kivy.utils import get_color_from_hex

class Styles:
    primary_color = get_color_from_hex("#577F9C")
    secondary_color = get_color_from_hex("#FFFFFF")
    textinput_color = (*get_color_from_hex("#66B9F2")[:-1], 0.3)
