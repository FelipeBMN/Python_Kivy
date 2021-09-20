from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


class Test(MDApp):

    def build(self):
        self.state = 0 #initial state
        #self.theme_cls.colors = colors
        self.theme_cls.theme_style = "Dark"
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
        right_action_items: [["alarm-panel-outline", lambda x: False]]
    MDBottomNavigation:
        

        panel_color: 1, 0.15, 0.10, 1
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Fator Solar'
            icon: 'weather-sunny'
              

            MDBoxLayout:
                do_scroll_x: False
                bar_width: 10
                bar_color: app.theme_cls.primary_color
                bar_color_acrive: app.theme_cls.accent_color
                effect_cls: "DampedScrollEffect"
                scroll_type: ['bars']
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
            text: 'Inversores'
            icon: 'alpha-i-box-outline'

            MDLabel:
                orientation:'vertical'
                text: 'JS'
                halign: 'center'   

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Condutores'
            icon: 'cable-data'

            MDLabel:
                text: 'I programming of C++'
                halign: 'center'            
'''
        )


Test().run()