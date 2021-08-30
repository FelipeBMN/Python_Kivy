from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class CalculadoraSolar(MDApp):
    def build(self):
        screen = MDScreen()
        self.toobar = MDToolbar(title="CalculadoraSolar")
        self.toobar.pos_hint = {"top": 1}
        screen.add_widget(self.toobar)
        return screen

if __name__ == '__main__':
    CalculadoraSolar().run