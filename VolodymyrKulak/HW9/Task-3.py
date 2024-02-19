
import tkinter as tk
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 500
WIDTH = 1075


root = tk.Tk()
WEATHER_INFO = 7

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



def get_weather(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather

    info_about = {}

    info_about['Status:'] = w.detailed_status
    info_about['Wind:'] = w.wind()
    info_about['Humidity:'] = w.humidity
    info_about['Temperature:'] = w.temperature('celsius')
    info_about['Rain:'] = w.rain
#   info_about['heat_index'] = w.heat_index
    info_about['Clouds:'] = w.clouds
    rely_line = 0

    for item in info_about.keys():
        info_line = str(item) + ' ' + str(info_about.get(item))
        line = tk.Label(lower_frame, text=info_line, font=('Courier', 14))
        line.place(relx=0, rely=rely_line)
        rely_line += 0.150



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 18))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 14),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor='n')
label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()
