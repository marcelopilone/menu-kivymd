from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

#from kivy.uix.behaviors.button import Button


class MainApp(App):
    theme_cls = ThemeManager()

    def screen1Local(self,*args):
        print(self.email_uno.text)

class screen1():
    def build(self):
	       print("jaja 1")
	#l = Label(text="DADADA")
	#self.add_widget(l)

class screen2():
	print("jaja 2")

MainApp().run()
