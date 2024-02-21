import tkinter as tk
from pyowm import OWM
import pygame



API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 500
WIDTH = 1000


root = tk.Tk()
WEATHER_INFO = 7

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

mudic_file = "OlexanderHramatovych/HW9/music.mp3"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(mudic_file)
pygame.mixer.music.play()

def get_weather(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather

    info_about = {
        'Status:': w.detailed_status,
        'Wind:': w.wind(),
        'Humidity:': w.humidity,
        'Temperature:': w.temperature('celsius'),
        'Rain:': w.rain,
        # 'heat_index': w.heat_index,
        'Clouds:': w.clouds
    }

    rely_line = 0

    for item, value in info_about.items():
        info_line = f"{item} {value}"
        line = tk.Label(lower_frame, text=info_line, font=('Courier', 14))
        line.place(relx=0, rely=rely_line)
        rely_line += 0.150


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 18))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="green", fg="white",
                   font=('Courier', 14),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='green', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor='n')
label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()