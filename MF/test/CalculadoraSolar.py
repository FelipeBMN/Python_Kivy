from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class CalculadoraSolar(MDApp):
    def menu(self):
        print("Menu...")

    def build(self):
        self.state = 0 #initial state
        self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        self.toobar = MDToolbar()
        self.toobar.pos_hint = {"top": 1}        
        self.toobar.left_action_items = [
            ["menu", lambda x: self.menu()]]
        screen.add_widget(self.toobar)
        

        #screen.add_widget(Image(
        #    source="logo_branca_pequena.png",
        #    pos_hint = {"center_x":0.5,"center_y":0.95}
        #))

        return screen


if __name__ == '__main__':
    CalculadoraSolar().run()