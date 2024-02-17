import tkinter as tk
from tkinter import font
from pyowm import OWM

def get_weather(city:str)->str:
    """
    Name: get_weater
    input parameters: city
    type number1: str
    function return str object
    """
    observation = mgr.weather_at_place(city)
    w = observation.weather 
    city_weater = {}
    city_weater['detailed_status'] = w.detailed_status
    city_weater['wind'] = w.wind()
    city_weater['humidity'] = w.humidity
    city_weater['temperature'] = w.temperature('celsius')
    city_weater['rain'] = w.rain
    city_weater['heat_index'] = w.heat_index
    city_weater['clouds'] = w.clouds
    rely_label = 0
    for item in city_weater.keys():
        text_label = str(item) + ' ' + str(city_weater.get(item))
        label = tk.Label(lower_frame,text=text_label, font=('Courier', 8))
        label.place(relx=0, rely=rely_label)
        rely_label +=0.143

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450


root = tk.Tk()
WEATHER_INFO = 7

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

#weather_info = get_weather(entry_field.get())

lower_frame = tk.Frame(root, bg='gold', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor='n')
label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()

