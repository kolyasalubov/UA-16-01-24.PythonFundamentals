import tkinter as tk
from tkinter import font
import pyowm

HEIGHT = 350
WIDTH = 450

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

root = tk.Tk()

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()

# Функция для получения информации о погоде
def get_weather():
    city = 'London,GB'  # Город, для которого получаем погоду
    observation = mgr.weather_at_place(city)
    w = observation.weather
    status = w.status
    detailed_status = w.detailed_status
    wind = w.wind()
    humidity = w.humidity
    temperature = w.temperature('celsius')
    rain = w.rain
    heat_index = w.heat_index
    clouds = w.clouds

    weather_info = f"City: {city}\nStatus: {status}\nDetailed Status: {detailed_status}\nWind: {wind}\nHumidity: {humidity}\nTemperature: {temperature}\nRain: {rain}\nHeat Index: {heat_index}\nClouds: {clouds}"
    label['text'] = weather_info

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

# Фрейм для кнопки "Get Weather"
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Кнопка "Get Weather"
button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Фрейм для отображения информации о погоде
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

# Метка для вывода информации о погоде
label = tk.Label(lower_frame, font=('Courier', 14), justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
