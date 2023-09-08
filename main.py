from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


# Search box
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
                        cursor= "hand2", bg= "#404040")
my_image_icon.place(x= 400, y= 34)

# Logo
Logo_image = PhotoImage(file= "assets/logo.png")
logo = Label(image= Logo_image)
logo.place(x= 150, y= 100)

# Bottom box
Frame_image = PhotoImage(file= "assets/box.png")
frame_my_image = Label(image= Frame_image)
frame_my_image.pack(padx= 5, pady= 5, side= BOTTOM)

# Label
label1 = Label(root, text= "WIND", font=("Helvetica", 15, 'bold'),
                                    fg= "white", bg= "#1ab5ef")




root.mainloop()

