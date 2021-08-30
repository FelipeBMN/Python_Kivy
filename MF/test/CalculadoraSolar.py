from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivy.uix.textfield import MDFTextField
from kivy.uix.label import MDFLabel
from kivy.uix.toobar import MDToolbar

class CalculadoraSolar(MDApp):
    def build(self):
        screen = MDScreen()

        MDToolbar(title="")
        return screen
if __name__ == '__main__':
    CalculadoraSolar().run