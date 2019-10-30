from kivy.uix.popup import Popup

class ventanaPopUp():

	def invalidForm():
	            pop = Popup(title='Invalid Form',
	      content=Label(text='Please fill in all inputs with valid information.'),
	      size_hint=(None, None), size=(400, 400))

	            pop.open()