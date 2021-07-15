from tkinter import*
from tkinter import ttk

#to create an array
import random

#import colours
from colours import *

#Create window
window=Tk()
window.title("sorting Algo")
window.maxsize(1000,700)
#background colour
window.config(bg = WHITE)

algorithm_name = StringVar()
#an array to choose which algo to run
algo_list = ['Bubble Sort', 'Merge Sort']

speed_name = StringVar()
#choosing the speed of the sort
speed_list = ['Fast', 'Medium', 'Slow']

#an empty list to fill with random numbers for the algos to sort
data = []

#Draws the values in the array on screen as vertical bars
def drawData(data, colourArray):
    pass

#Creates an array with random values
def generate():
    pass

#Set the speed
def set_speed():
    pass

#trigger the algorithm and sorts
def sort():
    pass

#User interface ############

#sets the frame for the window, 900x300, white background
UI_frame = Frame(window, width = 900, height = 300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#dropdown menu to pick algo
L1 = Label(UI_frame, text = "Algorithm: ", bg=WHITE)
L1.grid(row = 0, column = 0, padx=10, pady=5, sticky = W)
#a box, in the UI, with the names of the algorithms and the values set in the algo array
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column = 1, padx=5, pady=5)
algo_menu.current(0)

#dropdown menu for speed
L2 = Label(UI_frame, text = "Sorting Speed: " , bg=WHITE)
L2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

#sort button
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row = 2, column=1, padx=5, pady=5)

#button for generating array
b3 = Button(UI_frame, text = "Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row = 2, column= 0, padx=5, pady=5)

#canvas for drawing the array
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)






window.mainloop()