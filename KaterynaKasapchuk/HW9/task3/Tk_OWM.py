import tkinter as tk
from tkinter import font
from pyowm import OWM
HEIGHT = 350
WIDTH = 450



API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

#weather_info= None
# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather
def get_weather():


    status=w.detailed_status         # 'clouds'
    wind=w.wind()["speed"]                  # {'speed': 4.6, 'deg': 330}
    humidity=w.humidity                # 87
    temprature=w.temperature('celsius')["temp"]  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    rain=w.rain                    # {}
    heat=w.heat_index              # None
    clouds=w.clouds  
    weather_info = f"City: London, GB \n status: {status} \n wind: {wind} \n humidity: {humidity} \n temprature: {temprature} \n rain: {rain} \n heat: {heat} \n clouds: {clouds}"
    label["text"] = weather_info
root = tk.Tk()


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
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10, borderwidth=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')



label = tk.Label(lower_frame,font=('Courier', 14), justify="left")
label.place(relx=0,rely=0,relwidth=1,relheight=1)


city = tk.Label()


root.mainloop()

