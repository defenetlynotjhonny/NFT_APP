from cProfile import label
from tkinter import W, Widget
from application import maximum
from apirequests import Songbird_Api
from fastapi import FastAPI
import requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.text import Label as CoreLabel
from kivy.uix.label import Label

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Nikola was here."}

@app.post("/item")
async def root():
    return ["item of the list i return"]

api_object = Songbird_Api()
api_object.songbird_response_name()
print("###############################################")
api_object.songbird_response_price()
print("###############################################")
api_object.songbird_response("fdsvdsvw")

class TestApp(App):
    def build(self):
        return Button(text='Jhonny was here!')
    
class MyButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'

    def on_press(self):
        self.source = 'atlas://data/images/defaulttheme/checkbox_on'

    def on_release(self):
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'
        
triing = api_object.songbird_response("name")         
    
class MyButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'

    def on_press(self):
        self.source = 'atlas://data/images/defaulttheme/checkbox_on'

    def on_release(self):
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'

class SampleApp(App):
    def build(self):
        listing = ""
        for i in range(len(triing)-1):
            if i % 2 == 0 :
                listing = listing + str(triing[i]) +" : "+ str(triing[(i+1)])+ "\n"
                
        label = Label(text= f'{listing}\n ')
              
        return label
    

SampleApp().run()

    


