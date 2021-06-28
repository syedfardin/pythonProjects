from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("444x233")
root.title("My GUI")

yu = Label(text = """Warangal is a city in the Indian state of \nTelangana. It serves as the district headquarters of both Warangal Urban District and Warangal Rural District.[\n5] With a population of 830,281 per 2011 Census of India,[3][4] and spreading over an 406 km2 (157 sq mi),[1] \nWarangal is the second most populous city in the state after the capital Hyderabad.
\nWarangal served as the capital of the Kakatiya dynasty which was established in 1163. The monuments left by the \nKakatiyas include fortresses, lakes, temples and stone gateways which, in the present, helped the city to \nbecome a popular tourist attraction. The Kakatiya Kala Thoranam was included in the emblem of Telangana by the \nstate government.[6]""",bg = "yellow",fg = "purple",padx = 50, pady = 60,font = "comicsansms 10 bold",borderwidth = 4,relief = SUNKEN)
yu.pack(side = LEFT,fill = Y)


root.mainloop()