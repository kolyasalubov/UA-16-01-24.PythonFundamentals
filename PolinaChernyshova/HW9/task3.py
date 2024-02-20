from pyowm import OWM
import re
import tkinter as tk
# from tkinter import font, Entry


API_KEY = '9e7bf4f3fc52c3a3e17801ab3230a77a'

HEIGHT = 450
WIDTH = 550

root = tk.Tk()

def get_weather(frame):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(frame)
    w = observation.weather
    weather = f'The weather is {w.detailed_status}'
     
    weather += '\nAbout wind'

    for x, y in w.wind().items():
        weather +=(f'\n{x.capitalize()} = {y}')
    
    label.config(text = weather)
            
    weather += f'\nHumidity = {w.humidity}'

    weather += '\nAbout temperature'
    for x, y in w.temperature('celsius').items():
        x = re.sub('_', ' ', x)
        if y == None:
            weather +=f'\n{x.capitalize()} = We don\'t have information'
        else: 
            weather +=f'\n{x.capitalize()} = {y}'
    
    weather += '\nAbout rain'
    if len(w.rain) != 0: 
        for x, y in w.rain.items():
            if y == None:
                weather += f'\n{x.capitalize()} = We don\'t have information'
            else:
                weather += f'\n{x.capitalize()} = {y}'
    else:
        weather += "\nToday the rain in't in your city"

    if w.heat_index != None:
        weather += f'\nHeat index = {w.heat_index}'
    else:
        weather += "\nWe don't have information about heat index"


    weather +=f'\nThe clouds today is {w.clouds}%'

    label.config(text = weather)




canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame( root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 10))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
