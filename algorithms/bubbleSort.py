import time
from colours import *


#bubble sort
def bubble_sort(data, drawData, timeTick):
    size = len(data)

    for i in range(size-1):
        for j in range(size-i-1):

            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                #make the data beign switched around yellow if they are being swapped
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))])
                #stops for a certain amount of time depending on the speed
                time.sleep(timeTick)
    #draw the new sorted data and make everything blue again
    drawData(data, [BLUE for x in range(len(data))])