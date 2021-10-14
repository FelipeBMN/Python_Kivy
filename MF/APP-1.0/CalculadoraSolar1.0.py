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
    calculado = 0
    screen = MDScreen()
    # Função para o botão Calcular
    def calcular(self, args):
        if self.calculado == 0:
            self.screen.remove_widget(self.input_municipio)
            self.screen.remove_widget(self.input_placas)
            self.screen.remove_widget(self.input_pot_placas)
        self.calculado = 1
        return 0

    # Função para o botão Limpar
    def limpar(self, args):
        if self.calculado == 1:
            self.screen.add_widget(self.input_municipio)
            self.screen.add_widget(self.input_placas)
            self.screen.add_widget(self.input_pot_placas)
        self.calculado = 0
        return 0

    def build(self):

        self.state = 0 #initial state
        self.theme_cls.primary_palette = "DeepOrange"

        self.toobar = MDToolbar()
        self.toobar.title = 'Calculadora Solar'
        self.toobar.pos_hint = {"top": 1}        
        self.toobar.left_action_items = [["menu", lambda x: self.menu(x)]]
        # self.toobar.right_action_items = [["account-circle", lambda x: self.menu_user(x)]]
        self.screen.add_widget(self.toobar)
        
        # Logo
        self.screen.add_widget(Image(
            source="Logo_pequena.png",
            pos_hint = {"center_x":0.5,"center_y":0.8}
        ))

        # Labels Form ====================================================
        self.municipio = MDLabel(
            text = "Município",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.66},
            theme_text_color = "ContrastParentBackground",
            font_style = "H5"
        )
        self.n_placas = MDLabel(
            text = "Número de Placas",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.54},
            theme_text_color = "ContrastParentBackground",
            font_style = "H5"
        )
        self.pot_placas = MDLabel(
            text = "Potência da Placa",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.42},
            theme_text_color = "ContrastParentBackground",
            font_style = "H5"
        )
        
        self.pot_sist = MDLabel(
            text = "Potência: 5,0 kWp",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.25},
            theme_text_color = "ContrastParentBackground",
            font_style = "H5"
        )
        self.ger_mensal = MDLabel(
            text = "Geração Mensal: 545 kWh",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.20},
            theme_text_color = "ContrastParentBackground",
            font_style = "H5"
        )
        
        self.screen.add_widget(self.municipio)
        self.screen.add_widget(self.n_placas)
        self.screen.add_widget(self.pot_placas)
        self.screen.add_widget(self.ger_mensal)
        self.screen.add_widget(self.pot_sist)
        
        # Labels Answers ====================================================



        # Inputs ========================================================
        self.input_municipio = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.60},
            font_size = 22
        )
        self.input_placas = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.48},
            font_size = 22
        )
        self.input_pot_placas = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.36},
            font_size = 22
        )
        self.screen.add_widget(self.input_municipio)
        self.screen.add_widget(self.input_placas)
        self.screen.add_widget(self.input_pot_placas)
        
        # "CONVERT" button=============================================================
        self.screen.add_widget(MDFillRoundFlatButton(
            text="Calcular",
            font_size = 17,
            pos_hint = {"center_x": 0.4, "center_y":0.1},
            on_press = self.calcular
        ))
        self.screen.add_widget(MDFillRoundFlatButton(
            text="Limpar",
            font_size = 17,
            pos_hint = {"center_x": 0.6, "center_y":0.1},
            on_press = self.limpar
        ))

        return self.screen

    
if __name__ == '__main__':
    CalculadoraSolar().run()