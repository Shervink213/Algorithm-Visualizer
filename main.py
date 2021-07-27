from tkinter import*
from tkinter import ttk

#to create an array
import random

#import colours
from colours import *

#import algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.insertionSort import insertion_sort
from algorithms.selectionSort import selection_sort

#Create window
window=Tk()
window.title("sorting Algo")
window.maxsize(1000,700)
#background colour
window.config(bg = WHITE)

algorithm_name = StringVar()
#an array to choose which algo to run
algo_list = ['Bubble Sort','Insertion Sort','Selection Sort', 'Merge Sort', 'Quick Sort']

speed_name = StringVar()
#choosing the speed of the sort
speed_list = ['Fast', 'Medium', 'Slow']

#an empty list to fill with random numbers for the algos to sort
data = []

#Draws the values in the array on screen as vertical bars
def drawData(data, colourArray):
    #clears the screen
    canvas.delete("all")
    #resolution
    canvas_width = 800
    canvas_height = 400
    #the width of the UI is the width of the canvas divided by all
    #the numbers in the array + 1
    x_width = canvas_width / (len(data)+1)
    #for better UI
    offset = 4
    spacing = 2
    #makes the data better to use in for the UI
    normalizedData = [i / max(data) for i in data]

    #for each value in the array, it creates a rectangle of it's size
    ## loops over the data points but assigns a count to each data value
    for i, height in enumerate(normalizedData):
        #bottom left point, sets the point on the screen 
        x0 = i* x_width + offset + spacing
        #top left point
        y0 = canvas_height - height * 390
        #bottom right point
        x1 = (i+1)*x_width + offset
        #top right point
        y1 = canvas_height
        #creates the rectangle given the points, fills in the colour
        canvas.create_rectangle(x0, y0, x1, y1, fill=colourArray[i])

    window.update_idletasks()

#Creates an array with random values
def generate():
    #creates an array that everything can use
    global data
    data = []

    #find a random number, puts it in the array
    for i in range(0,100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    #call Draw data to create all the rectangles and colour it all blue
    drawData(data, [BLUE for x in range(len(data))])

#Set the speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.5
    elif speed_menu.get() == 'Medium':
        return 0.05
    else:
        return 0.005

#trigger the algorithm and sorts
def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)

    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, (len(data)-1), drawData, timeTick)

    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, (len(data)-1), drawData, timeTick)
    
    
    

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