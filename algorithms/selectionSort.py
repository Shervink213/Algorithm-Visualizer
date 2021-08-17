import time
from colours import *

def selection_sort(data, drawData, timeTick):
    
    for i in range(len(data)):
        min = i

        for j in range(i+1, len(data)):
            drawData(data, [YELLOW if x == min else PURPLE if x == j else BLUE for x in range(len(data))])
            if data[min] > data[j]:
                min = j
                drawData(data, [YELLOW if x == min else BLUE for x in range(len(data))])
                time.sleep(timeTick)
        
        data[i], data[min] = data[min], data[i]
        drawData(data, [YELLOW if x == i else PURPLE if x == min else BLUE for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, [BLUE for x in range(len(data))])