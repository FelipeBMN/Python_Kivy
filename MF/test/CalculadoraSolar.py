from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar



class CalculadoraSolar(MDApp):
    def callback(self, button):
                self.menu.caller = button
                self.menu.open()

    def user(self, button):
                self.menu_user.caller = button
                self.menu_user.open()

    def menu_callback_user(self, text_item):        
        self.menu.dismiss()
        Snackbar(text=text_item).open()

    def build(self):
        self.state = 0 #initial state
        self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        self.toobar = MDToolbar()
        self.toobar.title = 'Diario de Obra'
        self.toobar.pos_hint = {"top": 1}        
        self.toobar.left_action_items = [["menu", lambda x: self.callback(x)]]
        self.toobar.right_action_items = [["account-circle", lambda x: self.user(x)]]
        screen.add_widget(self.toobar)
        

        #screen.add_widget(Image(
        #    source="logo_branca_pequena.png",
        #    pos_hint = {"center_x":0.5,"center_y":0.95}
        #))

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
             } for i in range(5)
        ]

        menu_items_user = [
            {
                "viewclass": "OneLineListItem",
                "text": "Logar",
                "height": dp(40),
                "on_release": lambda x="Login": self.menu_callback_user(x),
             } 
        ]

        self.menu = MDDropdownMenu(
            items = menu_items,
            width_mult = 4,
        )

        self.menu_user = MDDropdownMenu(
            items = menu_items_user,
            width_mult = 2,
        )
        
        #return Builder.load_string(KV)
        return screen

    
if __name__ == '__main__':
    CalculadoraSolar().run()