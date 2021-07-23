import time
from colours import *


def insertion_sort(data, drawData, timeTick):

    #go through the array
    for i in range (1, len(data)):

        #J will the best value being compared to the key
        key = data[i]
        j=i-1

        #move value of data[j] ahead of the key if the value is greater than the key
        while j >= 0 and key < data[j]:
            #purple is being compared against yellow
            drawData(data, [PURPLE if x == j else YELLOW if x == j+1 else BLUE for x in range(len(data))])
            time.sleep(timeTick)
            data[j+1] = data[j]
            j-=1
            drawData(data, [PURPLE if x == j else YELLOW if x == j+1 else BLUE for x in range(len(data))]) 
            time.sleep(timeTick)
        data[j+1] = key
        drawData(data, [YELLOW if x == j+1 else BLUE for x in range(len(data))])
        time.sleep(timeTick) 
    
    drawData(data, [BLUE for x in range(len(data))])
