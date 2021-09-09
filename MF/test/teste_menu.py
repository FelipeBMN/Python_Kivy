from kivymd.app import MDApp
from kivy.lang import Builder

colors = {
    "Teal": {
        "50": "e4f8f9",
        "100": "bdedf0",
        "200": "97e2e8",
        "300": "79d5de",
        "400": "6dcbd6",
        "500": "6ac2cf",
        "600": "63b2bc",
        "700": "5b9ca3",
        "800": "54888c",
        "900": "486363",
        "A100": "bdedf0",
        "A200": "97e2e8",
        "A400": "6dcbd6",
        "A700": "5b9ca3",
    },
    "Blue": {
        "50": "e3f3f8",
        "100": "b9e1ee",
        "200": "91cee3",
        "300": "72bad6",
        "400": "62acce",
        "500": "589fc6",
        "600": "5191b8",
        "700": "487fa5",
        "800": "426f91",
        "900": "35506d",
        "A100": "b9e1ee",
        "A200": "91cee3",
        "A400": "62acce",
        "A700": "487fa5",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },
    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    }
}

class Test(MDApp):

    def build(self):
        self.state = 0 #initial state
        #self.theme_cls.colors = colors
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.surface_palette = "DeepOrange"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:    

        title: 'CalculadoraSolar'
        md_bg_color: 1, 0.15, 0.10, 1
        specific_text_color: 1, 1, 1, 1
        left_action_items: [["alarm-panel-outline", lambda x: False]]

    MDBottomNavigation:
        panel_color: 1, 0.15, 0.10, 1
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Fator Solar'
            icon: 'weather-sunny'
            adaptive_height: True
            orientation: 'vertical'  

            MDBoxLayout:
                adaptive_height: True
                orientation: 'vertical'  
                spacing: dp(10)
                padding: dp(10)

                MDTextField:
                    hint_text: "Rectangle mode"
                    mode: "rectangle"
                    size_hint_x: None
                    width: "300dp"
                    hint_text: "Quantidade de KW Desejada"
                    pos_hint: {"center_x": .5, "center_y": 0.5}  
                    halign: "center"  

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Fios'
            icon: 'cable-data'

            MDLabel:
                text: 'I programming of C++'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Inversores'
            icon: 'alpha-i-box-outline'

            MDLabel:
                orientation:'vertical'
                text: 'JS'
                halign: 'center'                
'''
        )


Test().run()