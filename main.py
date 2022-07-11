from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
import random



class StartScreen(Screen):
	
	def checkentry(self):
		field1 = self.ids.text1.text
		field2 = self.ids.text2.text
		if len(field1)==0 or  len(field2)==0 :
			Snackbar(text="Please Check Your Names").show()
			cbutton = MDFlatButton(text='Close',on_release=self.closeNN)
			Close_button = [cbutton]
			self.dialog2 = MDDialog(title='Warning', text="The Following Stats Might Be Falsy Because of Invalid Names. Please Try Again With Corrrect Names", size_hint=(0.95,1), buttons=Close_button)
			self.dialog2.open()
		psbl = ["ayush","Ayush"]
		message = "Woah, It turns out that you are friends with Ayush. Ayush is the the sweetest guy you'll ever meet in your life. Make sure to keep him Happy!"

	def closeN(self,obj):
		self.dialog1.dismiss()

	def closeNN(self,obj):
		self.dialog2.dismiss()

	def callback(self):
		cbutton = MDFlatButton(text='Close',on_release=self.close)
		Close_button = [cbutton]
		self.dialog = MDDialog(title='Share With Your Friends.', text='Share This App with your Friends.\nIn Any Way You Can think Of.', size_hint=(0.95,1), buttons=Close_button)
		self.dialog.open()

	def close(self,obj):
		self.dialog.dismiss()

	def addwidgets(self):
		pass
		

class NextScreen(Screen):
	
	n = 0
	percentage = round(random.randint(1,30) * 3.33 , 2)
		
	def calculator(self):
		
		print(self.percentage)
		return self.percentage

	def level(self, value):
		print(value)
		if value >= 90:
			message = "Extremely Awesomely Fantastic Friendship"
			return message

		elif value >= 80 and value < 90:
			message = "Awesomely Fantastic Friendship"
			return message

		elif value>= 70 and value < 80:
			message = "Fantastic Friendship"
			return message

		elif value >= 50 and value < 70:
			message = "Average Friendship"
			return message

		elif value >= 30 and value < 50:
			message = "You Need to work on your Friendship!"
			return message

		elif value >= 1 and value < 30:
			message = "Do You Even Know This Person?"
			return message
		else:
			pass
	def clearcache(self):
		
		try:
			self.remove_widget(self.ids.box)
			self.remove_widget(self.ids.box1)
		except:
			pass
		
		self.removeW()
		print("Removed")
		self.addW()
		print("Added")
		
		
		
	
	def removeW(self):
		self.n+=1
		if self.n != 1:
			self.remove_widget(self.box)
			self.remove_widget(self.box1)

	def addW(self):
		Npercentage = round(random.randint(1,30) * 3.33 , 2)
		print(Npercentage)
		self.box =  MDLabel(
				text= f"{Npercentage} %",
				halign= 'center',
				font_style= 'H1',
				theme_text_color= 'Custom',
				text_color= (1,0,0,1),
				pos_hint= {'center_x':0.5, 'center_y':0.9})
		self.add_widget(self.box)
		self.box1 = MDLabel(
				text= f"{self.level(Npercentage)}",
				halign= 'center',
				font_style= 'H3',
				theme_text_color= 'Custom',
				text_color= (0,0,1,1),
				pos_hint= {'center_x':0.5, 'center_y':0.5})
		self.add_widget(self.box1)
		

class ScreenManager(ScreenManager):
	pass


class MyApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette= "Purple"
		master = Builder.load_file("main.kv")
		return master
	

MyApp().run()
