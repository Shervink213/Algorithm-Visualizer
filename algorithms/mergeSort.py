<<<<<<< HEAD
import time
from colours import *

def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid+1
    tempArray = []

    for i in range (start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1
    
    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start +=1

def merge_sort(data, start, end, drawData, timeTick):
    if start<end:
        mid = int((start+end)/2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data,mid+1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, [PURPLE if x>= start and x< mid else YELLOW if x == mid
        else DARK_BLUE if x > mid and x <= end else BLUE for x in range(len(data))])

        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

=======
import time
from colours import *

def merge(data, start, mid, end, drawData, timeTick):
    #starting positions
    p = start
    q = mid+1
    #aux array
    tempArray = []

    for i in range (start, end+1):
        #Checks if the left side of the data has been broken up
        if p > mid:
            tempArray.append(data[q])
            q+=1
        #Checks if the right side of the data has been broken up
        elif q > end:
            tempArray.append(data[p])
            p+=1
        #Checks which one is the smaller element
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        #Adds the next variable if the p > q
        else:
            tempArray.append(data[q])
            q+=1
    
    #replaces the values in the data with the values in the tempArray
    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start +=1

#splits up the data and then merges them
def merge_sort(data, start, end, drawData, timeTick):
    if start<end:
        mid = int((start+end)/2) #cuts array in half
        merge_sort(data, start, mid, drawData, timeTick) #breaks up the 1st half of the array
        merge_sort(data,mid+1, end, drawData, timeTick) #breaks up the 2nd half of the array

        merge(data, start, mid, end, drawData, timeTick) #brings both halfs together by comparing both parts

        drawData(data, [PURPLE if x>= start and x< mid else YELLOW if x == mid
        else DARK_BLUE if x > mid and x <= end else BLUE for x in range(len(data))])

        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

>>>>>>> algo-update
