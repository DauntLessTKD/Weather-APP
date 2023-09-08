# Weather App Documentation

# Import necessary libraries and modules
import os
import pytz
import requests
import tkinter as tk
from tkinter import *
from datetime import datetime
from dotenv import load_dotenv
from tkinter import ttk,messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

# Create a Tkinter root window for the Weather App
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Load the environment variables from a .env file
load_dotenv(".env")

# Retrieve the Deta API key from environment variables
API_KEY = os.getenv("API_KEY")

# Function to retrieve weather information
def getWeather():

    try:
        # Get the city name from the input field
        city = textfield.get()

        # Use Nominatim geocoder to obtain the location details
        geolocator = Nominatim(user_agent= "main")
        location = geolocator.geocode(city)

        # Find the timezone for the location
        obj = TimezoneFinder()
        result = obj.timezone_at(lng= location.longitude, lat= location.latitude)

        # Calculate local time based on the timezone
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        # Update the clock and name labels
        clock.config(text= current_time)
        name.config(text= "CURRENT WEATHER")

        # Retrieve weather data from the OpenWeatherMap API
        http = "https://api.openweathermap.org/data/2.5/weather?q="
        api = http + city + f"&appid={API_KEY}"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update the weather-related labels
        t.config(text= (temp, "°"))
        c.config(text= (condition, "|", "FEELS" , "LIKE", temp, "°"))
        w.config(text= wind)
        h.config(text= humidity)
        d.config(text= description)
        p.config(text= pressure)

    except Exception as e:
        # Show an error message if there is an issue with the input
        messagebox.showerror("Weather App", "Invalid Entry!!")


# Search box: Entry field for city input and search button
Search_image = PhotoImage(file= "assets/search.png")
myimage = Label(image= Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width= 17,
                    font= ("poppins", 25, "bold"),bg= "#404040",
                    border= 0, fg= "white")
textfield.place(x= 50, y= 40)
textfield.focus()

Search_icon = PhotoImage(file="assets/search_icon.png")
my_image_icon = Button(image= Search_icon, borderwidth= 0,
                        cursor= "hand2", bg= "#404040", command= getWeather)
my_image_icon.place(x= 400, y= 34)

# Logo: Application logo
Logo_image = PhotoImage(file= "assets/logo.png")
logo = Label(image= Logo_image)
logo.place(x= 150, y= 100)

# Bottom box: Stylish frame at the bottom of the application
Frame_image = PhotoImage(file= "assets/box.png")
frame_my_image = Label(image= Frame_image)
frame_my_image.pack(padx= 5, pady= 5, side= BOTTOM)

# Time: Displays current time based on the selected location
name = Label(root, font= ("arial", 15, "bold"))
name.place(x= 30, y= 100)
clock = Label(root, font= ("Helvetica", 20))
clock.place(x= 30, y= 130)

# Label: Weather information labels for Wind, Humidity, Description, and Pressure
label1 = Label(root, text= "WIND", font=("Helvetica", 15, 'bold'),
                                    fg= "white", bg= "#1ab5ef")
label1.place(x= 120, y= 400)

label2 = Label(root, text= "HUMIDITY", font=("Helvetica", 15, 'bold'),
                                    fg= "white", bg= "#1ab5ef")
label2.place(x= 250, y= 400)

label3 = Label(root, text= "DESCRIPTION", font=("Helvetica", 15, 'bold'),
                                    fg= "white", bg= "#1ab5ef")
label3.place(x= 430, y= 400)

label4 = Label(root, text= "PRESSURE", font=("Helvetica", 15, 'bold'),
                                    fg= "white", bg= "#1ab5ef")
label4.place(x= 650, y= 400)

# Labels for displaying weather data such as temperature, condition, wind, etc.
t = Label(font=("arial", 70, "bold"), fg= "#ee666d")
t.place(x= 400, y= 150)
c = Label(font=("arial", 15, "bold"))
c.place(x= 400, y= 250)
w = Label(text= "", font= ("arial", 20, "bold"), bg= "#1ab5ef")
w.place(x= 120, y= 430)
h = Label(text= "", font= ("arial", 20, "bold"), bg= "#1ab5ef")
h.place(x= 280, y= 430)
d = Label(text= "", font= ("arial", 20, "bold"), bg= "#1ab5ef")
d.place(x= 425, y= 430)
p = Label(text= "", font= ("arial", 20, "bold"), bg= "#1ab5ef")
p.place(x= 700, y= 430)


# Start the main loop to run the Tkinter application
root.mainloop()

