from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from pprint import pprint
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
import sys #esto sirve para poner un die
#from kivy.uix.behaviors.button import Button


class MainApp(App):
    theme_cls = ThemeManager()
    email_uno = ObjectProperty(None)
    email_dos = ObjectProperty(None)
    def screen1Local(self,*args):
    	pprint(vars(self.todoDeTodo.children))
    	sys.exit()
        #print(self.screen_manager.email_uno.text)

class screen1(Screen):	
    def build(self):
	       print("jaja 1")
	#l = Label(text="DADADA")
	#self.add_widget(l)

class screen2():
	print("jaja 2")

MainApp().run()
