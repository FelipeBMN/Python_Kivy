from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class CalculadoraSolar(MDApp):
    def build(self):
        self.state = 0 #initial state
        #self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()
        self.toobar = MDToolbar()
        self.toobar.pos_hint = {"top": 1.05}
        screen.add_widget(self.toobar)
        return screen

if __name__ == '__main__':
    CalculadoraSolar().run()