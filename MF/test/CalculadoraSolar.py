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
    user = False
    def menu(self, button):
                self.menu_principal.caller = button
                self.menu_principal.open()

    def menu_user(self,button):
        if self.user == False :
            self.user_deslogado(button)
        if self.user == True :
            print("User Logado!!!")


    def user_deslogado(self, button):
                self.menu_user_deslogado.caller = button
                self.menu_user_deslogado.open()

    def menu_callback(self, text_item):        
        self.menu_principal.dismiss()
        Snackbar(text=text_item).open()

    def logar(self, text_item_user):        
        self.menu_user_deslogado.dismiss()
        Snackbar(text=text_item_user).open()

    def build(self):
        self.state = 0 #initial state
        self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        self.toobar = MDToolbar()
        self.toobar.title = 'Diario de Obra'
        self.toobar.pos_hint = {"top": 1}        
        self.toobar.left_action_items = [["menu", lambda x: self.menu(x)]]
        self.toobar.right_action_items = [["account-circle", lambda x: self.menu_user(x)]]
        screen.add_widget(self.toobar)
        

        #screen.add_widget(Image(
        #    source="logo_branca_pequena.png",
        #    pos_hint = {"center_x":0.5,"center_y":0.95}
        #))

        # Menu Principal
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
             } for i in range(5)
        ]
        self.menu_principal = MDDropdownMenu(
            items = menu_items,
            width_mult = 4,
        )
        
        # Menu do Usuário
        menu_items_user_deslogado = [
            {
                "viewclass": "OneLineListItem",
                "text": "Logar",
                "height": dp(40),
                "on_release": lambda x="Login": self.logar(x),
             } 
        ]
        self.menu_user_deslogado = MDDropdownMenu(
            items = menu_items_user_deslogado,
            width_mult = 2,
        )
        
        #return Builder.load_string(KV)
        return screen

    
if __name__ == '__main__':
    CalculadoraSolar().run()