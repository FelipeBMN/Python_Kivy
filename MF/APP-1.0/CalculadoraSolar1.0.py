import kivy

kivy.require('2.0.0')
import kivymd
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


# Função principal =====================================================
class CalculadoraSolar(MDApp):

    # Dados Para o Programa =====================================================
    dados_placas = [325,
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
                    550]

    fator_solares = [
        ["Sobral", 118],
        ["Cariré", 122],
        ["Pires Ferreira", 121],
        ["Varjota", 124],
        ["Reriutaba", 123],
        ["Graça", 120],
        ["Pacujá", 122],
        ["Mucambo", 121],
        ["Groairas", 120],
        ["Forquilha", 119],
        ["Frecheirinha", 120],
        ["Coreaú", 118],
        ["Alcântaras", 122],
        ["Moraújo", 121],
        ["Meruoca", 122],
        ["Massapê", 119],
        ["Senador Sá", 120],
        ["Santana", 119],
        ["Viçosa do Ceará", 123],
        ["Tianguá", 127],
        ["Ubajara", 123],
        ["Ibiapina", 124],
        ["São Benedito", 124],
        ["Carnaubal", 130],
        ["Guaraciaba do Norte", 123],
        ["Croatá", 130],
        ["Ipu", 117],
        ["Amontada", 121],
        ["Miraima", 119],
        ["Irauçuba", 122],
        ["Itapipoca", 121],
        ["Itapajé", 117],
        ["Tejuçuoca", 120],
        ["Tururu", 116],
        ["Uruburetama", 110],
        ["Umirim", 119],
        ["Pentecoste", 122],
        ["General Sampaio", 117],
        ["Apuiarés", 118],
        ["Barroquinha", 123],
        ["Chaval", 125],
        ["Granja", 119],
        ["Camocim", 126],
        ["Martinópole", 121],
        ["Uruoca", 121],
        ["Jijoca de Jericoacara", 123],
        ["Bela Cruz", 122],
        ["Marco", 122],
        ["Morrinhos", 120],
        ["Acaraú", 127],
        ["Itarema", 130],
        ["Poranga", 129],
        ["Hidrolandia", 123],
        ["Ipueiras", 121],
        ["Ararendá", 121],
        ["Nova Russas", 123],
        ["Ipaporanga", 122],
        ["Crateús", 124],
        ["Novo Oriente", 125],
        ["Independencia", 124],
        ["Tamboril", 121],
        ["Monsenhor Tabosa", 121],
        ["Catunda", 122],
        ["Santa Quitéria", 122],
        ["Boa Viagem", 124],
        ["Madalena", 121],
        ["Itatira", 122],
        ["Canindé", 122],
        ["Caridade", 121],
        ["Paramoti", 120],
        ["Quiterianópolis", 123],
        ["Parambu", 125],
        ["Tauá", 124],
        ["Arneiroz", 125],
        ["Aiuaba", 126],
        ["Trairi", 130],
        ["Paraipaba", 127],
        ["Paracuru", 132],
        ["São Luis do Curu", 121],
        ["São Gonçalo do Amarante", 126],
        ["Caucaia", 126],
        ["Fortaleza", 130],
        ["Maranguape", 116],
        ["Maracanaú", 124],
        ["Eusébio", 129],
        ["Pacatuba", 112],
        ["Guaiúba", 117],
        ["Itaitinga", 123],
        ["Aquiraz", 131],
        ["Horizonte", 125],
        ["Pacajus", 125],
        ["Chorozinho", 122],
        ["Cascavel", 120],
        ["Pindoretama", 130],
        ["Palmacia", 120],
        ["Pacoti", 120],
        ["Redenção", 114],
        ["Guaramiranga", 116],
        ["Acarape", 115],
        ["Barreira", 119],
        ["Baturité", 112],
        ["Mulungu", 123],
        ["Aratuba", 120],
        ["Capistrano", 117],
        ["Aracoiaba", 118],
        ["Itapiúna", 119],
        ["Ocara", 121],
        ["Beberibe", 133],
        ["Fortim", 133],
        ["Aracati", 133],
        ["Itaiçaba", 127],
        ["Jaguaruana", 125],
        ["Icapuí", 138],
        ["Choró", 123],
        ["Ibaretama", 123],
        ["Quixadá", 123],
        ["Ibicuitinga", 125],
        ["Quixeramobim", 124],
        ["Banabuiú", 125],
        ["Pedra Branca", 123],
        ["Mombaça", 124],
        ["Senador Pompeu", 124],
        ["Milhã", 126],
        ["Solonópole", 127],
        ["Piquet Carneiro", 125],
        ["Dep. Irapuan Pinheiro", 125],
        ["Palhano", 125],
        ["Russas", 125],
        ["Morada Nova", 128],
        ["Limoeiro do Norte", 125],
        ["Quixeré", 123],
        ["Tabuleiro do Norte", 125],
        ["São João do Jaguaribe", 125],
        ["Alto Santo", 127],
        ["Potiretama", 129],
        ["Iracema", 128],
        ["Ererê", 129],
        ["Pereiro", 131],
        ["Jaguaribe", 129],
        ["Jaguaribara", 128],
        ["Jaguaretama", 131],
        ["Catarina", 128],
        ["Saboeiro", 128],
        ["Acopiara", 126],
        ["Jucás", 123],
        ["Cariús", 127],
        ["Iguatu", 129],
        ["Quixelô", 132],
        ["Orós", 127],
        ["Icó", 129],
        ["Cedro", 130],
        ["Umari", 130],
        ["Baixio", 131],
        ["Ipaumirim", 131],
        ["Salitre", 128],
        ["Campos Sales", 128],
        ["Antonina do Norte", 126],
        ["Tarrafas", 126],
        ["Araripe", 126],
        ["Potengi", 126],
        ["Assaré", 128],
        ["Altaneira", 130],
        ["Santana do Cariri", 124],
        ["Nova Olinda", 128],
        ["Farias Brito", 127],
        ["Várzea Alegre", 130],
        ["Granjeiro", 129],
        ["Caririaçu", 129],
        ["Juazeiro do Norte", 130],
        ["Barbalha", 130],
        ["Lavras da Mangabeira", 129],
        ["Aurora", 129],
        ["Missão Velha", 129],
        ["Jardim", 123],
        ["Porteiras", 124],
        ["Abaiara", 130],
        ["Milagres", 129],
        ["Barro", 126],
        ["Mauriti", 127],
        ["Brejo Santo", 129],
        ["Jati", 124],
        ["Penaforte", 125],
        ["Crato", 128],
        ["Taperuaba", 121],
        ["Aracatiaçu", 121],
        ["Ubauna", 122],
        ["Alto lindo", 132],
        ["Tapuio", 121],
        ["Lisieux", 120],
        ["Jaibaras", 121],
        ["Aprazível", 123],

        ["Sobral", 118],
        ["Carire", 122],
        ["Pires Ferreira", 121],
        ["Varjota", 124],
        ["Reriutaba", 123],
        ["Graça", 120],
        ["Pacuja", 122],
        ["Mucambo", 121],
        ["Groairas", 120],
        ["Forquilha", 119],
        ["Frecheirinha", 120],
        ["Coreau", 118],
        ["Alcantaras", 122],
        ["Moraujo", 121],
        ["Meruoca", 122],
        ["Massape", 119],
        ["Senador Sa", 120],
        ["Santana", 119],
        ["Viçosa do Ceara", 123],
        ["Tiangua", 127],
        ["Ubajara", 123],
        ["Ibiapina", 124],
        ["São Benedito", 124],
        ["Carnaubal", 130],
        ["Guaraciaba do Norte", 123],
        ["Croata", 130],
        ["Ipu", 117],
        ["Amontada", 121],
        ["Miraima", 119],
        ["Irauçuba", 122],
        ["Itapipoca", 121],
        ["Itapaje", 117],
        ["Tejuçuoca", 120],
        ["Tururu", 116],
        ["Uruburetama", 110],
        ["Umirim", 119],
        ["Pentecoste", 122],
        ["General Sampaio", 117],
        ["Apuiares", 118],
        ["Barroquinha", 123],
        ["Chaval", 125],
        ["Granja", 119],
        ["Camocim", 126],
        ["Martinópole", 121],
        ["Uruoca", 121],
        ["Jijoca de Jericoacara", 123],
        ["Bela Cruz", 122],
        ["Marco", 122],
        ["Morrinhos", 120],
        ["Acarau", 127],
        ["Itarema", 130],
        ["Poranga", 129],
        ["Hidrolandia", 123],
        ["Ipueiras", 121],
        ["Ararenda", 121],
        ["Nova Russas", 123],
        ["Ipaporanga", 122],
        ["Crateus", 124],
        ["Novo Oriente", 125],
        ["Independencia", 124],
        ["Tamboril", 121],
        ["Monsenhor Tabosa", 121],
        ["Catunda", 122],
        ["Santa Quiteria", 122],
        ["Boa Viagem", 124],
        ["Madalena", 121],
        ["Itatira", 122],
        ["Caninde", 122],
        ["Caridade", 121],
        ["Paramoti", 120],
        ["Quiterianopolis", 123],
        ["Parambu", 125],
        ["Taua", 124],
        ["Arneiroz", 125],
        ["Aiuaba", 126],
        ["Trairi", 130],
        ["Paraipaba", 127],
        ["Paracuru", 132],
        ["São Luis do Curu", 121],
        ["São Gonçalo do Amarante", 126],
        ["Caucaia", 126],
        ["Fortaleza", 130],
        ["Maranguape", 116],
        ["Maracanau", 124],
        ["Eusebio", 129],
        ["Pacatuba", 112],
        ["Guaiuba", 117],
        ["Itaitinga", 123],
        ["Aquiraz", 131],
        ["Horizonte", 125],
        ["Pacajus", 125],
        ["Chorozinho", 122],
        ["Cascavel", 120],
        ["Pindoretama", 130],
        ["Palmacia", 120],
        ["Pacoti", 120],
        ["Redençao", 114],
        ["Guaramiranga", 116],
        ["Acarape", 115],
        ["Barreira", 119],
        ["Baturite", 112],
        ["Mulungu", 123],
        ["Aratuba", 120],
        ["Capistrano", 117],
        ["Aracoiaba", 118],
        ["Itapiuna", 119],
        ["Ocara", 121],
        ["Beberibe", 133],
        ["Fortim", 133],
        ["Aracati", 133],
        ["Itaiçaba", 127],
        ["Jaguaruana", 125],
        ["Icapui", 138],
        ["Choro", 123],
        ["Ibaretama", 123],
        ["Quixada", 123],
        ["Ibicuitinga", 125],
        ["Quixeramobim", 124],
        ["Banabuiu", 125],
        ["Pedra Branca", 123],
        ["Mombaça", 124],
        ["Senador Pompeu", 124],
        ["Milha", 126],
        ["Solonópole", 127],
        ["Piquet Carneiro", 125],
        ["Dep. Irapuan Pinheiro", 125],
        ["Palhano", 125],
        ["Russas", 125],
        ["Morada Nova", 128],
        ["Limoeiro do Norte", 125],
        ["Quixere", 123],
        ["Tabuleiro do Norte", 125],
        ["São João do Jaguaribe", 125],
        ["Alto Santo", 127],
        ["Potiretama", 129],
        ["Iracema", 128],
        ["Erere", 129],
        ["Pereiro", 131],
        ["Jaguaribe", 129],
        ["Jaguaribara", 128],
        ["Jaguaretama", 131],
        ["Catarina", 128],
        ["Saboeiro", 128],
        ["Acopiara", 126],
        ["Jucas", 123],
        ["Carius", 127],
        ["Iguatu", 129],
        ["Quixelo", 132],
        ["Oros", 127],
        ["Ico", 129],
        ["Cedro", 130],
        ["Umari", 130],
        ["Baixio", 131],
        ["Ipaumirim", 131],
        ["Salitre", 128],
        ["Campos Sales", 128],
        ["Antonina do Norte", 126],
        ["Tarrafas", 126],
        ["Araripe", 126],
        ["Potengi", 126],
        ["Assare", 128],
        ["Altaneira", 130],
        ["Santana do Cariri", 124],
        ["Nova Olinda", 128],
        ["Farias Brito", 127],
        ["Varzea Alegre", 130],
        ["Granjeiro", 129],
        ["Caririaçu", 129],
        ["Juazeiro do Norte", 130],
        ["Barbalha", 130],
        ["Lavras da Mangabeira", 129],
        ["Aurora", 129],
        ["Missão Velha", 129],
        ["Jardim", 123],
        ["Porteiras", 124],
        ["Abaiara", 130],
        ["Milagres", 129],
        ["Barro", 126],
        ["Mauriti", 127],
        ["Brejo Santo", 129],
        ["Jati", 124],
        ["Penaforte", 125],
        ["Crato", 128],
        ["Taperuaba", 121],
        ["Aracatiaçu", 121],
        ["Ubauna", 122],
        ["Alto lindo", 132],
        ["Tapuio", 121],
        ["Lisieux", 120],
        ["Jaibaras", 121],
        ["Aprazivel", 123]]

    Marcas = [  "GROWATT",
                "HOYMILES",
                "SMA",
                "SOLIS",
                "CANADIAN",
                "LIVOLTEK" ]

    Inversores = [  ["GROWATT",	"MID 15KTL3-X"],
                    ["GROWATT",	"MID 17KTL3-X"],
                    ["GROWATT",	"MID 20KTL3-X"],
                    ["GROWATT",	"MID 22KTL3-X"],
                    ["GROWATT",	"MID 25KTL3-X"],
                    ["GROWATT",	"MID 25KTL3-X"],
                    ["GROWATT",	"7000MTL-S"],
                    ["GROWATT",	"8000MTL-S"],
                    ["GROWATT",	"7000MTL-S"],
                    ["GROWATT",	"MIN 2500TL-X"],
                    ["GROWATT",	"MIN 2500TL-X"],
                    ["GROWATT",	"MIN 3600TL-X"],
                    ["GROWATT",	"MIN 4200TL-X"],
                    ["GROWATT",	"MIN 4600TL-X"],
                    ["GROWATT",	"MIN 5000TL-X"],
                    ["GROWATT",	"MIN 6000TL-X"],
                    ["GROWATT",	"MAX 50KTL3 LV"],
                    ["GROWATT",	"MAX 60KTL3 LV"],
                    ["GROWATT",	"MAX 70KTL3 LV"],
                    ["GROWATT",	"MAX 80KTL3 LV"],
                    ["SOLIS", "Solis-1P7K-4G"],
                    ["SOLIS", "Solis-1P8K-4G"],
                    ["SOLIS", "Solis-1P9K-4G"],
                    ["SOLIS", "Solis-1P10K-4G"],
                    ["SOLIS", "Solis-25K-5G"],
                    ["SOLIS", "Solis-30K-5G"],
                    ["SOLIS", "Solis-33K-5G"],
                    ["SOLIS", "Solis-36K-5G"],
                    ["SOLIS", "Solis-40K-5G"],
                    ["SOLIS", "Solis-40K-HV-5G"],
                    ["SOLIS", "Solis-50K-HV-5G"],
                    ["SOLIS", "Solis-50K"],
                    ["SOLIS", "Solis-50K-HV"],
                    ["SOLIS", "Solis-60K-HV"],
                    ["SOLIS", "Solis-60K-4G"],
                    ["SOLIS", "Solis-75K-5G"],
                    ["SOLIS", "Solis-80K-5G"],
                    ["SOLIS", "Solis-1P2.5K-4G"],
                    ["SOLIS", "Solis-1P3K-4G"],
                    ["SOLIS", "Solis-1P3.6K-4G"],
                    ["SOLIS", "Solis-1P4K-4G"],
                    ["SOLIS", "Solis-1P4.6K-4G"],
                    ["SOLIS", "Solis-1P5K-4G"],
                    ["SOLIS", "Solis-1P6K-4G"],
                    ["SOLIS", "Solis-3P5K-4G"],
                    ["SOLIS", "Solis-3P6K-4G"],
                    ["SOLIS", "Solis-3P8K-4G"],
                    ["SOLIS", "Solis-3P9K-4G"],
                    ["SOLIS", "Solis-3P10K-4G"],
                    ["SOLIS", "Solis-3P12K-4G"],
                    ["SOLIS", "Solis-3P15K-4G"],
                    ["SOLIS", "Solis-3P17K-4G"],
                    ["SOLIS", "Solis-3P20K-4G"],
                    ["SMA",	"Sunny Tripower 15000TL"],
                    ["SMA",	"Sunny Tripower 20000TL"],
                    ["SMA",	"Sunny Tripower 25000TL"],
                    ["SMA",	"Sunny Tripower CORE1"],
                    ["LIVOLTEK", "GT1-3K-S"],
                    ["LIVOLTEK", "GT1-5K-D"],
                    ["LIVOLTEK", "GT1-6K-D"],
                    ["LIVOLTEK", "GT1-5K-D"],
                    ["LIVOLTEK", "GT1-6K-D"],
                    ["CANADIAN", "CSI-3K-S22002-ED"],
                    ["CANADIAN", "CSI-5K-S22002-ED"],
                    ["CANADIAN", "CSI-5KTL1P-FL"],
                    ["CANADIAN", "CSI-7K-S22002-ED"],
                    ["CANADIAN", "CSI-8KTL1P-GI-FL"],
                    ["CANADIAN", "CSI-15K-T400GL01-E"],
                    ["CANADIAN", "CSI-20KTL-GI-LFL"],
                    ["CANADIAN", "CSI-25K-T400GL02-E"],
                    ["CANADIAN", "CSI-25KTL-GI-L"],
                    ["CANADIAN", "CSI-30KTL-GI-L"],
                    ["CANADIAN", "CSI-50KTL-GI"],
                    ["CANADIAN", "CSI-60KTL-GI"],
                    ["CANADIAN", "CSI-75K-T400GL02-E"],
                    ["CANADIAN", "CSI-100K-T400GL02-E"],
                    ["LIVOLTEK", "GT1 8K"],
                    ["LIVOLTEK", "GT1 10K"],
                    ["LIVOLTEK", "GT3-25K"],
                    ["LIVOLTEK", "GT3-30K"],
                    ["HOYMILES", "MI-1000"],
                    ["HOYMILES", "MI-1200"],
                    ["HOYMILES", "MI-1500"],
                    ["HOYMILES", "HMS-1800"],
                    ["HOYMILES", "HMS-2000"],
                    ["GROWATT",	"MAC 30KTL3-X LV"],
                    ["GROWATT",	"MAC 40KTL3-X LV"],
                    ["GROWATT",	"MAC 50KTL3-X LV"],
                    ["GROWATT",	"MAC 60KTL3-X LV"],
                    ["CANADIAN", "CSI-9K-S2202-E"]]
    # Variaveis do Programa =======================]==============================
    tela = 3
    pc_android = 0
    user = False
    calculado = 0
    inf = 0
    screen = MDScreen()

    # Funções para o Menu =====================================================
    def menu(self, button):
        self.menu_principal.caller = button
        self.menu_principal.open()

    def menu_callback(self, text_item):
        self.menu_principal.dismiss()
        if (text_item == 1) and (self.tela != 1):
            self.remove_tela2("all")
            self.remove_tela3("all")
            if self.pc_android == 0: 
                self.tela1_pc()
            else: 
                self.tela1_android()
            self.tela = 1
        if (text_item == 2) and (self.tela != 2):
            self.remove_tela1("all")
            self.remove_tela3("all")
            if self.pc_android == 0: 
                self.tela2_pc()
            else: 
                self.tela2_android() 
            self.tela = 2
        if (text_item == 3) and (self.tela != 3):
            self.remove_tela1("all")
            self.remove_tela2("all")
            if self.pc_android == 0: 
                self.tela3_pc()
            else: 
                self.tela3_android()   
            self.tela = 3    

    # Função para o botão Calcular ============================================          
    def remove_tela1(self, type):
        if self.tela == 1 :
            if type == "input":
                self.screen.remove_widget(self.input_municipio)
                self.screen.remove_widget(self.input_n_placas)
                self.screen.remove_widget(self.input_pot_placas)
            if type == "ans":
                self.screen.remove_widget(self.municipio_ans)
                self.screen.remove_widget(self.n_placas_ans)
                self.screen.remove_widget(self.pot_placas_ans)
            if type == "all":
                self.calculado = 0
                self.inf = 0
                self.screen.remove_widget(self.input_municipio)
                self.screen.remove_widget(self.input_n_placas)
                self.screen.remove_widget(self.input_pot_placas)
                self.screen.remove_widget(self.municipio_ans)
                self.screen.remove_widget(self.n_placas_ans)
                self.screen.remove_widget(self.pot_placas_ans)
                self.screen.remove_widget(self.ger_mensal)
                self.screen.remove_widget(self.pot_placas)
                self.screen.remove_widget(self.municipio)
                self.screen.remove_widget(self.n_placas)
                self.screen.remove_widget(self.pot_sist)
                self.screen.remove_widget(self.button_calcular)
                self.screen.remove_widget(self.button_corrigir)
                self.screen.remove_widget(self.logo1)

    def remove_tela2(self, type):
        if self.tela == 2:
            if type == "all":
                self.calculado = 0
                self.inf = 0
                self.screen.remove_widget(self.marca)
                self.screen.remove_widget(self.inversor)
                self.screen.remove_widget(self.pot_placas)
                self.screen.remove_widget(self.button_placas)
                self.screen.remove_widget(self.n_placas_ans)
                self.screen.remove_widget(self.button_marcas)
                self.screen.remove_widget(self.button_inversores)
                self.screen.remove_widget(self.button_placas)
                self.screen.remove_widget(self. button_inform)
                self.screen.remove_widget(self.button_limpar2)
                self.screen.remove_widget(self.disjuntor_ans)
                self.screen.remove_widget(self.cabos_ans)
      
    def remove_tela3(self, type):
        if self.tela == 3:

            if type == "input":
                self.screen.remove_widget(self.input_municipio)
                self.screen.remove_widget(self.input_pot_sistema)
            if type == "all":
                self.calculado = 0
                self.inf = 0
                self.screen.remove_widget(self.logo1)
                self.screen.remove_widget(self.municipio)
                self.screen.remove_widget(self.pot_sistema)
                self.screen.remove_widget(self.municipio_ans)
                self.screen.remove_widget(self.pot_sistema_ans)
                self.screen.remove_widget(self.geracao)
                self.screen.remove_widget(self.input_municipio)
                self.screen.remove_widget(self.input_pot_sistema)


        
    def calcular(self, args):
        potencia = 0
        try:
            pot_placas = int(self.input_pot_placas.text)
            n_placas = int(self.input_n_placas.text)
            if pot_placas in self.dados_placas:
                potencia = (pot_placas * n_placas) / 1000
                self.pot_sist.text = "Potência: " + str(round(potencia, 2)) + " kWp"
            else:
                self.pot_sist.text = "Potência de Placas Não Cadastrada"
        except:
            self.pot_sist.text = "Numero ou Potência das Placas Incorretos"
        try:
            fator_solar = 0
            for fator_solar_dados in self.fator_solares:
                distrito = self.fator_solares[0]
                if fator_solar_dados[0].lower() == self.input_municipio.text.lower():
                    fator_solar = fator_solar_dados[1]
            geracao = round(potencia * fator_solar, 2)
            if potencia > 0:
                if fator_solar > 0:
                    self.ger_mensal.text = "Geração Mensal: " + str(geracao) + " kWh"
                else:
                    self.ger_mensal.text = "Municipio Não Cadastrado"
            else:
                self.ger_mensal.text = ""
        except:
            self.ger_mensal.text = "Município Não Encontrado"
        # retira os campo os de input
        if self.calculado == 0:
            self.remove_tela1("input")
            self.screen.add_widget(self.municipio_ans)
            self.screen.add_widget(self.n_placas_ans)
            self.screen.add_widget(self.pot_placas_ans)
        self.calculado = 1
        # Mostrando respostas
        try:
            self.municipio_ans.text = self.input_municipio.text.upper() + " -> Fator Solar: " + str(fator_solar)
            self.n_placas_ans.text = self.input_n_placas.text
            self.pot_placas_ans.text = self.input_pot_placas.text
        except:
            print("Erro nas repostas")

    # Função para o botão Limpar
    def limpar(self, args):
        self.pot_sist.text = ""
        self.ger_mensal.text = ""
        if self.calculado == 1:
            self.remove_tela1("ans")
            self.screen.add_widget(self.input_municipio)
            self.screen.add_widget(self.input_n_placas)
            self.screen.add_widget(self.input_pot_placas)
        self.calculado = 0
        return 0

    # Função para o botão Limpar2
    def limpar2(self, args):
        self.screen.remove_widget(self.n_placas_ans)
        self.screen.remove_widget(self.disjuntor_ans)
        self.screen.remove_widget(self.cabos_ans)
        self.inf = 0

    # Função para o botão informações
    def inform(self,arg):
        self.n_placas_ans.text = "Número de Placas: "+self.button_placas.text
        if self.inf == 0:
            if self.button_placas.text == "Potência":
                self.n_placas_ans.text = "Potencia das placas não informada!"
            self.screen.add_widget(self.n_placas_ans)
            self.screen.add_widget(self.disjuntor_ans)
            self.screen.add_widget(self.cabos_ans)
        self.inf = 1

    def calcular3(self,args):
        potencia = 0
        try:
            potencia = float(self.input_pot_sistema.text)
        except:
            self.geracao.text = "Digite apenas numeros para descrever a potência"
        if  not self.geracao.text == "Digite apenas numeros" : 
            try:
                fator_solar = 0
                for fator_solar_dados in self.fator_solares:
                    distrito = self.fator_solares[0]
                    if fator_solar_dados[0].lower() == self.input_municipio.text.lower():
                        fator_solar = fator_solar_dados[1]
                geracao = round(potencia * fator_solar, 2)
                if potencia > 0:
                    if fator_solar > 0:
                        self.geracao.text = "Geração Mensal: " + str(geracao) + " kWh"
                    else:
                        self.ger_mensal.text = "Municipio Não Cadastrado"
                else:
                    self.geracao.text = "Digite a Potência do Sistema"
            except:
                self.ger_mensal.text = "Município Não Encontrado"
        # retira os campo os de input
        if self.calculado == 0:
            self.remove_tela3("input")
            self.screen.add_widget(self.municipio_ans)
            self.screen.add_widget(self.pot_sistema_ans)
        self.calculado = 1
        # Mostrando respostas
        try:
            self.municipio_ans.text = self.input_municipio.text.upper() + " -> Fator Solar: " + str(fator_solar)
            self.pot_sistema_ans.text = self.input_pot_sistema.text + " kWp"
        except:
            print("Erro nas repostas")

        
    def limpar3(self,args):
        self.geracao.text = ""
        self.calculado = 0
        self.screen.add_widget(self.input_municipio)
        self.screen.add_widget(self.input_pot_sistema)
        self.screen.remove_widget(self.municipio_ans)
        self.screen.remove_widget(self.pot_sistema_ans)

    # Arualiza a seleção de inversores com para os novos
    def atualizar_inversores(self,args):
        try:
            self.screen.remove_widget(self.button_inversores)
        except:
            print("Erro self.button_inversores nao existe")
        self.dropdown_inversores = DropDown()
        for index in self.Inversores:
            if index[0] == self.button_marcas.text:
                self.btn_inversores = Button(text= index[1], size_hint_y=None, height=44)
                self.btn_inversores.bind(on_release=lambda btn_inversores: self.dropdown_inversores.select(btn_inversores.text))
                self.dropdown_inversores.add_widget(self.btn_inversores)
        # create a big main button
        self.button_inversores = Button( pos_hint={"center_x": 0.5, "center_y": 0.57},text='Inversor', size_hint=(0.25, 0.072))
        self.button_inversores.bind(on_release=self.dropdown_inversores.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        

        self.dropdown_inversores.bind(on_select=lambda instance, x: setattr(self.button_inversores, 'text', x))
        
        self.screen.add_widget(self.button_inversores)
    


    # --------------------------------------------------------- TELAS ------------------------------------------------------------------------
    def tela1_andrid(self):
        # Logo
        self.logo1 = Image(
            source="logo.png",
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )
        self.screen.add_widget(self.logo1)

        # Labels Form ====================================================
        self.municipio = MDLabel(
            text="Município",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.n_placas = MDLabel(
            text="Número de Placas",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.54},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.pot_placas = MDLabel(
            text="Potência da Placa",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.42},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.screen.add_widget(self.municipio)
        self.screen.add_widget(self.n_placas)
        self.screen.add_widget(self.pot_placas)

        # Labels Answers ====================================================
        self.municipio_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.64},
            theme_text_color="Error",
            font_style="H5"
        )
        self.n_placas_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            theme_text_color="Error",
            font_style="H5"
        )
        self.pot_placas_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.36},
            theme_text_color="Error",
            font_style="H5"
        )
        self.pot_sist = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.28},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.ger_mensal = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.20},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.screen.add_widget(self.ger_mensal)
        self.screen.add_widget(self.pot_sist)

        # Inputs ===========================================================
        self.input_municipio = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.64},
            font_size=50
        )
        self.input_n_placas = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            font_size=50
        )
        self.input_pot_placas = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.36},
            font_size=50
        )
        self.screen.add_widget(self.input_municipio)
        self.screen.add_widget(self.input_n_placas)
        self.screen.add_widget(self.input_pot_placas)

        #  button ===========================================================
        self.button_calcular = MDFillRoundFlatButton(
            text="Calcular",
            font_size=17,
            pos_hint={"center_x": 0.8, "center_y": 0.1},
            on_press=self.calcular
        )
        self.screen.add_widget(self.button_calcular)

        self.button_corrigir = MDFillRoundFlatButton(
            text="Corrigir",
            font_size=17,
            pos_hint={"center_x": 0.2, "center_y": 0.1},
            on_press=self.limpar
        )
        self.screen.add_widget(self.button_corrigir)

    # Telas Para PC ========================================================   
    def tela1_pc(self):
        self.logo1 = Image(
            source="logo_pequena.png",
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )
        self.screen.add_widget(self.logo1)

        # Labels Form ====================================================
        self.municipio = MDLabel(
            text="Município",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.n_placas = MDLabel(
            text="Número de Placas",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.54},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.pot_placas = MDLabel(
            text="Potência da Placa",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.42},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.screen.add_widget(self.municipio)
        self.screen.add_widget(self.n_placas)
        self.screen.add_widget(self.pot_placas)

        # Labels Answers ====================================================
        self.municipio_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.64},
            theme_text_color="Error",
            font_style="H5"
        )
        self.n_placas_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            theme_text_color="Error",
            font_style="H5"
        )
        self.pot_placas_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.36},
            theme_text_color="Error",
            font_style="H5"
        )
        self.pot_sist = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.28},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.ger_mensal = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.20},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )

        self.screen.add_widget(self.ger_mensal)
        self.screen.add_widget(self.pot_sist)

        # Inputs ========================================================
        self.input_municipio = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.64},
            font_size=22
        )
        self.input_n_placas = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            font_size=22
        )
        self.input_pot_placas = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.36},
            font_size=22
        )
        self.screen.add_widget(self.input_municipio)
        self.screen.add_widget(self.input_n_placas)
        self.screen.add_widget(self.input_pot_placas)

        #  button =============================================================
        self.button_calcular = MDFillRoundFlatButton(
                text="Calcular",
                font_size=17,
                pos_hint={"center_x": 0.8, "center_y": 0.1},
                on_press=self.calcular
            )
        self.screen.add_widget(self.button_calcular)

        self.button_corrigir = MDFillRoundFlatButton(
            text="Corrigir",
            font_size=17,
            pos_hint={"center_x": 0.2, "center_y": 0.1},
            on_press=self.limpar
        )
        self.screen.add_widget(self.button_corrigir)


    def tela2_pc(self):
        # Labels Form ====================================================
        self.marca = MDLabel(
            text="Marca",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.80},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.inversor = MDLabel(
            text="Inversor",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.64},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.pot_placas = MDLabel(
            text="Potência da Placa",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.49},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.screen.add_widget(self.marca)
        self.screen.add_widget(self.inversor)
        self.screen.add_widget(self.pot_placas)

        # Buttons marcas ===========================================================
        self.dropdown_marcas = DropDown()
        for index in self.Marcas:
            btn_marcas = Button(text = index, size_hint_y=None, height=44)
            btn_marcas.bind(on_release=lambda btn_marcas: self.dropdown_marcas.select(btn_marcas.text))
            self.dropdown_marcas.add_widget(btn_marcas)
        # create a big main button
        self.button_marcas = Button(pos_hint={"center_x": 0.5, "center_y": 0.73},text='Marca', size_hint=(None, 0.072))
        self.button_marcas.bind(on_release=self.dropdown_marcas.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        self.dropdown_marcas.bind(on_select=lambda instance, x: setattr(self.button_marcas, 'text', x))
        self.dropdown_marcas.on_select = self.atualizar_inversores
        self.screen.add_widget(self.button_marcas)

        # Buttons inversores ===========================================================

        self.dropdown_inversores = DropDown()
        for index in self.Inversores:
            if index[0] == self.button_marcas.text:
                self.btn_inversores = Button(text= index[1], size_hint_y=None, height=44)
                self.btn_inversores.bind(on_release=lambda btn_inversores: self.dropdown_inversores.select(btn_inversores.text))
                self.dropdown_inversores.add_widget(self.btn_inversores)
        # create a big main button
        self.button_inversores = Button( pos_hint={"center_x": 0.5, "center_y": 0.57},text='Inversor', size_hint=(0.25, 0.072))
        self.button_inversores.bind(on_release=self.dropdown_inversores.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        

        self.dropdown_inversores.bind(on_select=lambda instance, x: setattr(self.button_inversores, 'text', x))
        
        self.screen.add_widget(self.button_inversores)
        
        # Buttons placas ===========================================================
        self.dropdown_placas = DropDown()
        for index in self.dados_placas:
            btn_placas = Button(text = str(index), size_hint_y=None, height=44)
            btn_placas.bind(on_release=lambda btn_placas: self.dropdown_placas.select(btn_placas.text))
            self.dropdown_placas.add_widget(btn_placas)
        # create a big main button
        self.button_placas = Button(pos_hint={"center_x": 0.5, "center_y": 0.42},text='Potência', size_hint=(None, 0.072))
        self.button_placas.bind(on_release=self.dropdown_placas.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        self.dropdown_placas.bind(on_select=lambda instance, x: setattr(self.button_placas, 'text', x))
        self.screen.add_widget(self.button_placas)

        # Answers ==================================================
        self.n_placas_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.34},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
        )
        self.disjuntor_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.28},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = "Disjuntor: 32 A "
        )
        self.cabos_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.22},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = "Cabos: 6 mm² "
        )

         # button =============================================================
        self.button_inform = MDFillRoundFlatButton(
        text="Informações",
        font_size=17,
        pos_hint={"center_x": 0.8, "center_y": 0.1},
        on_press=self.inform
        )
        
        self.button_limpar2 = MDFillRoundFlatButton(
            text="Limpar",
            font_size=17,
            pos_hint={"center_x": 0.2, "center_y": 0.1},
            on_press=self.limpar2
        )
        self.screen.add_widget(self.button_inform)
        self.screen.add_widget(self.button_limpar2)
        
    def tela3_pc(self):
        self.logo1 = Image(
            source="logo_pequena.png",
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )
        self.screen.add_widget(self.logo1)

        # Labels Form ====================================================
        self.municipio = MDLabel(
            text="Município",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
        )
        self.pot_sistema = MDLabel(
            text="Potência [kWp]",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.54},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.screen.add_widget(self.municipio)
        self.screen.add_widget(self.pot_sistema)

        # Labels label input ====================================================
        self.municipio_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.64},
            theme_text_color="Error",
            font_style="H5",
            text = ""
        )
        self.pot_sistema_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            theme_text_color="Error",
            font_style="H5",
            text = ""
        )
        

        # Labels Answers ====================================================
        self.geracao = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.30},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = ""
        )
       
        self.screen.add_widget(self.geracao)

        # Inputs ========================================================
        self.input_municipio = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.64},
            font_size=22
        )
        self.input_pot_sistema = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            font_size=22
        )
        self.screen.add_widget(self.input_municipio)
        self.screen.add_widget(self.input_pot_sistema)
         #  button =============================================================
        self.button_calcular3 = MDFillRoundFlatButton(
                text="Calcular",
                font_size=17,
                pos_hint={"center_x": 0.8, "center_y": 0.1},
                on_press=self.calcular3
            )
        self.screen.add_widget(self.button_calcular3)

        self.button_corrigir3 = MDFillRoundFlatButton(
            text="Corrigir",
            font_size=17,
            pos_hint={"center_x": 0.2, "center_y": 0.1},
            on_press=self.limpar3
        )
        self.screen.add_widget(self.button_corrigir3)
    def tela3_android():
        return 0
    #---------------------------------------------------------Principal---------------------------------------------------------
    def build(self):
        self.state = 0  # initial state
        self.theme_cls.primary_palette = "DeepOrange"
        self.toobar = MDToolbar()
        self.toobar.title = 'Calculadora Solar'
        self.toobar.pos_hint = {"top": 1}
        self.toobar.left_action_items = [["menu", lambda x: self.menu(x)]]
        # self.toobar.right_action_items = [["account-circle", lambda x: self.menu_user(x)]]
        self.screen.add_widget(self.toobar)

        # Menu Principal
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Geração Por Placas",
                "height": dp(56),
                "on_release": lambda x=1: self.menu_callback(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Info. - Inversores",
                "height": dp(56),
                "on_release": lambda x=2: self.menu_callback(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Geração por kWp",
                "height": dp(56),
                "on_release": lambda x=3: self.menu_callback(x),
            }
        ]
        self.menu_principal = MDDropdownMenu(
            items=menu_items,
            width_mult=3,
        )

        if self.tela == 1:
            if self.pc_android == 1:
                self.tela1_andrid()
            else:
                self.tela1_pc()
        if self.tela == 2: 
            if self.pc_android == 1:
                self.tela2_andrid()
            else:
                self.tela2_pc()
        if self.tela == 3: 
            if self.pc_android == 1:
                self.tela3_andrid()
            else:
                self.tela3_pc()
        return self.screen


if __name__ == '__main__':
    CalculadoraSolar().run()
