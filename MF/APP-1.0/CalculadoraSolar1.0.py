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
    # Potências de placas comercializadas
    dados_placas=[  325,
                    330,
                    335,
                    340,
                    345,
                    350,
                    355,
                    360,
                    370,
                    375,
                    380,
                    385,
                    390,
                    395,
                    400,
                    405,
                    410,
                    415,
                    420,
                    425,
                    430,
                    435,
                    440,
                    445,
                    450,
                    455,
                    460,
                    525,
                    530,
                    535,
                    540,
                    545,
                    550  ]

    user = False
    calculado = 0
    screen = MDScreen()
    def menu(self):
        return 0
    # Função para o botão Calcular
    def calcular(self, args):
        potencia = 0
        # Mostrando respostas
        try:
            self.municipio_ans.text = self.input_municipio.text
        except:
            print("Erro nas repostas")

        try:
            pot_placas = int(self.input_pot_placas.text)
            n_placas = int(self.input_n_placas.text)
            if pot_placas in self.dados_placas:
                potencia = (pot_placas * n_placas)/1000
                self.pot_sist.text = "Potência: "+str(potencia)+" kWp" 
            else:
                self.pot_sist.text = "Potência de Placas Não Cadastrada" 
        except:
            self.pot_sist.text = "Numero ou Potência das Placas Incorretos"

        try:
            fator_solar = 118
            geracao = potencia * fator_solar
            if  potencia > 0 :
                self.ger_mensal.text = "Geração Mensal: "+ str(geracao)+" kWh"
            else: 
                self.ger_mensal.text = ""
        except:
            self.ger_mensal.text = "Município Não Encontrado"
            
        
        # retira os campo os de input
        if self.calculado == 0:
            self.screen.remove_widget(self.input_municipio)
            self.screen.remove_widget(self.input_n_placas)
            self.screen.remove_widget(self.input_pot_placas)
            self.screen.add_widget(self.municipio_ans)
        self.calculado = 1
        return 0

    # Função para o botão Limpar
    def limpar(self, args):
        self.pot_sist.text = ""
        self.ger_mensal.text = ""
        if self.calculado == 1:
            self.screen.remove_widget(self.municipio_ans)
            self.screen.add_widget(self.input_municipio)
            self.screen.add_widget(self.input_n_placas)
            self.screen.add_widget(self.input_pot_placas)
        self.calculado = 0
        return 0

    def build(self):

        self.state = 0 #initial state
        self.theme_cls.primary_palette = "DeepOrange"

        self.toobar = MDToolbar()
        self.toobar.title = 'Calculadora Solar'
        self.toobar.pos_hint = {"top": 1}        
        self.toobar.left_action_items = [["menu", lambda x: self.menu()]]
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
        
        self.screen.add_widget(self.municipio)
        self.screen.add_widget(self.n_placas)
        self.screen.add_widget(self.pot_placas)
        
        
        # Labels Answers ====================================================
        self.municipio_ans = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.60},
            theme_text_color = "Error",
            font_style = "H5"
        )

        self.pot_sist = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.25},
            theme_text_color = "ContrastParentBackground",
            font_style = "H5"
        )
        self.ger_mensal = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.20},
            theme_text_color = "ContrastParentBackground",
            font_style = "H5"
        )

        self.screen.add_widget(self.ger_mensal)
        self.screen.add_widget(self.pot_sist)
        # Inputs ========================================================
        self.input_municipio = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.60},
            font_size = 22
        )
        self.input_n_placas = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.48},
            font_size = 22,
        )
        self.input_pot_placas = MDTextField(
            text="",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.36},
            font_size = 22
        )
        self.screen.add_widget(self.input_municipio)
        self.screen.add_widget(self.input_n_placas)
        self.screen.add_widget(self.input_pot_placas)
        
        # "CONVERT" button=============================================================
        self.screen.add_widget(MDFillRoundFlatButton(
            text="Calcular",
            font_size = 17,
            pos_hint = {"center_x": 0.8, "center_y":0.1},
            on_press = self.calcular
        ))
        self.screen.add_widget(MDFillRoundFlatButton(
            text="Corrigir",
            font_size = 17,
            pos_hint = {"center_x": 0.2, "center_y":0.1},
            on_press = self.limpar
        ))

        return self.screen

    
if __name__ == '__main__':
    CalculadoraSolar().run()