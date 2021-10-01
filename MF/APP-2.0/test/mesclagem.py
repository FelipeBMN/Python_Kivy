from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp



class CalculadoraSolar(MDApp):
        # create a dropdown with 10 buttons
    dropdown = DropDown()


    for index in range(10):
        # When adding widgets, we need to specify the height manually
        # (disabling the size_hint_y) so the dropdown can calculate
        # the area it needs.

        btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

        # for each button, attach a callback that will call the select() method
        # on the dropdown. We'll pass the text of the button as the data of the
        # selection.
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))

        # then add the button inside the dropdown
        dropdown.add_widget(btn)

    # create a big main button
    mainbutton = Button(text='Hello', size_hint=(None, None))

    # show the dropdown menu when the main button is released
    # note: all the bind() calls pass the instance of the caller (here, the
    # mainbutton instance) as the first argument of the callback (here,
    # dropdown.open.).
    mainbutton.bind(on_release=dropdown.open)

    # one last thing, listen for the selection in the dropdown list and
    # assign the data to the button text.
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

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
        

        screen.add_widget(Image(
            source="Logo_pequena.png",
            pos_hint = {"center_x":0.5,"center_y":0.8}
        ))

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