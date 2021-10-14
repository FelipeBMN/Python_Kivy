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
    
    def calcular(self, args):
        self.detalhes.text="121,5"
        return 0

    def flip(self):
        # a function for the "flip" icon
        # changes the state of the app
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.text = "enter a decimal number"
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = "enter a binary number"
        # hide labels until needed
        self.converted.text = ""
        self.label.text = ""

    def build(self):
        self.state = 0 #initial state
        #self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        self.state = 0 #initial state
        self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        self.toobar = MDToolbar()
        self.toobar.title = 'Calculadora Solar'
        self.toobar.pos_hint = {"top": 1}        
        self.toobar.left_action_items = [["menu", lambda x: self.menu(x)]]
        # self.toobar.right_action_items = [["account-circle", lambda x: self.menu_user(x)]]
        screen.add_widget(self.toobar)
        
        # Logo
        screen.add_widget(Image(
            source="Logo_pequena.png",
            pos_hint = {"center_x":0.5,"center_y":0.8}
        ))

        # Labels ====================================================
        self.municipio = MDLabel(
            text = "Município",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.62},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        self.n_placas = MDLabel(
            text = "Número de Placas",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        self.pot_placas = MDLabel(
            text = "Potência da Placa",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.38},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        self.detalhes = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.9, "center_y":0.56},
            theme_text_color = "Secondary"
        )
        screen.add_widget(self.municipio)
        screen.add_widget(self.n_placas)
        screen.add_widget(self.pot_placas)
        

        # Inputs =======================================================================
        self.input_municipio = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.56},
            font_size = 22
        )
        self.input_placas = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.44},
            font_size = 22
        )
        self.input_pot_placas = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.32},
            font_size = 22
        )
        screen.add_widget(self.input_municipio)
        screen.add_widget(self.input_placas)
        screen.add_widget(self.input_pot_placas)
        
        # "CONVERT" button=============================================================
        screen.add_widget(MDFillRoundFlatButton(
            text="Calcular",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y":0.1},
            on_press = self.calcular
        ))

        return screen

    
if __name__ == '__main__':
    CalculadoraSolar().run()