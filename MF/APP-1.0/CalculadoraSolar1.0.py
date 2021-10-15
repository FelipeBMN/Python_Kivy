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
    fator_solares = [
                    ["Sobral",118],
                    ["Cariré",122],
                    ["Pires Ferreira",121],
                    ["Varjota",124],
                    ["Reriutaba",123],
                    ["Graça",120],
                    ["Pacujá",122],
                    ["Mucambo",121],
                    ["Groairas",120],
                    ["Forquilha",119],
                    ["Frecheirinha",120],
                    ["Coreaú",118],
                    ["Alcântaras",122],
                    ["Moraújo",121],
                    ["Meruoca",122],
                    ["Massapê",119],
                    ["Senador Sá",120],
                    ["Santana",119],
                    ["Viçosa do Ceará",123],
                    ["Tianguá",127],
                    ["Ubajara",123],
                    ["Ibiapina",124],
                    ["São Benedito",124],
                    ["Carnaubal",130],
                    ["Guaraciaba do Norte",123],
                    ["Croatá",130],
                    ["Ipu",117],
                    ["Amontada",121],
                    ["Miraima",119],
                    ["Irauçuba",122],
                    ["Itapipoca",121],
                    ["Itapajé",117],
                    ["Tejuçuoca",120],
                    ["Tururu",116],
                    ["Uruburetama",110],
                    ["Umirim",119],
                    ["Pentecoste",122],
                    ["General Sampaio",117],
                    ["Apuiarés",118],
                    ["Barroquinha",123],
                    ["Chaval",125],
                    ["Granja",119],
                    ["Camocim",126],
                    ["Martinópole",121],
                    ["Uruoca",121],
                    ["Jijoca de Jericoacara",123],
                    ["Bela Cruz",122],
                    ["Marco",122],
                    ["Morrinhos",120],
                    ["Acaraú",127],
                    ["Itarema",130],
                    ["Poranga",129],
                    ["Hidrolandia",123],
                    ["Ipueiras",121],
                    ["Ararendá",121],
                    ["Nova Russas",123],
                    ["Ipaporanga",122],
                    ["Crateús",124],
                    ["Novo Oriente",125],
                    ["Independencia",124],
                    ["Tamboril",121],
                    ["Monsenhor Tabosa",121],
                    ["Catunda",122],
                    ["Santa Quitéria",122],
                    ["Boa Viagem",124],
                    ["Madalena",121],
                    ["Itatira",122],
                    ["Canindé",122],
                    ["Caridade",121],
                    ["Paramoti",120],
                    ["Quiterianópolis",123],
                    ["Parambu",125],
                    ["Tauá",124],
                    ["Arneiroz",125],
                    ["Aiuaba",126],
                    ["Trairi",130],
                    ["Paraipaba",127],
                    ["Paracuru",132],
                    ["São Luis do Curu",121],
                    ["São Gonçalo do Amarante",126],
                    ["Caucaia",126],
                    ["Fortaleza",130],
                    ["Maranguape",116],
                    ["Maracanaú",124],
                    ["Eusébio",129],
                    ["Pacatuba",112],
                    ["Guaiúba",117],
                    ["Itaitinga",123],
                    ["Aquiraz",131],
                    ["Horizonte",125],
                    ["Pacajus",125],
                    ["Chorozinho",122],
                    ["Cascavel",120],
                    ["Pindoretama",130],
                    ["Palmacia",120],
                    ["Pacoti",120],
                    ["Redenção",114],
                    ["Guaramiranga",116],
                    ["Acarape",115],
                    ["Barreira",119],
                    ["Baturité",112],
                    ["Mulungu",123],
                    ["Aratuba",120],
                    ["Capistrano",117],
                    ["Aracoiaba",118],
                    ["Itapiúna",119],
                    ["Ocara",121],
                    ["Beberibe",133],
                    ["Fortim",133],
                    ["Aracati",133],
                    ["Itaiçaba",127],
                    ["Jaguaruana",125],
                    ["Icapuí",138],
                    ["Choró",123],
                    ["Ibaretama",123],
                    ["Quixadá",123],
                    ["Ibicuitinga",125],
                    ["Quixeramobim",124],
                    ["Banabuiú",125],
                    ["Pedra Branca",123],
                    ["Mombaça",124],
                    ["Senador Pompeu",124],
                    ["Milhã",126],
                    ["Solonópole",127],
                    ["Piquet Carneiro",125],
                    ["Dep. Irapuan Pinheiro",125],
                    ["Palhano",125],
                    ["Russas",125],
                    ["Morada Nova",128],
                    ["Limoeiro do Norte",125],
                    ["Quixeré",123],
                    ["Tabuleiro do Norte",125],
                    ["São João do Jaguaribe",125],
                    ["Alto Santo",127],
                    ["Potiretama",129],
                    ["Iracema",128],
                    ["Ererê",129],
                    ["Pereiro",131],
                    ["Jaguaribe",129],
                    ["Jaguaribara",128],
                    ["Jaguaretama",131],
                    ["Catarina",128],
                    ["Saboeiro",128],
                    ["Acopiara",126],
                    ["Jucás",123],
                    ["Cariús",127],
                    ["Iguatu",129],
                    ["Quixelô",132],
                    ["Orós",127],
                    ["Icó",129],
                    ["Cedro",130],
                    ["Umari",130],
                    ["Baixio",131],
                    ["Ipaumirim",131],
                    ["Salitre",128],
                    ["Campos Sales",128],
                    ["Antonina do Norte",126],
                    ["Tarrafas",126],
                    ["Araripe",126],
                    ["Potengi",126],
                    ["Assaré",128],
                    ["Altaneira",130],
                    ["Santana do Cariri",124],
                    ["Nova Olinda",128],
                    ["Farias Brito",127],
                    ["Várzea Alegre",130],
                    ["Granjeiro",129],
                    ["Caririaçu",129],
                    ["Juazeiro do Norte",130],
                    ["Barbalha",130],
                    ["Lavras da Mangabeira",129],
                    ["Aurora",129],
                    ["Missão Velha",129],
                    ["Jardim",123],
                    ["Porteiras",124],
                    ["Abaiara",130],
                    ["Milagres",129],
                    ["Barro",126],
                    ["Mauriti",127],
                    ["Brejo Santo",129],
                    ["Jati",124],
                    ["Penaforte",125],
                    ["Crato",128],
                    ["Taperuaba",121],
                    ["Aracatiaçu",121],
                    ["Ubauna",122],
                    ["Alto lindo",132],
                    ["Tapuio",121],
                    ["Lisieux",120],
                    ["Jaibaras",121],
                    ["Aprazível",123]]
    

    user = False
    calculado = 0
    screen = MDScreen()
    def menu(self):
        return 0
    # Função para o botão Calcular
    def calcular(self, args):
        potencia = 0

        try:
            pot_placas = int(self.input_pot_placas.text)
            n_placas = int(self.input_n_placas.text)
            if pot_placas in self.dados_placas:
                potencia = (pot_placas * n_placas)/1000
                self.pot_sist.text = "Potência: "+str(round(potencia,2))+" kWp" 
            else:
                self.pot_sist.text = "Potência de Placas Não Cadastrada" 
        except:
            self.pot_sist.text = "Numero ou Potência das Placas Incorretos"

        try:
            fator_solar = 0
            for fator_solar_dados in self.fator_solares :
                if fator_solar_dados[0] == self.input_municipio.text:
                     fator_solar = fator_solar_dados[1]
            geracao = round(potencia * fator_solar,2)
            if  potencia > 0:
                if fator_solar > 0:
                    self.ger_mensal.text = "Geração Mensal: "+ str(geracao)+" kWh"
                else:
                    self.ger_mensal.text = "Municipio Não Cadastrado"
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
            self.screen.add_widget(self.n_placas_ans)
            self.screen.add_widget(self.pot_placas_ans)
        self.calculado = 1

         # Mostrando respostas
        try:
            self.municipio_ans.text = self.input_municipio.text + " -> Fator Solar: " + str(fator_solar)
            self.n_placas_ans.text = self.input_n_placas.text
            self.pot_placas_ans.text = self.input_pot_placas.text
        except:
            print("Erro nas repostas")



    # Função para o botão Limpar
    def limpar(self, args):
        self.pot_sist.text = ""
        self.ger_mensal.text = ""
        if self.calculado == 1:
            self.screen.remove_widget(self.municipio_ans)
            self.screen.remove_widget(self.n_placas_ans)
            self.screen.remove_widget(self.pot_placas_ans)
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
            pos_hint = {"center_x": 0.5, "center_y":0.7},
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
            pos_hint = {"center_x": 0.5, "center_y":0.64},
            theme_text_color = "Error",
            font_style = "H5"
        )

        self.n_placas_ans = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.48},
            theme_text_color = "Error",
            font_style = "H5"
        )

        self.pot_placas_ans = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.36},
            theme_text_color = "Error",
            font_style = "H5"
        )

        self.pot_sist = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.28},
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
        
        #  button=============================================================
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