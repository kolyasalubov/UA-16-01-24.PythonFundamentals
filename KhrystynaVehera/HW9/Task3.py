from pyowm import OWM
import tkinter as tk
# from tkinter import font

HEIGHT = 350
WIDTH = 450

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

def get_weather(city):
    API_KEY = '7aa287cd0be8d974f12d6a8314d5cba2'


    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    global lower_frame
    global entry_field



    observation = mgr.weather_at_place(city)
    w = observation.weather

    tk.Label(lower_frame, font=('Courier', 11), text=f"City: {city}").grid(row=1, column=2)
    tk.Label(lower_frame, font=('Courier', 11), text=f"Status: {w.detailed_status}").grid(column=2, row=2)
    tk.Label(lower_frame, font=('Courier', 11), text=f"Clouds: {w.clouds}").grid(column=2, row=3)
    tk.Label(lower_frame, font=('Courier', 11), text=f"Humidity: {w.humidity}").grid(column=2, row=4)
    tk.Label(lower_frame, font=('Courier', 11), text=f"Temperature: {w.temperature('celsius')['temp']}").grid(column=2, row=5)
    tk.Label(lower_frame,  font=('Courier', 11), text=f"Rain: {w.rain}").grid(column=2, row=6)
    tk.Label(lower_frame,  font=('Courier', 11), text=f"Heat index: {w.heat_index}").grid(column=2, row=7) 
    tk.Label(lower_frame, font=('Courier', 11), text=f"Wind speed: {w.wind()['speed']}").grid(column=2, row=8)
    tk.Label(lower_frame, font=('Courier', 11), text="       ").grid(column=1, row=8)



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



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()