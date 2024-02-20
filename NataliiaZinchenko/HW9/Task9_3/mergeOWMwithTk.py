from pyowm import OWM
import tkinter

API_KEY = 'ef2206ff5da67de63306d0b143e20872'


HEIGHT = 500
WIDTH = 500


def get_weather():
    """This function displays weather in entered city"""
    city = entry_field.get()
    conditions = mgr.weather_at_place(city)
    weather = conditions.weather


    weather_detailed_status = f"Detailed status: {weather.detailed_status}"
    weather_wind = f"Wind: {weather.wind()}"
    weather_humidity = f"Humidity: {weather.humidity}"
    weather_temperature = f"Temperature: {weather.temperature('celsius')}"
    weather_rain = f"Rain: {weather.rain}"
    weather_heat_index = f"Heat index: {weather.heat_index}"
    weather_clouds = f"Clouds: {weather.clouds}"


    weather_multiline['text'] = f"Weather in {city}:\
                                {weather_detailed_status}\
                                {weather_wind}\
                                {weather_humidity}\
                                {weather_temperature}\
                                {weather_rain}\
                                {weather_heat_index}\
                                {weather_clouds}"


owm = OWM(API_KEY)
mgr = owm.weather_manager()


root = tkinter.Tk()


canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Nataliia's application")
canvas.pack()


frame = tkinter.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry_field = tkinter.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


button = tkinter.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tkinter.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


weather_multiline = tkinter.Message(lower_frame, font=('Courier', 14))
weather_multiline.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()
