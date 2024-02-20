# Import libraries
import tkinter as tk
import pygame
import pyowm

# Setting window sizes

HEIGHT = 350
WIDTH = 450

# Api key for OpenWetherMap
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

# Initialization PyOWM and Pygame
owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
pygame.mixer.init()
# Create main window
root = tk.Tk()
# Definition function get_weather,play_music,stop_music

# Receiving weather data


def get_weather():
    city = 'London,GB'
    observation = mgr.weather_at_place(city)
    w = observation.weather
    status = w.status
    detailed_status = w.detailed_status
    wind = w.wind()['speed']  # Get the wind speed value
    humidity = w.humidity
    # Get the temperature value
    temperature = w.temperature('celsius')['temp']
    rain = w.rain['1h']
    heat_index = w.heat_index
    clouds = w.clouds
# Split f string
    weather_info = (
        f"City: {city}\n"
        f"Status: {status}\n"
        f"Detailed Status: {detailed_status}\n"
        f"Wind Speed: {wind}\n"
        f"Humidity: {humidity}\n"
        f"Temperature: {temperature}\n"
        f"Rain: {rain}\n"
        f"Heat Index: {heat_index}\n"
        f"Clouds: {clouds}"
    )

    label['text'] = weather_info


# function play music


def play_music():
    pygame.mixer.music.load('play.mp3')
    pygame.mixer.music.play(-1)
# function stop music


def stop_music():
    pygame.mixer.music.stop()


# Creating and placing widgets in the application window
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


# Frame for music control buttons
music_frame = tk.Frame(root, bg="deep sky blue", bd=5)
music_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')
# music button
play_button = tk.Button(music_frame, text="Play Music",
                        bg="gray", fg="white", font=('Courier', 15), command=play_music)
play_button.pack(side='left', padx=5)

stop_button = tk.Button(music_frame, text='Stop Music',
                        bg="gray", fg="white", font=('Courier', 15), command=stop_music)
stop_button.pack(side='right', padx=5)

# Frame for button Weather
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Button Get Weather
button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 15),
                   command=get_weather)
button.place(relx=0.4, rely=0, relwidth=0.3, relheight=1)

# Frame for displaying weather information
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.75,
                  relheight=0.4, anchor='n')

# Label for displaying weather information
label = tk.Label(lower_frame, font=('Courier', 14),
                 justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Main application loop
root.mainloop()
