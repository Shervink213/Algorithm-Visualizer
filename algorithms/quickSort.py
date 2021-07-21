import time
from colours import *

def partition(data, start, end):
    i = (start-1)
    piv = data[end] #make first element the pivot point

    #swap the elements that are less than the pivot element with  
    for j in range (start, end):
        if data[j] <= piv:
            i += 1
            data[i], data[j] = data[j], data[i]      

    data[i+1], data[end] = data[end], data[i+1] #Put piv in the right place
    return (i+1) #return position of the pivot

def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        piv_pos = partition(data, start, end) #stores the position of the piv
        quick_sort(data, start, piv_pos -1, drawData, timeTick) #sort left side of the pivot
        quick_sort(data, piv_pos +1, end, drawData, timeTick) #sort the right side of the pivot
        
        drawData(data, [PURPLE if x>= start and x < piv_pos else YELLOW if x == piv_pos
        else DARK_BLUE if x > piv_pos and x <= end else BLUE for x in range(len(data))])

        time.sleep(timeTick)
    
    drawData(data, [BLUE for x in range(len(data))])