import tkinter as tk
from tkinter import font
import requests

HEIGHT = 768
WIDTH = 1366

def test_function(entry):
    print("this is the entry", entry)

# api.openweathermap.org/data/2.5/forecast/hourly?q=London,us&mode=xml
#afa6d756a47f67d4571ea009a04209a7
#50:29

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str


def get_weather(city):
    weather_key = 'afa6d756a47f67d4571ea009a04209a7'
    url ='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH )
canvas.pack()

background_image = tk.PhotoImage(file='mountains2.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = '#80c1ff',bd=5)                              #this frame is where the button fills to
frame.place(relx = 0.5,rely = .1,relwidth = .75, relheight = .1,anchor= 'n')

entry = tk.Entry(frame, font = ('Calibri', 50))
entry.place(relwidth =.65,relheight =1)

button = tk.Button(frame, text="Get Weather",  font = ('Calibri', 35), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg ='#80c1ff', bd=10)
lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight =.6, anchor = 'n')

label = tk.Label(lower_frame, font = ('Calibri', 50))
label.place(relwidth =1, relheight=1)

root.mainloop()