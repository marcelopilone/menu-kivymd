from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.widget import Widget
from pprint import pprint
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
import sys #esto sirve para poner un die
import json
import math
import configparser
import ventanaPopUp

#from kivy.uix.behaviors.button import Button


class MainApp(App,BoxLayout):
    theme_cls = ThemeManager()

    def screen1Local(self,val):
        print(val)
        pop = Popup(title='Invalid Form',
            content=Label(text='Please fill in all inputs with valid information.'),
            size_hint=(None, None), size=(400, 400))

        pop.open()

    
        #pprint(vars(*args))
        #pprint(vars(.txt_input_email_uno))
        
        #print('asdasd')
    	#pprint(vars(self.container.children))
    	#sys.exit()
        #print(self.screen_manager.email_uno.text)

class screen1(Screen):	
    def build(self):
	       print("jaja 1")
	#l = Label(text="DADADA")
	#self.add_widget(l)
'''
class screen2():
	print("jaja 2")
'''
if __name__ == '__main__':
    MainApp().run()
