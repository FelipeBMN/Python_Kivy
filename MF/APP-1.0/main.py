import kivy

kivy.require('2.0.0')
import kivymd
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.core.window import Window


# Função principal =====================================================
class CalculadoraSolar(MDApp):

    # Dados Para o Programa =====================================================
    dados_placas = [
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

    dados_inversores = [['GROWATT', 'MID 15KTL3-X', '24,2', 25, 4, '22,5', 1000, 2, 2],
       ['GROWATT', 'MID 17KTL3-X', '27,4', 32, 6, '25,5', 1000, 2, 2],
       ['GROWATT', 'MID 20KTL3-X', '31,9', 32, 6, '30', 1000, 2, 2],
       ['GROWATT', 'MID 22KTL3-X', '35,5', 40, 6, '33', 1000, 2, 2],
       ['GROWATT', 'MID 25KTL3-X', '35,5', 40, 6, '37,5', 1000, 2, 3],
       ['GROWATT', 'MID 25KTL3-X', '40,2', 50, 10, '37,5', 1000, 2, 3],
       ['GROWATT', '7000MTL-S', '33,5', 40, 6, '9,1', 550, 2, 2],
       ['GROWATT', '8000MTL-S', '35,7', 40, 6, '10,5', 550, 2, 2],
       ['GROWATT', '7000MTL-S', '33,5', 40, 6, '9,1', 550, 2, 2],
       ['GROWATT', '8000MTL-S', '35,7', 40, 6, '10,5', 550, 2, 2],
       ['GROWATT', 'MIN 2500TL-X', '11,3', 16, 4, '3,5', 500, 2, 2],
       ['GROWATT', 'MIN 2500TL-X', '11,3', 16, 4, '4,2', 500, 2, 2],
       ['GROWATT', 'MIN 3600TL-X', '16', 20, 4, '5,04', 550, 2, 2],
       ['GROWATT', 'MIN 4200TL-X', '19', 20, 4, '5,88', 550, 2, 2],
       ['GROWATT', 'MIN 4600TL-X', '20,9', 25, 4, '6,44', 550, 2, 2],
       ['GROWATT', 'MIN 5000TL-X', '22,7', 25, 4, '7', 550, 2, 2],
       ['GROWATT', 'MIN 6000TL-X', '27,2', 25, 4, '8,1', 550, 2, 2],
       ['GROWATT', 'MAX 50KTL3 LV', '80,5', 100, 35, '65', 1100, 6, 2],
       ['GROWATT', 'MAX 60KTL3 LV', '96,6', 100, 35, '78', 1100, 6, 2],
       ['GROWATT', 'MAX 70KTL3 LV', '112,7', 125, 50, '91', 1100, 6, 2],
       ['GROWATT', 'MAX 80KTL3 LV', '128,8', 150, 70, '104', 1100, 6, 2],
       ['SOLIS', 'Solis-1P7K-4G', '33,7', 40, 6, '10,5', 600, 3, 3],
       ['SOLIS', 'Solis-1P8K-4G', '36,6', 40, 6, '12', 600, 3, 3],
       ['SOLIS', 'Solis-1P9K-4G', '41,3', 50, 16, '13,5', 600, 3, 3],
       ['SOLIS', 'Solis-1P10K-4G', '45,9', 50, 16, '15', 600, 3, 3],
       ['SOLIS', 'Solis-25K-5G', '41,8', 50, 16, '37,5', 1100, 3, 6],
       ['SOLIS', 'Solis-30K-5G', '50,2', 63, 16, '45', 1100, 3, 6],
       ['SOLIS', 'Solis-33K-5G', '55,1', 63, 16, '49,5', 1100, 3, 6],
       ['SOLIS', 'Solis-36K-5G', '60,2', 63, 16, '54', 1100, 4, 8],
       ['SOLIS', 'Solis-40K-5G', '66,9', 80, 25, '60', 1100, 4, 8],
       ['SOLIS', 'Solis-40K-HV-5G', '53', 63, 16, '60', 1100, 4, 8],
       ['SOLIS', 'Solis-50K-HV-5G', '66,2', 70, 25, '75', 1100, 4, 8],
       ['SOLIS', 'Solis-50K', '83,3', 100, 35, '75', 1100, 4, 12],
       ['SOLIS', 'Solis-50K-HV', '66,2', 70, 25, '75', 1100, 4, 8],
       ['SOLIS', 'Solis-60K-HV', '80', 100, 35, '90', 1100, 4, 12],
       ['SOLIS', 'Solis-60K-4G', '100', 125, 50, '90', 1100, 4, 12],
       ['SOLIS', 'Solis-75K-5G', '114', 125, 50, '120', 1100, 9, 18],
       ['SOLIS', 'Solis-80K-5G', '133,7', 150, 50, '120', 1100, 9, 18],
       ['SOLIS', 'Solis-1P2.5K-4G', '13,3', 16, 4, '3,75', 550, 2, 2],
       ['SOLIS', 'Solis-1P3K-4G', '15,7', 16, 4, '4,5', 600, 2, 2],
       ['SOLIS', 'Solis-1P3.6K-4G', '16', 20, 4, '5,4', 600, 2, 2],
       ['SOLIS', 'Solis-1P4K-4G', '21', 25, 4, '6', 600, 2, 2],
       ['SOLIS', 'Solis-1P4.6K-4G', '23,8', 25, 4, '6,9', 600, 2, 2],
       ['SOLIS', 'Solis-1P5K-4G', '25', 32, 6, '7,5', 600, 2, 2],
       ['SOLIS', 'Solis-1P6K-4G', '27,3', 32, 6, '9', 600, 2, 2],
       ['SOLIS', 'Solis-3P5K-4G', '7,9', 10, 4, '7,5', 1000, 2, 2],
       ['SOLIS', 'Solis-3P6K-4G', '9,5', 10, 4, '9', 1000, 2, 2],
       ['SOLIS', 'Solis-3P8K-4G', '12,7', 16, 4, '12', 1000, 2, 2],
       ['SOLIS', 'Solis-3P9K-4G', '14,3', 16, 4, '13,5', 1000, 2, 2],
       ['SOLIS', 'Solis-3P10K-4G', '15,9', 16, 4, '15', 1000, 2, 2],
       ['SOLIS', 'Solis-3P12K-4G', '19,1', 25, 4, '18', 1000, 2, 2],
       ['SOLIS', 'Solis-3P15K-4G', '23,8', 25, 4, '22,5', 1000, 2, 2],
       ['SOLIS', 'Solis-3P17K-4G', '27', 32, 6, '25,5', 1000, 2, 2],
       ['SOLIS', 'Solis-3P20K-4G', '31,8', 32, 6, '30', 1000, 2, 2],
       ['SMA', 'Sunny Tripower 15000TL', '29', 32, 6, '15', 1000, 3, 3],
       ['SMA', 'Sunny Tripower 20000TL', '29', 32, 6, '20', 1000, 3, 3],
       ['SMA', 'Sunny Tripower 25000TL', '36,2', 40, 6, '25', 1000, 3, 3],
       ['SMA', 'Sunny Tripower CORE1', '72,5', 80, 25, '75', 1000, 6, 12],
       ['LIVOLTEK', 'GT1-3K-S', '15', 16, 4, '4,4', 600, 1, 1],
       ['LIVOLTEK', 'GT1-5K-D', '25', 32, 6, '5,5', 600, 2, 2],
       ['LIVOLTEK', 'GT1-6K-D', '27,3', 32, 6, '8,8', 600, 2, 2],
       ['CANADIAN', 'CSI-3K-S22002-ED', '13,6', 16, 4, '4,45', 600, 1, 1],
       ['CANADIAN', 'CSI-5K-S22002-ED', '25', 32, 6, '8,19', 600, 2, 2],
       ['CANADIAN', 'CSI-5KTL1P-FL', '25', 32, 6, '6,5', 600, 2, 2],
       ['CANADIAN', 'CSI-7K-S22002-E', '35', 40, 6, '11,25', 600, 2, 2],
       ['CANADIAN', 'CSI-8KTL1P-GI-FL', '36,4', 40, 6, '10,8', 600, 2, 2],
       ['CANADIAN', 'CSI-15K-T400GL01-E', '23,8', 25, 4, '22,5', 1000, 2,
        4],
       ['CANADIAN', 'CSI-20KTL-GI-LFL', '31,8', 32, 6, '30', 1000, 2, 4],
       ['CANADIAN', 'CSI-25K-T400GL02-E', '41,8', 50, 16, '37,5', 1100,
        3, 6],
       ['CANADIAN', 'CSI-25KTL-GI-L', '65,6', 80, 25, '37,5', 1100, 2, 6],
       ['CANADIAN', 'CSI-30KTL-GI-L', '78,8', 80, 25, '45', 1100, 2, 6],
       ['CANADIAN', 'CSI-50KTL-GI', '76', 80, 25, '58', 1100, 4, 12],
       ['CANADIAN', 'CSI-60KTL-GI', '86,6', 100, 35, '72', 1100, 4, 8],
       ['CANADIAN', 'CSI-75K-T400GL02-E', '114', 125, 50, '112,5', 1100,
        9, 18],
       ['CANADIAN', 'CSI-100K-T400GL02-E', '152', 175, 95, '150', 1100,
        10, 20],
       ['LIVOLTEK', 'GT1 8K', '40', 50, 16, '13,2', 550, 2, 2],
       ['LIVOLTEK', 'GT1 10K', '45,5', 50, 16, '14,7', 550, 2, 2],
       ['LIVOLTEK', 'GT3-25K', '40', 50, 16, '27,5', 620, 2, 6],
       ['LIVOLTEK', 'GT3-30K', '48', 50, 16, '33', 620, 2, 6],
       ['HOYMILES', 'MI-1000', '4,54', 10, 4, '1', 60, 4, 4],
       ['HOYMILES', 'MI-1200', '5,45', 10, 4, '1,2', 60, 4, 4],
       ['HOYMILES', 'MI-1500', '6,2', 10, 4, '1.5', 60, 4, 4],
       ['HOYMILES', 'HMS-1800', '8,18', 10, 4, '1.8', 60, 4, 4],
       ['HOYMILES', 'HMS-2000', '9,09', 10, 4, '2', 60, 4, 4],
       ['GROWATT', 'MAC 30KTL3-X LV', '48,3', 50, 16, '45', 1100, 3, 9],
       ['GROWATT', 'MAC 40KTL3-X LV', '64,4', 80, 25, '60', 1100, 3, 9],
       ['GROWATT', 'MAC 50KTL3-X LV', '80,5', 100, 35, '75', 1100, 3, 9],
       ['GROWATT', 'MAC 60KTL3-X LV', '96,6', 100, 35, '90', 1100, 3, 12],
       ['CANADIAN', 'CSI-9K-S2202-E', '40,9', 50, 16, '13,5', 600, 2, 2]]

    dados_consumo = [['Aparelho de blu ray', 8, '2 h', '0,19'],
       ['Aparelho de DVD', 8, '2 h', '0,24'],
       ['Aparelho de som', 20, '3 h', '6,6'],
       ['Aquecedor de ambiente', 15, '8 h', '193,44'],
       ['Aquecedor de mamadeira', 30, '15 min', '0,75'],
       ['Aquecedor de marmita', 20, '30 min', '0,6'],
       ['Ar-condicionado tipo janela menor ou igual a 9.000 BTU/h', 30,
        '8 h', '128,8'],
       ['Ar-condicionado tipo janela de 9.001 a 14.000 BTU/h', 30, '8 h',
        '181,6'],
       ['Ar-condicionado tipo janela maior que 14.000 BTU/h', 30, '8 h',
        '374'],
       ['Ar-condicionado tipo split menor ou igual a 10.000 BTU/h', 30,
        '8 h', '142,28'],
       ['Ar-condicionado tipo split de 10.001 a 15.000 BTU/h', 30, '8 h',
        '193,76'],
       ['Ar-condicionado tipo split de 15.001 a 20.000 BTU/h', 30, '8 h',
        '293,68'],
       ['Ar-condicionado tipo split de 20.001 a 30.000 BTU/h', 30, '8 h',
        '439,2'],
       ['Ar-condicionado tipo split maior que 30.000 BTU/h', 30, '8 h',
        '679,2'],
       ['Aspirador de pó', 30, '20 min', '7,17'],
       ['Batedeira', 8, '20 min', '0,4'],
       ['Boiler elétrico de 200 L', 30, '24 h', '346,75'],
       ["Bomba d'água 1/2 cv", 30, '30 min', '7,2'],
       ["Bomba d'água 1/3 cv", 30, '30 min', '6,15'],
       ['Cafeteira elétrica', 30, '1 h', '6,56'],
       ['Cafeteira expresso', 30, '1 h', '23,82'],
       ['Chaleira elétrica', 30, '1 h', '28,23'],
       ['Churrasqueira elétrica', 5, '4 h', '76'],
       ['Chuveiro elétrico - 4500 W', 30, '32 min', '72'],
       ['Chuveiro elétrico - 5500 W', 30, '32 min', '88'],
       ['Computador', 30, '8 h', '15,12'],
       ['Enceradeira', 2, '2 h', '1,8'],
       ['Espremedor de frutas', 20, '10 min', '0,18'],
       ['Exaustor fogão', 30, '2 h', '9,96'],
       ['Fax modem em stand by', 30, '24 h', '2,16'],
       ['Ferro elétrico automático a seco - 1050 W', 12, '1 h', '2,4'],
       ['Ferro elétrico automático a vapor - 1200 W', 12, '1 h', '7,2'],
       ['Fogão elétrico - cook top\n(por queimador)', 30, '1 h', '68,55'],
       ['Forno elétrico', 30, '1 h', '15'],
       ['Forno micro-ondas - 25 L', 30, '20 min', '13,98'],
       ['Freezer vertical/horizontal', 30, '24 h', '47,55'],
       ['Freezer vertical frost free', 30, '24 h', '54'],
       ['Frigobar', 30, '24 h', '18,9'],
       ['Fritadeira elétrica', 15, '30 min', '6,81'],
       ['Furadeira', 4, '1 h', '0,94'],
       ['Geladeira 1 porta', 30, '24 h', '25,2'],
       ['Geladeira 1 porta frost free', 30, '24 h', '39,6'],
       ['Geladeira 2 portas', 30, '24 h', '48,24'],
       ['Geladeira 2 portas frost free', 30, '24 h', '56,88'],
       ['Grill', 10, '30 min', '3,2'],
       ['Home theater - 350 W', 8, '2 h', '5,6'],
       ['Impressora', 30, '1 h', '0,45'],
       ['Lâmpada fluorescente compacta - 11 W', 30, '5 h', '1,65'],
       ['Lâmpada fluorescente compacta - 15 W', 30, '5 h', '2,25'],
       ['Lâmpada fluorescente compacta - 23 W', 30, '5 h', '3,45'],
       ['Lâmpada incandescente - 40 W', 30, '5 h', '6'],
       ['Lâmpada incandescente - 60 W', 30, '5 h', '9'],
       ['Lâmpada incandescente - 100 W', 30, '5 h', '15'],
       ['Lavadora de louças', 30, '40 min', '30,86'],
       ['Lavadora de roupas', 12, '1 h', '1,76'],
       ['Liquidificador', 15, '15 min', '0,8'],
       ['Máquina de costura', 10, '3 h', '3'],
       ['Modem de internet', 30, '8 h', '1,92'],
       ['Monitor', 30, '8 h', '13,2'],
       ['Monitor LCD', 30, '8 h', '8,16'],
       ['Multiprocessador', 20, '1 h', '8,56'],
       ['Nebulizador', 16, '2,5 h', '1,68'],
       ['Notebook', 30, '8 h', '4,8'],
       ['Panela elétrica', 20, '1 h', '22'],
       ['Prancha (chapinha)', 20, '30 min', '0,33'],
       ['Projetor', 20, '1 h', '4,78'],
       ['Rádio elétrico pequeno', 30, '10 h', '1,5'],
       ['Rádio relógio', 30, '24 h', '3,6'],
       ['Roteador', 30, '8 h', '1,44'],
       ['Sanduicheira', 30, '10 min', '3,35'],
       ['Scanner', 30, '1 h', '0,27'],
       ['Secador de cabelo - 1000 W', 30, '10 min', '5,21'],
       ['Secadora de roupa', 8, '1 h', '14,92'],
       ['Tanquinho', 12, '1 h', '0,84'],
       ['Telefone sem fio', 30, '24 h', '2,16'],
       ['Torneira elétrica - 3250 W', 30, '30 min', '48,75'],
       ['Torradeira', 30, '10 min', '4'],
       ['TV em cores - 14" (tubo)', 30, '5 h', '6,3'],
       ['TV em cores - 29" (tubo)', 30, '5 h', '15,15'],
       ['TV em cores - 32" (LCD)', 30, '5 h', '14,25'],
       ['TV em cores - 40" (LED)', 30, '5 h', '12,45'],
       ['TV em cores - 42" (LED)', 30, '5 h', '30,45'],
       ['TV portátil', 30, '5 h', '7,05'],
       ['Ventilador de mesa', 30, '8 h', '17,28'],
       ['Ventilador de teto', 30, '8 h', '17,52'],
       ['Videogame', 15, '4 h', '1,44']]         
    # Variaveis do Programa =======================]==============================
    tela = 4
    pc_android = 1
    calculado = 0
    inf = 0
    screen = MDScreen()

    # Funções para o Menu =====================================================


    def menu(self, button):
        if self.tela != 4: 
            self.ir_tela4()
        return 0



    def ir_tela1(self, args):
        if self.tela == 2:
            self.remove_tela2("all")
        if self.tela == 3:
            self.remove_tela3("all")
        if self.tela == 4:
            self.remove_tela4("all")
        if self.tela == 4:
            self.remove_tela5("all")

        if self.pc_android == 1:
            self.tela1_android()
        else:
            self.tela1_pc()
        self.tela = 1
        
    
    def ir_tela2(self, args):
        if self.tela == 1:
            self.remove_tela1("all")
        if self.tela == 3:
            self.remove_tela3("all")
        if self.tela == 4:
            self.remove_tela4("all")
        if self.tela == 5:
            self.remove_tela5("all")
        if self.pc_android == 1:
            self.tela2_android()
        else:
            self.tela2_pc()
        self.tela = 2
    
    def ir_tela3(self, args):
        if self.tela == 1:
            self.remove_tela1("all")
        if self.tela == 2:
            self.remove_tela2("all")
        if self.tela == 4:
            self.remove_tela4("all")
        if self.tela == 5:
            self.remove_tela5("all")
        if self.pc_android == 1:
            self.tela3_android()
        else:
            self.tela3_pc()
        self.tela = 3

    def ir_tela4(self):
        if self.tela == 1:
            self.remove_tela1("all")
        if self.tela == 2:
            self.remove_tela2("all")
        if self.tela == 3:
            self.remove_tela3("all")
        if self.tela == 5:
            self.remove_tela5("all")
        if self.pc_android == 1:
            self.tela4_android()
        else:
            self.tela4_pc()
        self.tela = 4

    def ir_tela5(self, args):
        if self.tela == 1:
            self.remove_tela1("all")
        if self.tela == 2:
            self.remove_tela2("all")
        if self.tela == 4:
            self.remove_tela4("all")
        if self.pc_android == 1:
            self.tela5_android()
        else:
            self.tela5_pc()
        self.tela = 5
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
                #self.screen.remove_widget(self.logo1)
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
                self.screen.remove_widget(self.disjuntor_ans)
                self.screen.remove_widget(self.potencia_inv_ans)
                self.screen.remove_widget(self.cabos_ans)
                
      
    def remove_tela3(self, type):
        if self.tela == 3:

            if type == "input":
                self.screen.remove_widget(self.input_municipio)
                self.screen.remove_widget(self.input_pot_sistema)
                self.screen.remove_widget(self.input_pot_sistema_kwh)

            if type == "all":
                self.calculado = 0
                self.inf = 0
                #self.screen.remove_widget(self.logo1)
                self.screen.remove_widget(self.municipio)
                self.screen.remove_widget(self.pot_sistema)
                self.screen.remove_widget(self.pot_sistema_kwh)
                self.screen.remove_widget(self.municipio_ans)
                self.screen.remove_widget(self.pot_sistema_ans)
                self.screen.remove_widget(self.pot_sistema_kwh_ans)
                self.screen.remove_widget(self.geracao)
                self.screen.remove_widget(self.input_municipio)
                self.screen.remove_widget(self.button_calcular3)
                self.screen.remove_widget(self.button_corrigir3)
                self.screen.remove_widget(self.input_pot_sistema)
                self.screen.remove_widget(self.input_pot_sistema_kwh)
                

    def remove_tela4(self, type):
        if type == "all":
            self.screen.remove_widget(self.logo1)
            self.screen.remove_widget(self.button_tela1)
            self.screen.remove_widget(self.button_tela2)
            self.screen.remove_widget(self.button_tela3)
            self.screen.remove_widget(self.Menu)
            self.screen.remove_widget(self.button_tela5)
    
    def remove_tela5(self, type):
        if self.tela == 5:
            if type == "all":
                self.calculado = 0
                self.inf = 0
                #self.screen.remove_widget(self.logo1)
                self.screen.remove_widget(self.equipamento)
                self.screen.remove_widget(self.equipamento_ans)
                self.screen.remove_widget(self.equipamento_horas_ans)
                self.screen.remove_widget(self.button_consumo)

   

    # botoes =================================================================
    def calcular(self, args):
        potencia = 0
        erro = 0
        fator_solar = 0
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
            erro = 1

        if erro == 0 :  
            try:
                fator_solar = 0
                for fator_solar_dados in self .fator_solares:
                    municipio = self.input_municipio.text.lower().split()[0]
                    if fator_solar_dados[0].lower() == municipio:
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
        self.screen.remove_widget(self.potencia_inv_ans)
        self.screen.remove_widget(self.disjuntor_ans)
        self.screen.remove_widget(self.cabos_ans)
        self.inf = 0

    # Função para o botão informações
    def inform(self,arg):
        n_placas = 0
        disj_encontrado = 0
        vet_inversores = self.dados_inversores
        for i in range(len(vet_inversores)):
            if (vet_inversores[i][1]==self.button_inversores.text):
                potencia_maxima = float(vet_inversores[i][5].replace(',','.')) * 1000
                self.potencia_inv_ans.text = "Potência Max. Inv. : " + str(potencia_maxima/1000) + " kWp"
                if not(self.button_placas.text == "Potência") :
                    tensao_maxima = float(vet_inversores[i][6])
                    tensao_placa = 50
                    n_mppt = vet_inversores[i][8]
                    print("mppt: ",n_mppt)
                    print("tensão: ", tensao_maxima)
                    n_placas_1 = potencia_maxima / int(self.button_placas.text)
                    n_placas_2 = int(tensao_maxima / tensao_placa) * n_mppt
                    print("N placas por potencia",n_placas_1)
                    print("N placas por tensão",n_placas_2)
                    if (n_placas_1 > n_placas_2):
                        self.n_placas_ans.text = "Número de Placas: " + str(int(n_placas_2)) + " (VERIFICAR)"
                    else:
                        self.n_placas_ans.text = "Número de Placas: " + str(int(n_placas_1))
                self.disjuntor_ans.text = "Disjuntor: " + str(vet_inversores[i][3]) + " A"
                self.cabos_ans.text = "Cabos :" + str(vet_inversores[i][4]) + " mm²"
                disj_encontrado = 1
                break
        if self.button_placas.text == "Potência":
            self.n_placas_ans.text = "Potencia das placas não informada!"
        if (disj_encontrado == 0):
            self.n_placas_ans.text = "Informações do Disjuntor Não Encontrada"
            self.disjuntor_ans.text = ""
            self.cabos_ans.text = "" 
        if self.inf == 0:
            self.screen.add_widget(self.n_placas_ans)
            self.screen.add_widget(self.disjuntor_ans)
            self.screen.add_widget(self.potencia_inv_ans)
            self.screen.add_widget(self.cabos_ans)
        self.inf = 1

    def calcular3(self,args):
        potencia = 0
        erro = 0
        fator_solar = 0
        self.calculado = 1 
        print(self.input_pot_sistema.text)
        if self.input_pot_sistema.text.strip(" ") != "" and self.input_pot_sistema_kwh.text.strip(" ") == "":
            print("kwp")
            try:
                potencia_sem_virgula = self.input_pot_sistema.text.replace(",",".")
                potencia = float(potencia_sem_virgula)
            except:
                self.geracao.text = "Digite apenas numeros para descrever a potência"
                erro = 1

            if erro == 0 :
                try:
                    fator_solar = 0
                    municipio = self.input_municipio.text.lower().split()[0]
                    print(municipio)
                    for fator_solar_dados in self.fator_solares:
                        if fator_solar_dados[0].lower() == municipio:
                            fator_solar = fator_solar_dados[1]
                    geracao = round(potencia * fator_solar, 2)
                    if potencia > 0:
                        if fator_solar > 0:
                            self.geracao.text = "Geração Mensal: " + str(geracao) + " kWh"
                        else:
                            self.geracao.text = "Municipio Não Cadastrado"
                    else:
                        self.geracao.text = "Digite a Potência do Sistema"
                except:
                    self.geracao.text = "Município Não Encontrado"

                # retira os campo os de input
                if self.calculado == 0:
                    self.remove_tela3("input")
                    self.screen.add_widget(self.municipio_ans)
                self.calculado = 1
                # Mostrando respostas
                try:
                    self.municipio_ans.text = self.input_municipio.text.upper() + " -> Fator Solar: " + str(fator_solar)
                    self.pot_sistema_ans.text = self.input_pot_sistema.text + " kWp"
                except:
                    print("Erro nas repostas")
        elif self.input_pot_sistema_kwh.text.strip(" ") != "" and self.input_pot_sistema.text.strip(" ") == "":
            print("iniciando calculo kwh")
            try:
                potencia_sem_virgula = self.input_pot_sistema_kwh.text.replace(",",".")
                potencia = float(potencia_sem_virgula)
            except:
                self.geracao_kwh.text = "Digite apenas numeros para descrever a potência"
                erro = 1
            try:
                fator_solar = 0
                municipio = self.input_municipio.text.lower().split()[0]
                print(municipio)
                for fator_solar_dados in self.fator_solares:
                    if fator_solar_dados[0].lower() == municipio:
                        fator_solar = fator_solar_dados[1]
                geracao = round(potencia / fator_solar, 2)
                if potencia > 0:
                    if fator_solar > 0:
                        self.geracao_kwh.text = "Geração Mensal: " + str(geracao) + " kWh"
                    else:
                        self.geracao_kwh.text = "Municipio Não Cadastrado"
                else:
                    self.geracao_kwh.text = "Digite a Potência do Sistema"
            except:
                self.geracao_kwh.text = "Município Não Encontrado"
            try:
                    self.municipio_ans.text = self.input_municipio.text.upper() + " -> Fator Solar: " + str(fator_solar)
                    self.pot_sistema_kwh_ans.text = self.input_pot_sistema_kwh.text + " kWp"
            except:
                    print("Erro nas repostas")
        else:
            self.geracao_kwh.text = "Deixe um desses campos em branco"
            self.geracao.text = "Deixe um desses campos em branco"

        self.calculado = 1
        self.screen.remove_widget(self.input_municipio)
        self.screen.remove_widget(self.input_pot_sistema)
        self.screen.remove_widget(self.input_pot_sistema_kwh)

    def limpar3(self,args):
        self.geracao.text = ""
        self.geracao_kwh.text = ""
        if self.calculado == 1: 
            self.screen.add_widget(self.input_municipio)
            self.screen.add_widget(self.input_pot_sistema)
            self.screen.add_widget(self.input_pot_sistema_kwh)
            self.municipio_ans.text = " "
            self.pot_sistema_ans.text = " "
            self.pot_sistema_kwh_ans.text = " "

        self.calculado = 0

    # Arualiza a seleção de inversores com para os novos
    def atualizar_inversores(self,args):
        try:
            self.screen.remove_widget(self.button_inversores)
        except:
            print("Erro self.button_inversores nao existe")
        self.dropdown_inversores = DropDown()
        for index in self.Inversores:
            if index[0] == self.button_marcas.text:
                self.btn_inversores = Button(text= index[1], size_hint_y=None, height=100)
                self.btn_inversores.bind(on_release=lambda btn_inversores: self.dropdown_inversores.select(btn_inversores.text))
                self.dropdown_inversores.add_widget(self.btn_inversores)
        # create a big main button
        self.button_inversores = Button( pos_hint={"center_x": 0.5, "center_y": 0.62},text='Inversor', size_hint=(0.6, 0.072), background_color = (0.,0.,0.,0.9))
        self.button_inversores.bind(on_release=self.dropdown_inversores.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        

        self.dropdown_inversores.bind(on_select=lambda instance, x: setattr(self.button_inversores, 'text', x))
        self.dropdown_inversores.on_select = self.inform
        self.screen.add_widget(self.button_inversores)
    
    # Funções do teclado
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key, *args):
        if (key==27 and not(self.tela == 4)):
            self.ir_tela4()
        return True
    # Funções para tela 5
    def limpar4(self,args):
        self.equipamento_ans.text = ""
        self.calculado = 0
        self.screen.remove_widget(self.pot_consumo_ans)

    def mostrar(self,args):
        for index in self.dados_consumo:
            if str(self.button_consumo.text.strip(" ")) == str(index[0].strip(" ")):
                self.equipamento_ans.text = "Consumo Mensal: " + index[3] + " kWh"
                self.equipamento_horas_ans.text =  "Utilização Diaria: " + index[2] 
  
    #-------------------------------------------------------- TELAS ------------------------------------------------------------------------
    def tela1_android(self):
        self.toobar.left_action_items = [["backburger", lambda x: self.menu(x)]]
        # Logo
        # self.logo1 = Image(
        #     source="logo.png",
        #     pos_hint={"center_x": 0.5, "center_y": 0.8}
        # )
        # self.screen.add_widget(self.logo1)

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
            font_size=60
        )
        self.input_n_placas = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            font_size=60
        )
        self.input_pot_placas = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.36},
            font_size=60
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
            text="Alterar",
            font_size=17,
            pos_hint={"center_x": 0.2, "center_y": 0.1},
            on_press=self.limpar
        )
        self.screen.add_widget(self.button_corrigir)

    # Telas Para PC ========================================================   
    def tela1_pc(self):
        #self.logo1 = Image(
        #    source="logo_pequena.png",
        #    pos_hint={"center_x": 0.5, "center_y": 0.8}
        #)
        #self.screen.add_widget(self.logo1)

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

        #  button ========================================================
        self.button_calcular = MDFillRoundFlatButton(
                text="Calcular",
                font_size=17,
                pos_hint={"center_x": 0.8, "center_y": 0.1},
                on_press=self.calcular
            )
        self.screen.add_widget(self.button_calcular)

        self.button_corrigir = MDFillRoundFlatButton(
            text="Alterar",
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
            btn_marcas = Button(text = index, size_hint_y=None, height=100, background_color = (0.,0.,0.,0.9))
            btn_marcas.bind(on_release=lambda btn_marcas: self.dropdown_marcas.select(btn_marcas.text))
            self.dropdown_marcas.add_widget(btn_marcas)
        # create a big main button
        self.button_marcas = Button(pos_hint={"center_x": 0.5, "center_y": 0.73},text='Marca', size_hint=(0.6, 0.072))
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
                self.btn_inversores = Button(text= index[1], size_hint_y=None, height=100, background_color = (0.,0.,0.,0.9))
                self.btn_inversores.bind(on_release=lambda btn_inversores: self.dropdown_inversores.select(btn_inversores.text))
                self.dropdown_inversores.add_widget(self.btn_inversores)
        # create a big main button
        self.button_inversores = Button( pos_hint={"center_x": 0.5, "center_y": 0.57},text='Inversor', size_hint=(0.6, 0.072))
        self.button_inversores.bind(on_release=self.dropdown_inversores.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        

        self.dropdown_inversores.bind(on_select=lambda instance, x: setattr(self.button_inversores, 'text', x))
        
        self.screen.add_widget(self.button_inversores)
        
        # Buttons placas ===========================================================
        self.dropdown_placas = DropDown()
        for index in self.dados_placas:
            btn_placas = Button(text = str(index), size_hint_y=None, height=100, background_color = (0.,0.,0.,0.9))
            btn_placas.bind(on_release=lambda btn_placas: self.dropdown_placas.select(btn_placas.text))
            self.dropdown_placas.add_widget(btn_placas)
        # create a big main button
        self.button_placas = Button(pos_hint={"center_x": 0.5, "center_y": 0.42},text='Potência', size_hint=(0.6, 0.072))
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

    def tela2_android(self):
        self.toobar.left_action_items = [["backburger", lambda x: self.menu(x)]]
        # Labels Form ====================================================
        self.marca = MDLabel(
            text="Marca",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.inversor = MDLabel(
            text="Inversor",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.69},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.pot_placas = MDLabel(
            text="Potência da Placa",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.54},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.screen.add_widget(self.marca)
        self.screen.add_widget(self.inversor)
        self.screen.add_widget(self.pot_placas)

        # Buttons marcas ===========================================================
        self.dropdown_marcas = DropDown()
        for index in self.Marcas:
            btn_marcas = Button(text = index, size_hint_y=None, height=100)
            btn_marcas.bind(on_release=lambda btn_marcas: self.dropdown_marcas.select(btn_marcas.text))
            self.dropdown_marcas.add_widget(btn_marcas)
        # create a big main button
        self.button_marcas = Button(pos_hint={"center_x": 0.5, "center_y": 0.77},text='Marca', size_hint=(0.60, 0.1),background_color = (0.,0.,0.,0.9))
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
                self.btn_inversores = Button(text= index[1], size_hint_y=None, height=100)
                self.btn_inversores.bind(on_release=lambda btn_inversores: self.dropdown_inversores.select(btn_inversores.text))
                self.dropdown_inversores.add_widget(self.btn_inversores)
        # create a big main button
        self.button_inversores = Button( pos_hint={"center_x": 0.5, "center_y": 0.62},text='Inversor', size_hint=(0.60, 0.1),background_color = (0.,0.,0.,0.9))
        self.button_inversores.bind(on_release=self.dropdown_inversores.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        

        self.dropdown_inversores.bind(on_select=lambda instance, x: setattr(self.button_inversores, 'text', x))
        self.dropdown_inversores.on_select = self.inform
        self.screen.add_widget(self.button_inversores)
        
        # Buttons placas ===========================================================
        self.dropdown_placas = DropDown()
        for index in self.dados_placas:
            btn_placas = Button(text = str(index), size_hint_y=None, height=100)
            btn_placas.bind(on_release=lambda btn_placas: self.dropdown_placas.select(btn_placas.text))
            self.dropdown_placas.add_widget(btn_placas)
        # create a big main button
        self.button_placas = Button(pos_hint={"center_x": 0.5, "center_y": 0.47},text='Potência', size_hint=(0.60, 0.1), background_color = (0.,0.,0.,0.9))
        self.button_placas.bind(on_release=self.dropdown_placas.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        self.dropdown_placas.bind(on_select=lambda instance, x: setattr(self.button_placas, 'text', x))
        self.dropdown_placas.on_select = self.inform
        self.screen.add_widget(self.button_placas)

        # Answers ==================================================
        self.potencia_inv_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.32},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
        )
        self.n_placas_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.27},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
        )
        self.cabos_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.22},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = ""
        )
        self.disjuntor_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = ""
        )

         # button ============================================================= 
        

    def tela3_pc(self):
        #self.logo1 = Image(
        #    source="logo_pequena.png",
        #    pos_hint={"center_x": 0.5, "center_y": 0.8}
        #)
        #self.screen.add_widget(self.logo1)

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
        self.pot_sistema_kwh = MDLabel(
            text="Potência [kWh]",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.38},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.screen.add_widget(self.municipio)
        self.screen.add_widget(self.pot_sistema)
        self.screen.add_widget(self.pot_sistema_kwh)

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
            text = "teste 2"
        )
        self.pot_sistema_kwh_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.32},
            theme_text_color="Error",
            font_style="H5",
            text = "teste 1"
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
        self.input_pot_sistema_kwh = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            font_size=22
        )
        self.screen.add_widget(self.input_municipio)
        self.screen.add_widget(self.input_pot_sistema)
        self.screen.add_widget(self.input_pot_sistema_kwh)
        # button =============================================================
        self.button_calcular3 = MDFillRoundFlatButton(
                text="Calcular",
                font_size=17,
                pos_hint={"center_x": 0.8, "center_y": 0.1},
                on_press=self.calcular3
            )
        self.screen.add_widget(self.button_calcular3)

        self.button_corrigir3 = MDFillRoundFlatButton(
            text="Alterar",
            font_size=17,
            pos_hint={"center_x": 0.2, "center_y": 0.1},
            on_press=self.limpar3
        )
        self.screen.add_widget(self.button_corrigir3)
    

    def tela3_android(self):
        self.toobar.left_action_items = [["backburger", lambda x: self.menu(x)]]
        self.toobar.left_action_items = [["backburger", lambda x: self.menu(x)]]
        #self.logo1 = Image(
        #    source="logo_pequena.png",
        #    pos_hint={"center_x": 0.5, "center_y": 0.8}
        #)
        #self.screen.add_widget(self.logo1)

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
        self.pot_sistema_kwh = MDLabel(
            text="Potência [kWh]",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.38},
            theme_text_color="ContrastParentBackground",
            font_style="H5"
        )
        self.screen.add_widget(self.municipio)
        self.screen.add_widget(self.pot_sistema)
        self.screen.add_widget(self.pot_sistema_kwh)

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
        self.pot_sistema_kwh_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.32},
            theme_text_color="Error",
            font_style="H5",
            text = ""
        )
        
        self.screen.add_widget(self.municipio_ans)
        self.screen.add_widget(self.pot_sistema_ans)
        self.screen.add_widget(self.pot_sistema_kwh_ans)

        # Labels Answers ====================================================
        self.geracao_kwh = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = ""
        )

        self.geracao = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.30},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = ""
        )
       
        self.screen.add_widget(self.geracao)
        self.screen.add_widget(self.geracao_kwh)

        # Inputs ========================================================
        self.input_municipio = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.64},
            font_size=60
        )
        self.input_pot_sistema = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.48},
            font_size=60
        )
        self.input_pot_sistema_kwh = MDTextField(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.32},
            font_size=60
        )
        self.screen.add_widget(self.input_municipio)
        self.screen.add_widget(self.input_pot_sistema)
        self.screen.add_widget(self.input_pot_sistema_kwh)
        # button =============================================================
        self.button_calcular3 = MDFillRoundFlatButton(
                text="Calcular",
                font_size=17,
                pos_hint={"center_x": 0.8, "center_y": 0.1},
                on_press=self.calcular3
            )
        self.screen.add_widget(self.button_calcular3)

        self.button_corrigir3 = MDFillRoundFlatButton(
            text="Alterar",
            font_size=17,
            pos_hint={"center_x": 0.2, "center_y": 0.1},
            on_press=self.limpar3
        )
        self.screen.add_widget(self.button_corrigir3)
        
        
        
    
    # Tela 4 ================================================================================
    def tela4_pc(self):
        self.logo1 = Image(
            source="logo_pequena.png",
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )
        self.screen.add_widget(self.logo1)
        # Labels Form ====================================================
        self.Menu = Image(
            source="menu.png",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            size = {"x":0.5,"y":0.5}
        )
        self.screen.add_widget(self.Menu)

        # button =============================================================
        self.button_tela1 = MDFillRoundFlatButton(
            text="Sistema por Modulos",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            on_press=self.ir_tela1
        )
        self.screen.add_widget(self.button_tela1)

        self.button_tela2 = MDFillRoundFlatButton(
            text="Inversores",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_press=self.ir_tela2
        )
        self.screen.add_widget(self.button_tela2)

        self.button_tela3 = MDFillRoundFlatButton(
            text="Sistema por kWp",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            on_press=self.ir_tela3
        )
        self.screen.add_widget(self.button_tela3)
        

        self.button_tela5 = MDFillRoundFlatButton(
            text="Sistema por Consumo",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_press=self.ir_tela5
        )
        self.screen.add_widget(self.button_tela5)



    def tela4_android(self):
        self.toobar.left_action_items = [["menu", lambda x: self.menu(x)]]
        self.logo1 = Image(
            source="logomenu.png",
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )
        self.screen.add_widget(self.logo1)
        # Labels Form ====================================================
        self.Menu = Image(
            source="menu.png",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
        )
        self.screen.add_widget(self.Menu)
        # button =============================================================
        self.button_tela1 = MDFillRoundFlatButton(
            text=" Geração - Modulo",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_press=self.ir_tela1
        )
        self.screen.add_widget(self.button_tela1)

        self.button_tela2 = MDFillRoundFlatButton(
            text="Dados Inversores",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            on_press=self.ir_tela2
        )
        self.screen.add_widget(self.button_tela2)

        self.button_tela3 = MDFillRoundFlatButton(
            text="Geração - kWp",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_press=self.ir_tela3
        )
        self.screen.add_widget(self.button_tela3)

        self.button_tela5 = MDFillRoundFlatButton(
            text="Consumo de Equipamentos",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_press=self.ir_tela5
        )
        self.screen.add_widget(self.button_tela5)
        
    def tela5_pc(self):
        return 0

    def tela5_android(self):
        self.toobar.left_action_items = [["backburger", lambda x: self.menu(x)]]
        #self.logo1 = Image(
        #    source="logo_pequena.png",
        #    pos_hint={"center_x": 0.5, "center_y": 0.8}
        #)
        #self.screen.add_widget(self.logo1)

        # Labels Form ====================================================
        self.equipamento = MDLabel(
            text="Equipamento",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
        )

        self.screen.add_widget(self.equipamento)
        

        # Labels Answers ====================================================
        
        self.equipamento_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = ""
        )
       
        self.screen.add_widget(self.equipamento_ans)

        self.equipamento_horas_ans = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.30},
            theme_text_color="ContrastParentBackground",
            font_style="H5",
            text = ""
        )
        self.screen.add_widget(self.equipamento_horas_ans)


        # Inputs ========================================================
        self.dropdown_consumo = DropDown()
        print(self.dados_consumo[1][1])
        for index in self.dados_consumo:
            btn_consumo = Button(text = index[0], size_hint_y=None, height=100, background_color = (0.,0.,0.,0.9))
            btn_consumo.bind(on_release=lambda btn_consumo: self.dropdown_consumo.select(btn_consumo.text))
            self.dropdown_consumo.add_widget(btn_consumo)
        # create a big main button
        self.button_consumo = Button(pos_hint={"center_x": 0.5, "center_y": 0.73},text='Equipamento', size_hint=(0.6, 0.072))
        self.button_consumo.bind(on_release=self.dropdown_consumo.open)
        self.dropdown_consumo.on_select = self.mostrar
        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        self.dropdown_consumo.bind(on_select=lambda instance, x: setattr(self.button_consumo, 'text', x))
        self.screen.add_widget(self.button_consumo)

        
    #---------------------------------------------------------Principal---------------------------------------------------------
    def build(self):
        self.state = 0  # initial state
        self.theme_cls.primary_palette = "DeepOrange"
        self.toobar = MDToolbar()
        self.toobar.title = 'Calculadora Solar'
        self.toobar.pos_hint = {"top": 1}
        self.toobar.left_action_items = [["menu", lambda x: self.menu(x)]]
        self.screen.add_widget(self.toobar)
        self.icon = "logo256.png"
        self.ir_tela4()
        self.on_pre_enter()
        return self.screen


if __name__ == '__main__':
    CalculadoraSolar().run()
